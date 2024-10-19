from PyQt5.QtWidgets import QDialog
from ui import Ui_MainWindow, Ui_addEditPatient_form
from models import DatabaseManager, Patients, DatabaseWorker
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from utility import Messages, Numbers, BaseController

class PatientsTabController(BaseController):
    def __init__(self, ui: Ui_MainWindow, appointment_controller):
        self.ui = ui
        self.active_workers = []
        self.load_patients_list()
        self._connect_buttons()
        self.appointment_controller = appointment_controller
        # Validatiors
        identity_code_validator = QRegExpValidator(QRegExp(r"^\d{10}$"))
        self.ui.patientsIdentityCodeSearch_txtbox.setValidator(identity_code_validator)

    def _connect_buttons(self):
        self.ui.addPatient_btn.clicked.connect(self.open_add_patient)
        self.ui.patients_lst.itemDoubleClicked.connect(self.open_patient_file)
        self.ui.refreshPatientsList_btn.clicked.connect(self.load_patients_list)
        self.ui.patientsIdentityCodeSearch_btn.clicked.connect(
            self.search_patient_by_identity_code
        )
        self.ui.patientsLastNameSearch_btn.clicked.connect(
            self.search_patient_by_last_name
        )

    def search_patient_by_identity_code(self):
        entered_identity_code = Numbers.persian_to_english_numbers(
            self.ui.patientsIdentityCodeSearch_txtbox.text()
        )
        self._start_worker(
            Patients.get_by_identity_code,
            [entered_identity_code],
            self.display_searched_patient,
        )

    def display_searched_patient(self, patient):
        self.ui.patients_lst.clear()
        if patient:
            self.add_to_patients_list(patient)

    def search_patient_by_last_name(self):
        entered_last_name = self.ui.patientsLastNameSearch_txtbox.text()
        self._start_worker(
            Patients.get_by_last_name, entered_last_name, self.display_patients_list
        )

    def open_add_patient(self):
        self.add_patient_controller = AddEditPatientController()
        self.add_patient_controller.refresh_patients_list.connect(
            self.load_patients_list
        )
        self.add_patient_controller.show()

    def open_patient_file(self, item):
        patient_id = item.data(1)
        from controllers import PatientFileController

        self.patient_file_controller = PatientFileController(patient_id)
        self.patient_file_controller.refresh_patients_list.connect(
            self.load_patients_list
        )
        self.patient_file_controller.load_today_appointments_list.connect(
            self.appointment_controller.load_today_appointments_list
        )
        self.patient_file_controller.show()

    def load_patients_list(self):
        self._start_worker(Patients.get_all, result_callback=self.display_patients_list)

    def display_patients_list(self, patients):
        self.ui.patients_lst.clear()
        if patients:
            for patient in patients:
                self.add_to_patients_list(patient)

    def add_to_patients_list(self, patient):
        full_name = f"{patient['firstName']} {patient['lastName']}"
        identity_code = Numbers.english_to_persian_numbers(patient["identityCode"])
        phone_number = Numbers.english_to_persian_numbers(patient["phoneNumber"])
        item = QListWidgetItem(
            f"{full_name} | جنسیت: {patient['gender']} | کد ملی: {identity_code} | شماره تلفن: {phone_number}"
        )
        item.setData(1, patient["id"])
        self.ui.patients_lst.addItem(item)


