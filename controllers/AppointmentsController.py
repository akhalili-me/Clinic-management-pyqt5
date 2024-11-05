from PyQt5.QtWidgets import QDialog
from ui import get_ui_class
from models import (
    Appointments,
    delete_appointment_add_medical_record_transaction,
    Patients,
)
from PyQt5.QtCore import pyqtSignal
from utility import (
    Dates,
    Numbers,
    Messages,
    SpecialDays,
    SMSWorker,
    BaseController,
    Validators,
    GroupSMSWorker,
    LoadComboBox,
    LoadSpinBox
)
from PyQt5.QtWidgets import QListWidgetItem
import jdatetime


class AppointmentsTabController(BaseController):
    def __init__(self, ui, dispatcher):
        super().__init__()
        self.ui = ui
        self.active_workers = []
        self.dispatcher = dispatcher
        LoadSpinBox.set_current_date_into_date_spin_boxes(self.ui)
        self.load_today_appointments_list()
        self._connect_dispatcher_methods()
        self._connect_buttons()

    def _connect_dispatcher_methods(self):
        self.dispatcher.refresh_appointments_list.connect(
            self.load_today_appointments_list
        )

    def _connect_buttons(self):
        self.ui.appointments_lst.itemDoubleClicked.connect(self.open_appointment_info)
        self.ui.AppointmentSearchByDate_btn.clicked.connect(self.search_appointments_by_date)
        self.ui.appointmentSearchByDay_btn.clicked.connect(self.search_appointments_by_day_select)
        self.ui.sendToAllSMSByDays_btn.clicked.connect(self.handle_group_reminder_sms_send_by_date)
        self.ui.autoSMSSend_btn.clicked.connect(self.handle_auto_reminder_sms_send)
        self.ui.addAppointment_btn.clicked.connect(
            self.open_add_appointment_with_patient_search
        )

    def open_add_appointment_with_patient_search(self):
        self.add_appointment_patient_search_controller = AddAppointmentWithPatientSearchController(self.dispatcher)
        self.add_appointment_patient_search_controller.load_today_appointments_list.connect(
            self.load_today_appointments_list
        )
        self.add_appointment_patient_search_controller.show()

    def open_appointment_info(self, item):
        appointment_id = item.data(1)
        self.appointment_info_controller = AppointmentInfoController(appointment_id,self.dispatcher)
        self.appointment_info_controller.show()

    def handle_group_reminder_sms_send_by_date(self):
        if not self._confirm_send():
            return

        days_ahead_mapping = {
            SpecialDays.TODAY: 0,
            SpecialDays.TOOMMORROW: 1,
            SpecialDays.TWO_DAYS_LATER: 2,
            SpecialDays.THREE_DAYS_LATER: 3,
            SpecialDays.FOUR_DAYS_LATER: 4,
        }
        selected_day = self.ui.sendToAllSMSByDays_cmbox.currentText().strip()
        days_ahead = days_ahead_mapping.get(SpecialDays(selected_day), None)

        if days_ahead is not None:
            selected_date = Dates.get_future_date(days_ahead)
            self._start_worker(
                Appointments.get_appointments_for_send_sms,
                [selected_date],
                self.group_reminder_sms_send,
            )

    def group_reminder_sms_send(self, appointments):
        self._disable_button(self.ui.sendToAllSMSByDays_btn)
        self._start_group_worker(appointments, self.ui.sendToAllSMSByDays_btn)

    def handle_auto_reminder_sms_send(self):
        if not self._confirm_send():
            return

        start_date = Dates.get_today_date_greg()
        end_date = Dates.get_future_date_greg(3)
        self._start_worker(
            Appointments.get_appointments_for_auto_send_sms,
            [start_date, end_date],
            self.send_auto_reminder_sms,
        )

    def send_auto_reminder_sms(self, appointments):
        self._disable_button(self.ui.autoSMSSend_btn)
        self._start_group_worker(appointments, self.ui.autoSMSSend_btn)

    def _start_group_worker(self, appointments, button):
        group_worker = GroupSMSWorker(appointments)
        group_worker.update_sms_field_signal.connect(self._update_appointment_sms_field)
        group_worker.summary_signal.connect(lambda success, fail: self._sms_send_finished(success, fail, button))
        self.active_workers.append(group_worker)
        group_worker.finished.connect(lambda: self.active_workers.remove(group_worker))
        group_worker.start()

    def _sms_send_finished(self, success_count, failure_count, button):
        button.setEnabled(True)
        total_count = success_count + failure_count
        progress_msg = f"{success_count} از {total_count} پیامک یادآوری با موفقیت ارسال شد."
        Messages.show_info_msg(progress_msg)

    def _update_appointment_sms_field(self, appointment):
        self._start_worker(Appointments.update_appointment, [appointment], show_error=False)

    def search_appointments_by_day_select(self):
        day_mapping = {
            SpecialDays.TODAY.value: 0,
            SpecialDays.TOOMMORROW.value: 1,
            SpecialDays.TWO_DAYS_LATER.value: 2,
            SpecialDays.THREE_DAYS_LATER.value: 3,
            SpecialDays.FOUR_DAYS_LATER.value: 4,
        }
        selected_day = self.ui.appointmentSearchDaySelect_cmbox.currentText().strip()
        days_ahead = day_mapping.get(selected_day)

        if days_ahead is not None:
            if days_ahead == 0:
                self.load_today_appointments_list()
            else:
                self._load_future_date_appointments(days_ahead)

    def search_appointments_by_date(self):
        year, month, day = self.ui.year_spnbox.value(), self.ui.month_spnbox.value(), self.ui.day_spnbox.value()
        date_str = jdatetime.date(year, month, day).strftime("%Y-%m-%d")
        self._load_appointment_list_by_date(date_str)

    def load_today_appointments_list(self):
        today_date = jdatetime.date.today().strftime("%Y-%m-%d")
        self._load_appointment_list_by_date(today_date)

    def _load_future_date_appointments(self, days_ahead):
        date = Dates.get_future_date(days_ahead)
        self._load_appointment_list_by_date(date)

    def _load_appointment_list_by_date(self, date):
        selected_status = self.ui.appointmentSearchStatus_cmbox.currentText().strip()
        status_mapping = {
            "نوبت‌های فعال": "فعال",
            "نوبت‌های غیرفعال": "غیرفعال"
        }
        status = status_mapping.get(selected_status)
        self._start_worker(
            Appointments.get_by_jalali_date,
            [date, status],
            self.display_appointments_list,
        )
        LoadSpinBox.load_date_into_date_spinboxes(self.ui, date)

    def display_appointments_list(self, appointments):
        self.ui.appointments_lst.clear()
        for appointment in appointments:
            date = Dates.convert_to_jalali_format(appointment["jalali_date"])
            time = Numbers.english_to_persian_numbers(appointment["time"])
            phone_number = Numbers.english_to_persian_numbers(appointment["phone_number"])
            description = appointment.get("description", "بدون توضیحات")
            item_txt = f"{appointment['patient_name']} | {phone_number} | {appointment['service_name']} | دکتر {appointment['doctor_name']} | {appointment['status']} | {date} | ساعت {time}"
            item = QListWidgetItem(item_txt)
            item.setData(1, appointment["id"])
            self.ui.appointments_lst.addItem(item)

    def _confirm_send(self):
        msg_box, yes_button = Messages.show_confirm_msg()
        return msg_box.clickedButton() == yes_button

    def _disable_button(self, button):
        button.setDisabled(True)

