from PyQt5.QtWidgets import QDialog
from ui import Ui_MainWindow,Ui_addEditPatient_form
from models import DatabaseManager,Patients
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from utility import Messages,Numbers


class PatientsTabController:
    def __init__(self, ui: Ui_MainWindow,appointment_controller):
        self.ui = ui
        self.load_patients_list()
        self._connect_buttons()
        self.appointment_controller = appointment_controller
        # Validatiors
        identity_code_validator = QRegExpValidator(QRegExp(r"^\d{10}$"))
        self.ui.patientsIdentityCodeSearch_txtbox.setValidator(identity_code_validator)

    def _connect_buttons(self):
        self.ui.addPatient_btn.clicked.connect(self.open_add_patient)
        self.ui.patients_lst.itemDoubleClicked.connect(
            self.open_patient_file
        )
        self.ui.refreshPatientsList_btn.clicked.connect(self.load_patients_list)
        self.ui.patientsIdentityCodeSearch_btn.clicked.connect(
            self.search_patient_by_identity_code
        )
        self.ui.patientsLastNameSearch_btn.clicked.connect(
            self.seach_patient_by_last_name
        )

    def search_patient_by_identity_code(self):
        patient_identity_code = Numbers.persian_to_english_numbers(
            self.ui.patientsIdentityCodeSearch_txtbox.text()
        )
        with DatabaseManager() as db:
            patient = Patients.get_by_identity_code(db, patient_identity_code)
            self.ui.patients_lst.clear()
            if patient:
                self.add_to_patients_list(patient)

    def seach_patient_by_last_name(self):
        patient_last_name = self.ui.patientsLastNameSearch_txtbox.text()
        with DatabaseManager() as db:
            patients = Patients.get_by_last_name(db, patient_last_name)
            self.ui.patients_lst.clear()
            if patients:
                for patient in patients:
                    self.add_to_patients_list(patient)

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
        self.patient_file_controller.refresh_patients_list.connect(self.load_patients_list)
        self.patient_file_controller.load_today_appointments_list.connect(self.appointment_controller.load_today_appointments_list)
        self.patient_file_controller.show()

    def load_patients_list(self):
        self.ui.patients_lst.clear()
        with DatabaseManager() as db:
            all_patients = Patients.get_all(db)
            for patient in all_patients:
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


class AddEditPatientController(QDialog):
    refresh_patients_list = pyqtSignal()
    refresh_patient_file_data = pyqtSignal()

    def __init__(self, patient=None):
        super(AddEditPatientController, self).__init__()
        self.ui = Ui_addEditPatient_form()
        self.ui.setupUi(self)
        self.setModal(True)

        self.patient = patient
        self._setup_validators()

        # Check if it's edit window
        if self.patient:
            self.load_patient_data_into_txtboxes()
            self.ui.title_lbl.setText("ویرایش اطلاعات")

        # Connecting the buttons
        self.ui.save_btn.clicked.connect(self.validate_form)
        self.ui.cancel_btn.clicked.connect(self.close)

    def _setup_validators(self):
        identity_code_validator = QRegExpValidator(QRegExp(r"^\d{10}$"))
        self.ui.identityCode_txtbox.setValidator(identity_code_validator)

        phone_number_validator = QRegExpValidator(QRegExp(r"^\d{11}$"))
        self.ui.phoneNumber_txtbox.setValidator(phone_number_validator)

    def load_patient_data_into_txtboxes(self):
        patient = self.patient

        # Convert numbers
        identity_code = Numbers.english_to_persian_numbers(patient['identityCode'])
        phoneNumber = Numbers.english_to_persian_numbers(patient['phoneNumber'])

        self.ui.firstName_txtbox.setText(patient['firstName'])
        self.ui.lastName_txtbox.setText(patient['lastName'])
        self.ui.gender_cmbox.setCurrentText(patient['gender'])
        self.ui.age_txtbox.setValue(patient['age'])
        self.ui.phoneNumber_txtbox.setText(phoneNumber)
        self.ui.address_txtbox.setPlainText(patient['address'])
        self.ui.identityCode_txtbox.setText(identity_code)
        self.ui.extraInfo_txtbox.setPlainText(patient['extraInfo'])

    def validate_form(self):
        firstName = self.ui.firstName_txtbox.text().strip()
        lastName = self.ui.lastName_txtbox.text().strip()
        identity_code = self.ui.identityCode_txtbox.text().strip()
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

        if self.patient:
            self.update_patient()
        else:
            self.save_patient()

    def save_patient(self):
        identity_code = Numbers.persian_to_english_numbers(self.ui.identityCode_txtbox.text())
        phone_number = Numbers.persian_to_english_numbers(self.ui.phoneNumber_txtbox.text())

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

        with DatabaseManager() as db:
            Patients.add_patient(db, patient)
            Messages.show_success_msg("بیمار با موفقیت اضافه شد.")
            self.refresh_patients_list.emit()
            self.close()

    def update_patient(self):
        identity_code = Numbers.persian_to_english_numbers(self.ui.identityCode_txtbox.text())
        phone_number = Numbers.persian_to_english_numbers(self.ui.phoneNumber_txtbox.text())

        patient = {
            "id": self.patient["id"],
            "firstName": self.ui.firstName_txtbox.text().strip(),
            "lastName": self.ui.lastName_txtbox.text().strip(),
            "gender": self.ui.gender_cmbox.currentText().strip(),
            "age": self.ui.age_txtbox.value(),
            "phoneNumber": phone_number.strip(),
            "address": self.ui.address_txtbox.toPlainText().strip(),
            "identityCode": identity_code.strip(),
            "extraInfo": self.ui.extraInfo_txtbox.toPlainText().strip(),
        }

        with DatabaseManager() as db:
            Patients.update_patient(db, patient)
            Messages.show_success_msg("بیمار با موفقیت ویرایش شد.")
            self.refresh_patients_list.emit()
            self.refresh_patient_file_data.emit()
            self.close()
