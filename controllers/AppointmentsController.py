from PyQt5.QtWidgets import QDialog
from ui import Ui_MainWindow,Ui_addEditAppointment_form,Ui_appointmentInfo_form
from models import DatabaseManager
from models import Services,Appointments,MedicalRecords
from PyQt5.QtCore import pyqtSignal
from utility import LoadingValues,Dates,Numbers,Messages,SpecialDays,SMS
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
        self.ui.appointmentSearchByDay_btn.clicked.connect(self.search_appointments_by_day_select)
        self.ui.sendToAllSMSByDays_btn.clicked.connect(self.send_sms_to_searched_list)

    def open_appointment_info(self,item):
        appointment_id = item.data(1)
        self.appointment_info_controller = AppointmentInfoController(appointment_id)
        self.appointment_info_controller.load_today_appointments_list.connect(self.load_today_appointments_list)
        self.appointment_info_controller.show()

    def _load_future_date_appointments(self, days_ahead):
        date = Dates.get_future_date(days_ahead)
        self._load_data_into_appointment_list(date)

    def send_sms_to_searched_list(self):

        selected_day = self.ui.sendToAllSMSByDays_cmbox.currentText().strip()

        if selected_day == SpecialDays.TODAY.value:
            selected_date  = jdatetime.date.today().strftime("%Y-%m-%d")
        elif selected_day == SpecialDays.TOOMMORROW.value:  
            selected_date =  Dates.get_future_date(days_ahead=1)
        elif selected_day == SpecialDays.TWO_DAYS_LATER.value:  
            selected_date =  Dates.get_future_date(days_ahead=2)
        elif selected_day == SpecialDays.THREE_DAYS_LATER.value:  
            selected_date =  Dates.get_future_date(days_ahead=3)
        elif selected_day == SpecialDays.FOUR_DAYS_LATER.value:  
            selected_date =  Dates.get_future_date(days_ahead=4)

        appointments = self._get_appointments_by_jalali_date(selected_date)

        for appointment in appointments:
            #send reminder sms as async
            pass

    def search_appointments_by_day_select(self):
        selected_day = self.ui.appointmentSearchDaySelect_cmbox.currentText().strip()

        day_to_function = {
            SpecialDays.TODAY.value: self.load_today_appointments_list,
            SpecialDays.TOOMMORROW.value: lambda: self._load_future_date_appointments(1),
            SpecialDays.TWO_DAYS_LATER.value: lambda: self._load_future_date_appointments(2),
            SpecialDays.THREE_DAYS_LATER.value: lambda: self._load_future_date_appointments(3),
            SpecialDays.FOUR_DAYS_LATER.value: lambda: self._load_future_date_appointments(4),
        }
        
        selected_function = day_to_function.get(selected_day)
        if selected_function:
            selected_function()

    def search_appointments_by_date(self):
        year, month, day = self.ui.year_spnbox.value(), self.ui.month_spnbox.value(), self.ui.day_spnbox.value()
        date_str = jdatetime.date(year, month, day).strftime("%Y-%m-%d")
        self._load_data_into_appointment_list(date_str)

    def load_today_appointments_list(self):
        today_date = jdatetime.date.today().strftime("%Y-%m-%d")
        self._load_data_into_appointment_list(today_date)

    def _get_appointments_by_jalali_date(self,date):
        with DatabaseManager() as db:
            try:
                return Appointments.get_by_jalali_date(db, date)
            except Exception as e:
                Messages.show_error_msg(str(e))
                return
            
    def _load_data_into_appointment_list(self,date):
        self.ui.appointments_lst.clear()
        appointments = self._get_appointments_by_jalali_date(date)
        for appointment in appointments:  
            date = Dates.convert_to_jalali_format(appointment["jalali_date"])
            time = Numbers.english_to_persian_numbers(appointment["time"])
            phone_number = Numbers.english_to_persian_numbers(appointment["phone_number"])
            description = appointment["description"] or "بدون توضیحات"
            item_txt = f"{appointment["patient_name"]} | {phone_number} | {appointment["service_name"]} | دکتر {appointment["doctor_name"]} | {appointment['status']} | {date} | {time} | {description}"
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
        self.appointment = self._get_appointment_data(appointment_id)
        self.load_appointment_data(self.appointment)
        self._connect_buttons()

    def _get_appointment_data(self,appointment_id):
        with DatabaseManager() as db:
            try:
                return Appointments.get_appointment_details_by_id(db,appointment_id)
            except Exception as e:
                Messages.show_error_msg(str(e))
                
    def _connect_buttons(self):
        self.ui.deleteAppointment_btn.clicked.connect(self.delete_appointment)
        self.ui.sendReminderSMS_btn.clicked.connect(self.send_reminder_sms)
        self.ui.editAppointment_btn.clicked.connect(self.open_edit_appointment)
        self.ui.addAppointmentToMedicalRecords_btn.clicked.connect(self.add_appointment_to_medical_records)

    def add_appointment_to_medical_records(self):
        msg_box, yes_button = Messages.show_confirm_msg()
        if msg_box.clickedButton() == yes_button:
            appointment = self.appointment
            
            greg_date = appointment["greg_datetime"].split(" ")[0]
            medical_record_data = {
                "jalali_date": appointment["jalali_date"],
                "doctor": appointment["doctor"],
                "service": appointment["service"],
                "price":appointment["service_price"],
                "description": appointment["description"],
                "patient": appointment["patient"],
                "greg_date": greg_date,
            }
            with DatabaseManager() as db:
                try:
                    MedicalRecords.add_medical_record(db,medical_record_data)
                    Appointments.delete_appointment(db,self.appointment.id)
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
                try:
                    Appointments.delete_appointment(db,self.appointment.id)
                except Exception as e:
                    Messages.show_error_msg(str(e))
                    return
                
                Messages.show_success_msg("نوبت با موفقیت حذف شد.")
                self.close()
                self.load_today_appointments_list.emit()
                self.load_user_appointment_list.emit()
        else:
            msg_box.close()

    def open_edit_appointment(self):
        self.edit_appointment_controller = AddEditAppointmentController(appointment_id=self.appointment["id"])
        self.edit_appointment_controller.refresh_appointment_info_data.connect(
            self._refresh_appointment_info_data
        )
        self.edit_appointment_controller.refresh_user_appointment_list_data.connect(
            self.load_user_appointment_list
        )
        self.edit_appointment_controller.load_today_appointments_list.connect(
            self.load_today_appointments_list
        )
        self.edit_appointment_controller.show()

    def load_appointment_data(self,appointment):
        jalali_date = Dates.convert_to_jalali_format(appointment["jalali_date"])
        time = Numbers.english_to_persian_numbers(appointment["time"])
        description = appointment["description"] or "بدون توضیحات"
        phone_number = Numbers.english_to_persian_numbers(appointment["phone_number"])
        sms_count = Numbers.english_to_persian_numbers(appointment["sms"])

        self.ui.patientFullName_lbl.setText(appointment["patient_name"])
        self.ui.phoneNumber_lbl.setText(phone_number)
        self.ui.serviceName_lbl.setText(appointment["patient_name"])
        self.ui.doctorName_lbl.setText(f"دکتر {appointment["doctor_name"]}")
        self.ui.datetime_lbl.setText(f"{jalali_date} ساعت {time}")
        self.ui.status_lbl.setText(appointment["status"])
        self.ui.description_lbl.setText(description)
        self.ui.smsCount_lbl.setText(f"{sms_count} پیامک یادآوری برای بیمار ارسال شده است ")

    def _refresh_appointment_info_data(self,appointment_id):
       appointment = self._get_appointment_data(appointment_id)
       self.load_appointment_data(appointment)