class AppointmentInfoController(BaseController, QDialog):
    load_user_appointment_list = pyqtSignal()
    load_user_medical_records_list = pyqtSignal()

    def __init__(self, appointment_id,dispatcher ):
        super(AppointmentInfoController, self).__init__()
        self.ui = get_ui_class("iAppointment")()
        self.ui.setupUi(self)
        self.setModal(True)
        self.active_workers = []
        self.dispatcher = dispatcher
        self.appointment_id = appointment_id
        self.appointment = None
        self.load_appointment_data()
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.deleteAppointment_btn.clicked.connect(self.delete_appointment)
        self.ui.sendReminderSMS_btn.clicked.connect(self.send_reminder_sms)
        self.ui.editAppointment_btn.clicked.connect(self.open_edit_appointment)
        self.ui.addAppointmentToMedicalRecords_btn.clicked.connect(
            self.add_appointment_to_medical_records
        )

    def add_appointment_to_medical_records(self):
        msg_box, yes_button = Messages.show_confirm_msg()
        if msg_box.clickedButton() != yes_button:
            msg_box.close()
            return

        appointment = self.appointment

        greg_date = appointment["greg_datetime"].split(" ")[0]
        medical_record_data = {
            "jalali_date": appointment["jalali_date"],
            "doctor": appointment["doctor"],
            "service": appointment["service"],
            "price": appointment["service_price"],
            "description": appointment["description"],
            "patient": appointment["patient"],
            "greg_date": greg_date,
        }

        self._start_worker(
            delete_appointment_add_medical_record_transaction,
            [self.appointment_id, medical_record_data],
            success_callback=lambda: self.operation_successful(
                "نوبت با موفقیت به پرونده خدمات ارائه شده بیمار اضافه شد.", True
            ),
        )

    def send_reminder_sms(self):
        if not self._confirm_send():
            return
        self.ui.sendReminderSMS_btn.setDisabled(True)
        self._start_sms_worker(self.appointment)

    def _confirm_send(self):
        msg_box, yes_button = Messages.show_confirm_msg()
        if msg_box.clickedButton() != yes_button:
            msg_box.close()
            return False
        return True

    def _start_sms_worker(self, sms_params):
        sms_worker = SMSWorker(sms_params)
        sms_worker.success_signal.connect(self._on_sms_send_success)
        sms_worker.error_signal.connect(self.handle_error)
        sms_worker.finished.connect(lambda: self._sms_worker_finished(sms_worker))
        self.active_workers.append(sms_worker)
        sms_worker.start()

    def _sms_worker_finished(self,sms_worker):
        self.active_workers.remove(sms_worker)
        self.ui.sendReminderSMS_btn.setEnabled(True)

    def _on_sms_send_success(self):
        self.appointment["sms"] += 1  # Update local state
        update_data = {"id": self.appointment["id"], "sms": self.appointment["sms"]}
        self._start_worker(
            Appointments.update_appointment,
            [update_data],
            success_callback=self._on_appointment_sms_update_success,
        )
        Messages.show_success_msg("پیامک یادآوری نوبت با موفقیت ارسال شد.")

    def _on_appointment_sms_update_success(self):
        self.load_appointment_data()

    def delete_appointment(self):
        msg_box, yes_button = Messages.show_confirm_delete_msg()
        if msg_box.clickedButton() != yes_button:
            msg_box.close()
            return

        self._start_worker(
            Appointments.delete_appointment,
            [self.appointment_id],
            success_callback=lambda: self.operation_successful(
                "نوبت با موفقیت حذف شد."
            ),
        )

    def open_edit_appointment(self):
        self.edit_appointment_controller = AddEditAppointmentController(
            self.dispatcher, appointment_id=self.appointment_id
        )
        self.edit_appointment_controller.refresh_appointment_info_data.connect(
            self.load_appointment_data
        )
        self.edit_appointment_controller.refresh_user_appointment_list_data.connect(
            self.load_user_appointment_list
        )

        self.edit_appointment_controller.load_today_appointments_list.connect(
            self.dispatcher.refresh_appointments_list
        )
        self.edit_appointment_controller.show()

    def load_appointment_data(self):
        self._start_worker(
            Appointments.get_appointment_details_by_id,
            [self.appointment_id],
            self.handle_appointment_data,
        )

    def handle_appointment_data(self, appointment):
        self.appointment = appointment
        self.display_appointment_info(appointment)

    def display_appointment_info(self, appointment):
        jalali_date = Dates.convert_to_jalali_format(appointment["jalali_date"])
        time = Numbers.english_to_persian_numbers(appointment["time"])
        description = appointment["description"] or "بدون توضیحات"
        phone_number = Numbers.english_to_persian_numbers(appointment["phone_number"])
        sms_count = Numbers.english_to_persian_numbers(appointment["sms"])

        self.ui.patientFullName_lbl.setText(appointment["patient_name"])
        self.ui.phoneNumber_lbl.setText(phone_number)
        self.ui.serviceName_lbl.setText(appointment["service_name"])
        self.ui.doctorName_lbl.setText(f"دکتر {appointment["doctor_name"]}")
        self.ui.datetime_lbl.setText(f"{jalali_date} ساعت {time}")
        self.ui.status_lbl.setText(appointment["status"])
        self.ui.description_lbl.setText(description)
        self.ui.smsCount_lbl.setText(
            f"{sms_count} پیامک یادآوری برای بیمار ارسال شده است "
        )

    def operation_successful(self, success_msg, medical_record_refresh=False):
        Messages.show_success_msg(success_msg)
        self.dispatcher.refresh_appointments_list.emit()
        self.load_user_appointment_list.emit()
        self.dispatcher.refresh_main_tab_reports.emit()
        if medical_record_refresh:
            self.load_user_medical_records_list.emit()
        self.close()