class AddEditPatientController(BaseController, QDialog):
    refresh_patients_list = pyqtSignal()
    refresh_patient_file_data = pyqtSignal()

    def __init__(self, patient_id=None):
        super(AddEditPatientController, self).__init__()
        self.ui = Ui_addEditPatient_form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.active_workers = []
        self.patient_id = patient_id
        self._setup_validators()
        if self.patient_id:
            self.load_patient_data(self.patient_id)
            self.ui.title_lbl.setText("ویرایش اطلاعات")
        self.ui.save_btn.clicked.connect(self.validate_form)
        self.ui.cancel_btn.clicked.connect(self.close)

    def _setup_validators(self):
        identity_code_validator = QRegExpValidator(QRegExp(r"^\d{10}$"))
        self.ui.identityCode_txtbox.setValidator(identity_code_validator)

        phone_number_validator = QRegExpValidator(QRegExp(r"^\d{11}$"))
        self.ui.phoneNumber_txtbox.setValidator(phone_number_validator)

    def load_patient_data(self, patient_id):
        worker = DatabaseWorker(Patients.get_by_id, patient_id)
        worker.result_signal.connect(self.display_patient_data)
        worker.error_signal.connect(self.handle_error)
        self.active_workers.append(worker)
        worker.start()

    def display_patient_data(self, patient):
        # Convert numbers
        identity_code = Numbers.english_to_persian_numbers(patient["identityCode"])
        phoneNumber = Numbers.english_to_persian_numbers(patient["phoneNumber"])

        self.ui.firstName_txtbox.setText(patient["firstName"])
        self.ui.lastName_txtbox.setText(patient["lastName"])
        self.ui.gender_cmbox.setCurrentText(patient["gender"])
        self.ui.age_txtbox.setValue(patient["age"])
        self.ui.phoneNumber_txtbox.setText(phoneNumber)
        self.ui.address_txtbox.setPlainText(patient["address"])
        self.ui.identityCode_txtbox.setText(identity_code)
        self.ui.extraInfo_txtbox.setPlainText(patient["extraInfo"])

    def validate_form(self):
        firstName = self.ui.firstName_txtbox.text().strip()
        lastName = self.ui.lastName_txtbox.text().strip()
        identity_code = Numbers.persian_to_english_numbers(
            self.ui.identityCode_txtbox.text()
        )
        phone_number = self.ui.phoneNumber_txtbox.text().strip()

        txtboxes_text = [firstName, lastName]
        for txtbox_text in txtboxes_text:
            if len(txtbox_text) == 0:
                Messages.show_error_msg("نام و نام خانوادگی را وارد کنید.")
                return

        if len(identity_code) != 10:
            Messages.show_error_msg("کد ملی باید ۱۰ رقم باشد.")
            return

        if len(phone_number) != 11:
            Messages.show_error_msg("شماره تلفن باید ۱۱ رقم باشد.")
            return

        self._check_if_patient_exist(identity_code)

    def save_patient(self):
        identity_code = Numbers.persian_to_english_numbers(
            self.ui.identityCode_txtbox.text()
        )
        phone_number = Numbers.persian_to_english_numbers(
            self.ui.phoneNumber_txtbox.text()
        )

        patient = {
            "firstName": self.ui.firstName_txtbox.text().strip(),
            "lastName": self.ui.lastName_txtbox.text().strip(),
            "gender": self.ui.gender_cmbox.currentText().strip(),
            "age": self.ui.age_txtbox.value(),
            "phoneNumber": phone_number.strip(),
            "address": self.ui.address_txtbox.toPlainText().strip(),
            "identityCode": identity_code.strip(),
            "extraInfo": self.ui.extraInfo_txtbox.toPlainText().strip(),
        }

        if self.patient_id:
            patient["id"] = self.patient_id
            self.update_patient(patient)
        else:
            self.add_patient(patient)

    def add_patient(self, patient):
        self._start_worker(
            Patients.add_patient,
            [patient],
            success_callback=lambda: self.operation_successful(
                "بیمار با موفقیت اضافه شد."
            ),
        )

    def update_patient(self, patient):
        self._start_worker(
            Patients.update_patient,
            [patient],
            success_callback=lambda: self.operation_successful(
                "بیمار با موفقیت ویرایش شد."
            ),
        )

    def operation_successful(self, success_msg):
        Messages.show_success_msg(success_msg)
        self.refresh_patients_list.emit()
        self.refresh_patient_file_data.emit()
        self.close()

    def _check_if_patient_exist(self, identity_code):
        self._start_worker(
            Patients.patient_exist_identity_code,
            [identity_code],
            lambda is_exist: self._handle_patient_existence(is_exist),
        )

    def _handle_patient_existence(self, is_exist):
        if is_exist and self.patient_id is None:
            Messages.show_error_msg("یک بیمار قبلا با این شماره ملی ثبت شده است.")
            return

        self.save_patient()