class AddEditAppointmentController(QDialog):
    load_today_appointments_list = pyqtSignal()
    refresh_appointment_info_data = pyqtSignal(int)
    refresh_user_appointment_list_data = pyqtSignal()

    def __init__(self, patient_id=None, appointment_id=None):
        super(AddEditAppointmentController, self).__init__()
        self.ui = Ui_addEditAppointment_form()
        self.ui.setupUi(self)
        self.setModal(True)

        self.patient_id = patient_id

        self._load_initial_values()

        if appointment_id:
            self.appointment = self._get_appointment_data(appointment_id)
            self.patient_id = self.appointment["patient"]
            self.ui.title_lbl.setText("ویرایش نوبت")
            self.load_appointment_data_into_txtboxes()

        self._connect_buttons()

    def _load_initial_values(self):
        LoadingValues.load_doctors_services_combo_boxes(self.ui)
        LoadingValues.load_current_date_spin_box_values(self.ui)
    
    def _get_appointment_data(self,appointment_id):
        with DatabaseManager() as db:
            try:
                return Appointments.get_appointment_details_by_id(db,appointment_id)
            except Exception as e:
                Messages.show_error_msg(str(e))

    def _connect_buttons(self):
        self.ui.save_btn.clicked.connect(self.save_appointment)
        self.ui.cancel_btn.clicked.connect(self.close)

    def load_appointment_data_into_txtboxes(self):
        appointment = self.appointment
        self.ui.doctor_cmbox.setCurrentText(f"دکتر {appointment["doctor_name"]}")
        self.ui.service_cmbox.setCurrentText(appointment["service_name"])
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

                try:
                    Appointments.update_appointment(db, appointment_data)
                except Exception as e:
                    Messages.show_error_msg(str(e))
                    return
                
                success_msg = "نوبت با موفقیت ویرایش شد."
                self.refresh_appointment_info_data.emit(self.appointment["id"])
            else:
                
                try:
                    Appointments.add_appointment(db, appointment_data)
                except Exception as e:
                    Messages.show_error_msg(str(e))
                    return
                
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

        # Pad both hour and minute with zeros 
        hour_str = str(hour).zfill(2)
        minute_str = str(minute).zfill(2)

        return f"{hour_str}:{minute_str}"

    def _get_gregorian_datetime(self, jalali_date_str, time_str):
        year, month, day = map(int, jalali_date_str.split('-'))
        hour, minute = map(int, time_str.split(':'))
        return jdatetime.datetime(year, month, day, hour, minute).togregorian().strftime('%Y-%m-%d %H:%M')