class AddEditAppointmentController(BaseController, QDialog):
    load_today_appointments_list = pyqtSignal()
    refresh_appointment_info_data = pyqtSignal()
    refresh_user_appointment_list_data = pyqtSignal()

    def __init__(
        self,
        dispatcher,
        patient_id=None,
        appointment_id=None,
    ):
        super(AddEditAppointmentController, self).__init__()
        self.ui = get_ui_class("aeAppointment")()
        self.ui.setupUi(self)
        self.setModal(True)
        self.active_workers = []
        self.dispatcher = dispatcher
        self.patient_id = patient_id
        self.appointment_id = appointment_id
        self._initialize_ui()
        if appointment_id:
            self.load_appointment_data()
            self.ui.save_btn.setText("ویرایش")
        self._connect_buttons()

    def _initialize_ui(self):
        self._setup_validators()
        self.combo_box_loader = LoadComboBox(self.ui, self._start_worker)
        self.combo_box_loader.load_doctors_services_combo_boxes()
        LoadSpinBox.set_current_date_into_date_spin_boxes(self.ui)

    def _setup_validators(self):
        self.ui.description_txtbox.textChanged.connect(
            lambda: Validators.limit_text_edit(self.ui.description_txtbox)
        )

    def _connect_buttons(self):
        self.ui.save_btn.clicked.connect(self.validate_appointment)
        self.ui.cancel_btn.clicked.connect(self.close)

    def load_appointment_data(self):
        self._start_worker(
            Appointments.get_appointment_details_by_id,
            [self.appointment_id],
            result_callback=self.display_appointment_data,
        )

    def display_appointment_data(self, appointment):
        self.ui.doctor_cmbox.setCurrentText(f"دکتر {appointment["doctor_name"]}")
        self.ui.service_cmbox.setCurrentText(appointment["service_name"])
        self.ui.status_cmbox.setCurrentText(appointment["status"])
        self.ui.description_txtbox.setText(appointment["description"])
        LoadSpinBox.load_date_into_date_spinboxes(self.ui, appointment["jalali_date"])
        LoadSpinBox.load_time_into_time_spinboxes(self.ui, appointment["time"])

    def validate_appointment(self):
        try:
            self._get_jalali_date()
        except Exception as e:
            warning_message = f"""
            تاریخ انتخاب شده وجود ندارد. 
            {str(e)}
            """
            Messages.show_warning_msg(warning_message)
            return
        self.save_appointment()

    def save_appointment(self):
        jalali_date_str = self._get_jalali_date()
        time_str = self._get_time_str()
        greg_datetime = self._get_gregorian_datetime(jalali_date_str, time_str)

        appointment_data = {
            "status": self.ui.status_cmbox.currentText().strip(),
            "jalali_date": jalali_date_str,
            "greg_datetime": greg_datetime,
            "time": time_str,
            "doctor": self.ui.doctor_cmbox.currentData(),
            "service": self.ui.service_cmbox.currentData(),
            "description": self.ui.description_txtbox.toPlainText().strip(),
        }

        if self.appointment_id:
            appointment_data["id"] = self.appointment_id
            self.update_appointment(appointment_data)
        else:
            appointment_data["patient"] = self.patient_id
            self.add_appointment(appointment_data)

    def add_appointment(self, appointment):
        self._start_worker(
            Appointments.add_appointment,
            [appointment],
            success_callback=lambda: self.operation_successful(
                "نوبت با موفقیت اضافه شد."
            ),
        )

    def update_appointment(self, appointment):
        self._start_worker(
            Appointments.update_appointment,
            [appointment],
            success_callback=lambda: self.operation_successful(
                "نوبت با موفقیت ویرایش شد."
            ),
        )

    def operation_successful(self, success_msg):
        Messages.show_success_msg(success_msg)
        self.load_today_appointments_list.emit()
        self.refresh_user_appointment_list_data.emit()
        self.refresh_appointment_info_data.emit()
        self.dispatcher.refresh_main_tab_reports.emit()
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
        year, month, day = map(int, jalali_date_str.split("-"))
        hour, minute = map(int, time_str.split(":"))
        return (
            jdatetime.datetime(year, month, day, hour, minute)
            .togregorian()
            .strftime("%Y-%m-%d %H:%M")
        )

