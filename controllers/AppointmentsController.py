from PyQt5.QtWidgets import QDialog
from ui import Ui_MainWindow,Ui_addEditAppointment_form,Ui_appointmentInfo_form
from models import DatabaseManager,UtilityFetcher
from models import Services,Appointments,MedicalRecords
from PyQt5.QtCore import pyqtSignal
from utility import LoadingValues,Dates,Numbers,Messages
from PyQt5.QtWidgets import QListWidgetItem
import jdatetime

class AppointmentsTabController:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        LoadingValues.load_current_date_spin_box_values(self.ui)
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
        self.appointment_info_controller.load_today_appointments_list.connect(self.load_today_appointments_list)
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
            patient, service, doctor_full_name = (
                UtilityFetcher.get_patient_service_doctor_names(
                    db,
                    appointment["patient"],
                    appointment["service"],
                    appointment["doctor"],
                )
            )
            date = Dates.convert_to_jalali_format(appointment["jalali_date"])
            time = Numbers.english_to_persian_numbers(appointment["time"])
            phone_number = Numbers.english_to_persian_numbers(patient["phoneNumber"])

            description = appointment["description"] or "بدون توضیحات"
            item_txt = f"{patient["fullName"]} | {phone_number} | {service["name"]} | دکتر {doctor_full_name} | {appointment['status']} | {date} | {time} | {description}"
            item = QListWidgetItem(item_txt)
            item.setData(1, appointment["id"])
            self.ui.appointments_lst.addItem(item)

