from PyQt5.QtWidgets import QDialog
from ui import Ui_MainWindow,Ui_addEditAppointment_form,Ui_appointmentInfo_form
from models import DatabaseManager,UtilityFetcher
from PyQt5.QtWidgets import QMessageBox
from models import Doctors,Services,Appointments,Patients
from PyQt5.QtCore import pyqtSignal
from utility import LoadingValues,Dates,Numbers
from PyQt5.QtWidgets import QListWidgetItem
import jdatetime
from utility import Dates

class AppointmentsTabController:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        LoadingValues.load_date_spin_box_values(self.ui)
        self.load_today_appointments_list()
        self._connect_buttons()
        
    def _connect_buttons(self):
        self.ui.appointments_lst.itemDoubleClicked.connect(self.open_appointment_info)
        self.ui.AppointmentSearchByDate_btn.clicked.connect(self.search_appointments_by_date)
        self.ui.todayAppointmentSearch_btn.clicked.connect(self.load_today_appointments_list)
        self.ui.tomorrowAppointmentSearch_btn.clicked.connect(lambda: self._load_future_date_appointments(1))
        self.ui.twoDayAppointmentSearch_btn.clicked.connect(lambda: self._load_future_date_appointments(2))
        self.ui.threeDayAppointmentSearch_btn.clicked.connect(lambda: self._load_future_date_appointments(3))
        self.ui.fourDayAppointmentSearch_btn.clicked.connect(lambda: self._load_future_date_appointments(4))

    def open_appointment_info(self,item):
        appointment_id = item.data(1)
        self.appointment_info_controller = AppointmentInfoController(appointment_id)
        self.appointment_info_controller.show()

    def _load_future_date_appointments(self, days_ahead):
        date = Dates.get_future_date(days_ahead)
        self._load_appointments_by_date(date)

    def search_appointments_by_date(self):
        year, month, day = self.ui.year_spnbox.value(), self.ui.month_spnbox.value(), self.ui.day_spnbox.value()
        date_str = jdatetime.date(year, month, day).strftime("%Y-%m-%d")
        self._load_appointments_by_date(date_str)

    def load_today_appointments_list(self):
        today_date = jdatetime.date.today().strftime("%Y-%m-%d")
        self._load_appointments_by_date(today_date)

    def _load_appointments_by_date(self, date):
        with DatabaseManager() as db:
            appointments = Appointments.get_by_date(db, date)
            self._load_data_into_appointment_list(db, appointments)

    def _load_data_into_appointment_list(self, db, appointments):
        self.ui.appointments_lst.clear()
        for appointment in appointments:
            patient_full_name, service_name, doctor_full_name = (
                UtilityFetcher.get_patient_service_doctor_names(
                    db,
                    appointment["patient"],
                    appointment["service"],
                    appointment["doctor"],
                )
            )
            date = Dates.convert_to_jalali_format(appointment["jalali_date"])
            time = Numbers.english_to_persian_numbers(appointment["time"])
            description = appointment["description"] or "بدون توضیحات"
            item_txt = f"{patient_full_name} | {service_name} | دکتر {doctor_full_name} | {appointment['status']} | {date} | {time} | {description}"
            item = QListWidgetItem(item_txt)
            item.setData(1, appointment["id"])
            self.ui.appointments_lst.addItem(item)

class AppointmentInfoController(QDialog):

    def __init__(self,appointment_id):
        super(AppointmentInfoController, self).__init__()
        self.ui = Ui_appointmentInfo_form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.appointment_id = appointment_id

        self.load_appointment_data()
        self._connect_buttons()

    def _connect_buttons(self):
        pass

    def load_appointment_data(self):
        appointment_id = self.appointment_id

        with DatabaseManager() as db:
            appointment = Appointments.get_by_id(db,appointment_id)
            patient_full_name, service_name, doctor_full_name = (
                UtilityFetcher.get_patient_service_doctor_names(
                    db,
                    appointment["patient"],
                    appointment["service"],
                    appointment["doctor"],
                )
            )
            jalali_date = Dates.convert_to_jalali_format(appointment["jalali_date"])
            time = Numbers.english_to_persian_numbers(appointment["time"])
            description = appointment["description"] or "بدون توضیحات"
           
            self.ui.patientFullName_lbl.setText(patient_full_name)
            self.ui.serviceName_lbl.setText(service_name)
            self.ui.doctorName_lbl.setText(f"دکتر {doctor_full_name}")
            self.ui.datetime_lbl.setText(f"{jalali_date} ساعت {time}")
            self.ui.status_lbl.setText(appointment["status"])
            self.ui.description_lbl.setText(description)


class AddEditAppointmentController(QDialog):
    refresh_appointment_list = pyqtSignal()

    def __init__(self,patient_id):
        super(AddEditAppointmentController, self).__init__()
        self.ui = Ui_addEditAppointment_form()
        self.ui.setupUi(self)
        self.setModal(True)

        self.patient_id = patient_id
        
        LoadingValues.load_doctors_services_combo_boxes(self.ui)
        LoadingValues.load_date_spin_box_values(self.ui)

        self.ui.save_btn.clicked.connect(self.save_appointment)
        self.ui.cancel_btn.clicked.connect(self.close)

    def save_appointment(self):
        year = self.ui.year_spnbox.value()
        month = self.ui.month_spnbox.value()
        day = self.ui.day_spnbox.value()
        jalali_date_str = jdatetime.date(year,month,day).strftime("%Y-%m-%d")

        hour = self.ui.hour_spnbox.value()
        minute = self.ui.minute_spnbox.value()
        time_str = f"{hour}:{minute}"

        greg_datetime = jdatetime.datetime(year,month,day,hour,minute).togregorian().strftime('%Y-%m-%d %H:%M')

        appointment = {
            'status': self.ui.status_cmbox.currentText().strip(),
            'jalali_date': jalali_date_str.strip(),
            'greg_datetime': greg_datetime.strip(),
            "time": time_str.strip(),
            "doctor": self.ui.doctor_cmbox.currentData(),
            "service": self.ui.service_cmbox.currentData(),
            "description": self.ui.description_txtbox.toPlainText().strip(),
            "patient": self.patient_id,
        }

        with DatabaseManager() as db:
            Appointments.add_appointment(db,appointment)
            QMessageBox.information(self, "موفقیت", "نوبت با موفقیت اضافه شد.")
            self.refresh_appointment_list.emit()
            self.close()
