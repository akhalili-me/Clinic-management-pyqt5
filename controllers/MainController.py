from PyQt5.QtWidgets import QMainWindow, QDialog
from ui import get_ui_class
from utility import (
    DatabaseUtils,
    Messages,
    restart_app,
    copy_file_to_directory,
    BaseController,
    ConfigUtils,
    Dates,
    FetchTodayDateEventWorker,
    Numbers,
)
from models import Reports,Backup
from PyQt5.QtWidgets import QFileDialog
import jdatetime
from controllers import (
    DoctorsTabController,
    PatientsTabController,
    ServicesTabController,
    AppointmentsTabController,
    ExpenseTabController,
    ReportsTabController,
    MedicalRecordsTabController
)
import logging
from PyQt5.QtCore import QObject, pyqtSignal


class SignalDispatcher(QObject):
    refresh_appointments_list = pyqtSignal()
    refresh_main_tab_reports = pyqtSignal()
    reload_report_services = pyqtSignal()
    load_today_medical_records_list = pyqtSignal()
    refresh_patient_medical_records_list = pyqtSignal()


class MainTabController(BaseController):
    def __init__(
        self,
        ui,
        dispatcher
    ):
        self.ui = ui
        self.active_workers = []
        dispatcher.refresh_main_tab_reports.connect(self.load_daily_reports)
        self.load_daily_reports()
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.reloadDailyData_btn.clicked.connect(self.load_daily_reports)

    def load_daily_reports(self):
        today_date = jdatetime.date.today().strftime("%Y-%m-%d")
        date_str = Dates.convert_to_jalali_format(today_date)
        self.ui.todayDate_lbl.setText(date_str)
        self.get_today_events()
        self.get_appointment_medical_records_count()
        self.get_latest_backup_date()

    def get_today_events(self):
        event_worker = FetchTodayDateEventWorker()
        event_worker.result_signal.connect(self.display_today_events)
        event_worker.error_signal.connect(self.handle_event_fetch_error)
        event_worker.finished.connect(lambda: self.active_workers.remove(event_worker))
        self.active_workers.append(event_worker)
        event_worker.start()

    def handle_event_fetch_error(self,error_msg):
        logging.error(error_msg)
        self.ui.dateEvents_txtedit.setText('واکشی مناسبت‌ها با خطا مواجه شده است.')

    def display_today_events(self,events_data):
        unique_descriptions = set(event['description'] for event in events_data['events'])

        events = ' - '.join(unique_descriptions)
        if events_data['is_holiday']:
            events = "تعطیل است  -  " + events

        self.ui.dateEvents_txtedit.setText(events)

    def get_appointment_medical_records_count(self,):
        today_date = jdatetime.date.today().strftime("%Y-%m-%d")
        self._start_worker(
            Reports.get_service_medical_records_count,
            [today_date],
            self.display_appointment_medical_records_count,
        )

    def display_appointment_medical_records_count(self,data):
        appointment_txt = f"امروز {Numbers.english_to_persian_numbers(data["appointments_count"])} نوبت در انتظار رسیدگی شما است."
        medical_records_txt = f"{Numbers.english_to_persian_numbers(data["medical_records_count"])} خدمات جدید امروز ثبت شده است."
        self.ui.dailyAppointmentsCount_lbl.setText(appointment_txt)
        self.ui.dailyMedicalRecordsCount_lbl.setText(medical_records_txt)

    def get_latest_backup_date(self):
        self._start_worker(
            Backup.get_latest_backup_date,
            [],
            result_callback=self.display_latest_backup_date,
        )

    def display_latest_backup_date(self,backup):
        if backup:
            jalali_date = self._convert_greg_to_jalali(backup["date"])
            latest_backup_txt = f"آخرین بار {jalali_date} از دیتابیس پشتیبان گرفته شده است."
        else:
            latest_backup_txt = "هنوز هیج پشتیبانی از دیتابیس گرفته نشده است."
        self.ui.latestBackupDate_lbl.setText(latest_backup_txt)

    def _convert_greg_to_jalali(self,greg_date_str):
        year, month, day = map(int, greg_date_str.split('-'))
        jalali_date = jdatetime.GregorianToJalali(year, month, day).getJalaliList()
        jalali_str = jdatetime.date(*jalali_date).strftime("%Y/%m/%d")

        return Numbers.english_to_persian_numbers(jalali_str)