class AppointmentInfoController(QDialog):
    load_today_appointments_list = pyqtSignal()
    load_user_appointment_list = pyqtSignal()
    load_user_medical_records_list = pyqtSignal()

    def __init__(self,appointment_id):
        super(AppointmentInfoController, self).__init__()
        self.ui = Ui_appointmentInfo_form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.appointment_id = appointment_id

        self.load_appointment_data()
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.deleteAppointment_btn.clicked.connect(self.delete_appointment)
        self.ui.sendReminderSMS_btn.clicked.connect(self.send_reminder_sms)
        self.ui.editAppointment_btn.clicked.connect(self.open_edit_appointment)
        self.ui.addAppointmentToMedicalRecords_btn.clicked.connect(self.add_appointment_to_medical_records)

    def add_appointment_to_medical_records(self):
        msg_box, yes_button = Messages.show_confirm_msg()
        if msg_box.clickedButton() == yes_button:
            with DatabaseManager() as db:
                appointment = Appointments.get_by_id(db,self.appointment_id)
                service_price = Services.get_by_id(db,appointment["service"])["price"]
                greg_date = appointment["greg_datetime"].split(" ")[0]
                
                medical_record_data = {
                    "jalali_date": appointment["jalali_date"],
                    "doctor": appointment["doctor"],
                    "service": appointment["service"],
                    "price":service_price,
                    "description": appointment["description"],
                    "patient": appointment["patient"],
                    "greg_date": greg_date,
                }

                try:
                    MedicalRecords.add_medical_record(db,medical_record_data)
                    Appointments.delete_appointment(db,self.appointment_id)
                    Messages.show_success_msg("نوبت با موفقیت به پرونده خدمات ارائه شده بیمار اضافه شد.")
                    self.load_today_appointments_list.emit()
                    self.load_user_appointment_list.emit()
                    self.load_user_medical_records_list.emit()
                except:
                    Messages.show_error_msg("عملیات با خطا مواجه شد. لطفا مجدد امتحان کنید")
                self.close()
        else:
            msg_box.close()

    def send_reminder_sms(self):
        # TO-DO
        pass

    def delete_appointment(self):
        msg_box, yes_button = Messages.show_confirm_delete_msg()
        if msg_box.clickedButton() == yes_button:
            with DatabaseManager() as db:
                Appointments.delete_appointment(db,self.appointment_id)
                Messages.show_success_msg("نوبت با موفقیت حذف شد.")
                self.close()
                self.load_today_appointments_list.emit()
                self.load_user_appointment_list.emit()
        else:
            msg_box.close()

    def open_edit_appointment(self):
        with DatabaseManager() as db:
            appointment = Appointments.get_by_id(db,self.appointment_id)
        self.edit_appointment_controller = AddEditAppointmentController(appointment=appointment)
        self.edit_appointment_controller.refresh_appointment_info_data.connect(
            self.load_appointment_data
        )
        self.edit_appointment_controller.refresh_user_appointment_list_data.connect(
            self.load_user_appointment_list
        )
        self.edit_appointment_controller.load_today_appointments_list.connect(
            self.load_today_appointments_list
        )
        self.edit_appointment_controller.show()

    def load_appointment_data(self):
        appointment_id = self.appointment_id

        with DatabaseManager() as db:
            appointment = Appointments.get_by_id(db,appointment_id)
            patient, service, doctor_full_name = (
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
            phone_number = Numbers.english_to_persian_numbers(patient["phoneNumber"])

            self.ui.patientFullName_lbl.setText(patient["fullName"])
            self.ui.phoneNumber_lbl.setText(phone_number)
            self.ui.serviceName_lbl.setText(service["name"])
            self.ui.doctorName_lbl.setText(f"دکتر {doctor_full_name}")
            self.ui.datetime_lbl.setText(f"{jalali_date} ساعت {time}")
            self.ui.status_lbl.setText(appointment["status"])
            self.ui.description_lbl.setText(description)


class AddEditAppointmentController(QDialog):
    load_today_appointments_list = pyqtSignal()
    refresh_appointment_info_data = pyqtSignal()
    refresh_user_appointment_list_data = pyqtSignal()

    def __init__(self, patient_id=None, appointment=None):
        super(AddEditAppointmentController, self).__init__()
        self.ui = Ui_addEditAppointment_form()
        self.ui.setupUi(self)
        self.setModal(True)

        self.patient_id = patient_id
        self.appointment = appointment
        self._load_initial_values()

        if appointment:
            self.patient_id = appointment["patient"]
            self.ui.title_lbl.setText("ویرایش نوبت")
            self.load_appointment_data_into_txtboxes()

        self._connect_buttons()

    def _load_initial_values(self):
        LoadingValues.load_doctors_services_combo_boxes(self.ui)
        LoadingValues.load_current_date_spin_box_values(self.ui)

    def _connect_buttons(self):
        self.ui.save_btn.clicked.connect(self.save_appointment)
        self.ui.cancel_btn.clicked.connect(self.close)

    def load_appointment_data_into_txtboxes(self):
        appointment = self.appointment
        with DatabaseManager() as db:
            _, service, doctor_full_name = UtilityFetcher.get_patient_service_doctor_names(
                db, None, appointment["service"], appointment["doctor"]
            )

        self.ui.doctor_cmbox.setCurrentText(f"دکتر {doctor_full_name}")
        self.ui.service_cmbox.setCurrentText(service["name"])
        self.ui.status_cmbox.setCurrentText(appointment["status"])
        self.ui.description_txtbox.setText(appointment["description"])

        LoadingValues.load_date_into_date_spinbox(self.ui, appointment["jalali_date"])
        LoadingValues.load_time_into_time_spnbox(self.ui, appointment["time"])

    def save_appointment(self):
        jalali_date_str = self._get_jalali_date()
        time_str = self._get_time_str()
        greg_datetime = self._get_gregorian_datetime(jalali_date_str, time_str)

        appointment_data = {
            'status': self.ui.status_cmbox.currentText().strip(),
            'jalali_date': jalali_date_str,
            'greg_datetime': greg_datetime,
            'time': time_str,
            'doctor': self.ui.doctor_cmbox.currentData(),
            'service': self.ui.service_cmbox.currentData(),
            'description': self.ui.description_txtbox.toPlainText().strip(),
            'patient': self.patient_id,
        }

        with DatabaseManager() as db:
            if self.appointment:
                appointment_data["id"] = self.appointment["id"]
                Appointments.update_appointment(db, appointment_data)
                success_msg = "نوبت با موفقیت ویرایش شد."
                self.refresh_appointment_info_data.emit()
            else:
                Appointments.add_appointment(db, appointment_data)
                success_msg = "نوبت با موفقیت اضافه شد."

            Messages.show_success_msg(success_msg)
            self.load_today_appointments_list.emit()
            self.refresh_user_appointment_list_data.emit()
            self.close()

    def _get_jalali_date(self):
        year = self.ui.year_spnbox.value()
        month = self.ui.month_spnbox.value()
        day = self.ui.day_spnbox.value()
        return jdatetime.date(year, month, day).strftime("%Y-%m-%d")

    def _get_time_str(self):
        hour = self.ui.hour_spnbox.value()
        minute = self.ui.minute_spnbox.value()
        return f"{hour}:{minute}"

    def _get_gregorian_datetime(self, jalali_date_str, time_str):
        year, month, day = map(int, jalali_date_str.split('-'))
        hour, minute = map(int, time_str.split(':'))
        return jdatetime.datetime(year, month, day, hour, minute).togregorian().strftime('%Y-%m-%d %H:%M')