class AddAppointmentWithPatientSearchController(BaseController, QDialog):
    load_today_appointments_list = pyqtSignal()

    def __init__(self,dispatcher):
        super(AddAppointmentWithPatientSearchController, self).__init__()
        self.ui = get_ui_class("aAppointmentPatientSearch")()
        self.ui.setupUi(self)
        self.setModal(True)
        self.dispatcher = dispatcher
        self.active_workers = []
        self.selected_patient_id = None
        self._initialize_ui()
        self._connect_buttons()

    def _initialize_ui(self):
        self._setup_validators()
        self.combo_box_loader = LoadComboBox(self.ui,self._start_worker)
        self.combo_box_loader.load_doctors_services_combo_boxes()
        LoadSpinBox.set_current_date_into_date_spin_boxes(self.ui)
        self.ui.searchedPatient_list.hide()
        self.ui.patientLastName_txtbox.textChanged.connect(self.on_patient_last_name_text_changed)
        self.ui.searchedPatient_list.itemDoubleClicked.connect(self.on_patient_selected)
        self.ui.undoSelectedPatient_btn.setDisabled(True)

    def _setup_validators(self):
        self.ui.description_txtbox.textChanged.connect(
            lambda: Validators.limit_text_edit(self.ui.description_txtbox)
        )

    def _connect_buttons(self):
        self.ui.save_btn.clicked.connect(self.validate_appointment)
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.undoSelectedPatient_btn.clicked.connect(self.undo_selected_patient)

    def undo_selected_patient(self):
        msg_box, yes_button = Messages.show_confirm_msg()
        if msg_box.clickedButton() != yes_button:
            msg_box.close()
            return
        self.selected_patient_id = None
        self.ui.patientLastName_txtbox.setText("")
        self.ui.patientLastName_txtbox.setEnabled(True)
        self.ui.undoSelectedPatient_btn.setDisabled(True)

    def on_patient_last_name_text_changed(self, text):
        if len(text.strip()) >= 3 and self.ui.patientLastName_txtbox.isEnabled():
            self._start_worker(
                Patients.get_by_last_name, [text.strip()], self.populate_searched_patient_list
            )

    def populate_searched_patient_list(self, patients):
        self.ui.searchedPatient_list.clear()
        for patient in patients:
            identity_code = Numbers.english_to_persian_numbers(patient["identityCode"])
            item_txt = f"{patient["firstName"]} {patient["lastName"]} - {identity_code}"
            patient_item = QListWidgetItem(item_txt)
            patient_item.setData(1,patient["id"])
            self.ui.searchedPatient_list.addItem(patient_item)
        self.ui.searchedPatient_list.show()

    def on_patient_selected(self,item):
        self.selected_patient_id = item.data(1)
        patient_full_name = item.text()
        self.ui.searchedPatient_list.hide()
        self.ui.patientLastName_txtbox.setDisabled(True)
        self.ui.patientLastName_txtbox.setText(patient_full_name)
        self.ui.undoSelectedPatient_btn.setEnabled(True)

    def validate_appointment(self):
        if not self.selected_patient_id:
            Messages.show_warning_msg("هیچ بیماری برای نوبت دهی انتخاب نشده است.")
            return

        try:
            self._get_jalali_date()
        except Exception as e:
            warning_message = f"""
            تاریخ انتخاب شده وجود ندارد. 
            {str(e)}
            """
            Messages.show_warning_msg(warning_message)
            return

        self.save_appointment()

    def save_appointment(self):
        jalali_date_str = self._get_jalali_date()
        time_str = self._get_time_str()
        greg_datetime = self._get_gregorian_datetime(jalali_date_str, time_str)

        appointment_data = {
            "status": self.ui.status_cmbox.currentText().strip(),
            "jalali_date": jalali_date_str,
            "greg_datetime": greg_datetime,
            "time": time_str,
            "doctor": self.ui.doctor_cmbox.currentData(),
            "service": self.ui.service_cmbox.currentData(),
            "description": self.ui.description_txtbox.toPlainText().strip(),
            "patient": self.selected_patient_id
        }

        self.add_appointment(appointment_data)

    def add_appointment(self, appointment):
        self._start_worker(
            Appointments.add_appointment,
            [appointment],
            success_callback=lambda: self.operation_successful(
                "نوبت با موفقیت اضافه شد."
            ),
        )

    def operation_successful(self, success_msg):
        Messages.show_success_msg(success_msg)
        self.load_today_appointments_list.emit()
        self.dispatcher.refresh_main_tab_reports.emit()
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
        year, month, day = map(int, jalali_date_str.split("-"))
        hour, minute = map(int, time_str.split(":"))
        return (
            jdatetime.datetime(year, month, day, hour, minute)
            .togregorian()
            .strftime("%Y-%m-%d %H:%M")
        )