class AppController(BaseController, QMainWindow):
    def __init__(self):
        super(AppController, self).__init__()
        self.ui = get_ui_class("main")()
        self.ui.setupUi(self)
        self.active_workers = []
        self._connect_buttons()

        # Initialize the dispatcher
        self.dispatcher = SignalDispatcher()

        # Initialize tabs with the dispatcher passed to those that need it
        self.main_tab_controller = MainTabController(self.ui, self.dispatcher)
        self.appointments_tab_controller = AppointmentsTabController(
            self.ui, self.dispatcher
        )
        self.doctors_tab_controller = DoctorsTabController(self.ui, self.dispatcher)
        self.patients_tab_controller = PatientsTabController(self.ui, self.dispatcher)
        self.expense_tab_controller = ExpenseTabController(self.ui)
        self.report_controller = ReportsTabController(self.ui, self.dispatcher)
        self.services_tab_controller = ServicesTabController(self.ui, self.dispatcher)
        self.medical_records_tab_controller = MedicalRecordsTabController(
            self.ui, self.dispatcher
        )

    def _connect_buttons(self):
        self.ui.save_backup.triggered.connect(self.save_database_backup)
        self.ui.import_backup.triggered.connect(self.import_database)
        self.ui.insertSMSApiKey.triggered.connect(self.open_sms_api_key)

    def save_database_backup(self):
        db_path = DatabaseUtils.get_database_path()

        dir_dialog = QFileDialog(self)
        selected_dir_path = dir_dialog.getExistingDirectory()

        if selected_dir_path:
            current_time = jdatetime.datetime.now().strftime("%Y-%m-%d %H-%M")
            file_name = "Revita backup " + current_time + ".sqlite"
            try:
                copy_file_to_directory(db_path, selected_dir_path, file_name)
            except Exception as e:
                error_msg = f"""
                کپی کردن فایل دیتابیس با خطا مواجه شده است.
                {str(e)}
                """
                logging.error(error_msg)
                Messages.show_error_msg(error_msg)
                return
            self.add_new_backup_date()

    def import_database(self):
        new_db_path = DatabaseUtils.import_database()

        if not DatabaseUtils.validate_database(new_db_path):
            Messages.show_error_msg("پایگاه داده انتخابی معتبر نمی‌باشد.")
            return
        DatabaseUtils.save_new_path(new_db_path)
        restart_app()

    def open_sms_api_key(self):
        self.import_api_controller = ImportSMSApiController()
        self.import_api_controller.show()

    def add_new_backup_date(self):
        today_date = jdatetime.date.today().togregorian().strftime("%Y-%m-%d")
        self._start_worker(
            Backup.add_backup_info,
            [today_date],
            success_callback=self.handle_sucess_add_backup_date,
        )

    def handle_sucess_add_backup_date(self):
        success_msg = """
            پایگاه داده با موفقیت ذخیره شد. 
            فراموش نشود پوشه مدیا برنامه در مسیر پایگاه داده کپی شود.
        """
        self.dispatcher.refresh_main_tab_reports.emit()
        Messages.show_success_msg(success_msg)

class ImportSMSApiController(BaseController, QDialog):

    def __init__(self):
        super(ImportSMSApiController, self).__init__()
        self.ui = get_ui_class("aSmsApi")()
        self.ui.setupUi(self)
        self.setModal(True)
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.save_btn.clicked.connect(self.validate_form)
        self.ui.cancel_btn.clicked.connect(self.close)

    def validate_form(self):
        sms_api_key = self.ui.apiKey_txtbox.toPlainText().strip()
        if len(sms_api_key) == 0:
            Messages.show_error_msg("کلیدی وارد نشده است.")
            return
        if len(sms_api_key) < 50:
            Messages.show_error_msg("کلید وارد شده صحیح نمی‌باشد.")
            return
        self.save_api_key()

    def save_api_key(self):
        msg_box, yes_button = Messages.show_confirm_msg()
        if msg_box.clickedButton() != yes_button:
            msg_box.close()
            return

        sms_api_key = self.ui.apiKey_txtbox.toPlainText().strip()
        ConfigUtils.set_value("sms_api_key", sms_api_key)
        Messages.show_success_msg("کلید سرویس پیامکی با موفقیت ذخیره شد.")
        self.close()
