from PyQt5.QtWidgets import QDialog
from ui import Ui_addPatient_form,Ui_MainWindow
from models import DatabaseManager,Patients
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from utility import Messages,Numbers


class PatientsTabController:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        self.load_patients_list()

        # Connecting buttons
        self.ui.addPatient_btn.clicked.connect(self.open_add_patient)
        self.ui.patients_lst.itemDoubleClicked.connect(
            self.open_patient_medical_records
        )
        self.ui.refreshPatientsList_btn.clicked.connect(self.load_patients_list)
        self.ui.patientsIdentityCodeSearch_btn.clicked.connect(
            self.search_patient_by_identity_code
        )
        self.ui.patientsLastNameSearch_btn.clicked.connect(
            self.seach_patient_by_last_name
        )

        # Validatiors
        identity_code_validator = QRegExpValidator(QRegExp(r"^\d{10}$"))
        self.ui.patientsIdentityCodeSearch_txtbox.setValidator(identity_code_validator)

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
        self.add_patient_controller = AddPatientController()
        self.add_patient_controller.refresh_patients_list.connect(
            self.load_patients_list
        )
        self.add_patient_controller.show()

    def open_patient_medical_records(self, item):
        patient_id = item.data(1)
        from controllers.MedicalRecordsController import MedicalRecordsInfoController

        self.medical_record_info_controller = MedicalRecordsInfoController(patient_id)
        self.medical_record_info_controller.show()

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


class AddPatientController(QDialog):
    refresh_patients_list = pyqtSignal()

    def __init__(self):
        super(AddPatientController, self).__init__()
        self.ui = Ui_addPatient_form()
        self.ui.setupUi(self)
        self.setModal(True)

        self._setup_validators()

        # Connecting the buttons
        self.ui.save_btn.clicked.connect(self.validate_form)
        self.ui.cancel_btn.clicked.connect(self.close)

    def _setup_validators(self):
        identity_code_validator = QRegExpValidator(QRegExp(r"^\d{10}$"))
        self.ui.identityCode_txtbox.setValidator(identity_code_validator)

        phone_number_validator = QRegExpValidator(QRegExp(r"^\d{11}$"))
        self.ui.phoneNumber_txtbox.setValidator(phone_number_validator)

    def validate_form(self):
        identity_code = self.ui.identityCode_txtbox.text()
        phone_number = self.ui.phoneNumber_txtbox.text()

        if len(identity_code) != 10:
            Messages.show_error_msg("کد ملی باید ۱۰ رقم باشد.")
            return

        if len(phone_number) != 11:
            Messages.show_error_msg("شماره تلفن باید ۱۱ رقم باشد.")
            return

        self.save_patient()

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

        with DatabaseManager() as db:
            Patients.add_patient(db, patient)
            Messages.show_success_msg("بیمار با موفقیت اضافه شد.")
            self.refresh_patients_list.emit()
            self.close()
