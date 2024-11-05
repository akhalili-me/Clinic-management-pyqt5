from PyQt5.QtWidgets import QDialog,QWidget
from ui import get_ui_class
from models import  Patients
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from utility import (
    Messages,
    Numbers,
    BaseController,
    Validators,
    create_patient_directory_if_not_exist,get_patient_signature_image_path
    ,Images
)
import os
from PyQt5.QtGui import QPixmap

class PatientsTabController(BaseController):
    def __init__(self, ui, dispatcher):
        self.ui = ui
        self.active_workers = []
        self.dispatcher = dispatcher
        self.load_patients_list()
        self._setup_validators()
        self._connect_buttons()

    def _setup_validators(self):
        txtbox_only_number = QRegExpValidator(QRegExp(r"^\d{10}$"))
        self.ui.patientsIdentityCodeSearch_txtbox.setValidator(txtbox_only_number)
        self.ui.patientSearchFileNumber_txtbox.setValidator(txtbox_only_number)

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
        self.ui.patientSearchByFileNumber_btn.clicked.connect(self.search_patient_by_file_number)

    def search_patient_by_file_number(self):
        searched_file_number = Numbers.persian_to_english_numbers(
            self.ui.patientSearchFileNumber_txtbox.text() or ""
        )
        if searched_file_number:
            self._start_worker(
                Patients.get_by_id, [searched_file_number], self.display_searched_patient
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
            Patients.get_by_last_name, [entered_last_name], self.display_patients_list
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

        self.patient_file_controller = PatientFileController(
            patient_id, self.dispatcher
        )
        self.patient_file_controller.refresh_patients_list.connect(
            self.load_patients_list
        )
        self.patient_file_controller.show()

    def load_patients_list(self):
        self._start_worker(Patients.get_all, result_callback=self.display_patients_list)
        self.clear_search_text_boxes()

    def clear_search_text_boxes(self):
        self.ui.patientSearchFileNumber_txtbox.setText("")
        self.ui.patientsIdentityCodeSearch_txtbox.setText("")
        self.ui.patientsLastNameSearch_txtbox.setText("")

    def display_patients_list(self, patients):
        self.ui.patients_lst.clear()
        if patients:
            for patient in patients:
                self.add_to_patients_list(patient)

    def add_to_patients_list(self, patient):
        full_name = f"{patient['firstName']} {patient['lastName']}"
        identity_code = Numbers.english_to_persian_numbers(patient["identityCode"])
        phone_number = Numbers.english_to_persian_numbers(patient["phoneNumber"])
        file_number = Numbers.english_to_persian_numbers(patient["id"])
        age = Numbers.english_to_persian_numbers(patient["age"])
        item = QListWidgetItem(
            f"شماره پرونده: {file_number} | {full_name} | سن: {age} | کد ملی: {identity_code} | شماره تلفن: {phone_number}"
        )
        item.setData(1, patient["id"])
        self.ui.patients_lst.addItem(item)

class AddEditPatientController(BaseController, QDialog):
    refresh_patients_list = pyqtSignal()
    refresh_patient_file_data = pyqtSignal()

    def __init__(self, patient_id=None):
        super(AddEditPatientController, self).__init__()
        self.ui = get_ui_class("aePatient")()
        self.ui.setupUi(self)
        self.setModal(True)
        self.active_workers = []
        self.patient_id = patient_id
        self.patient_identity_code = None
        self.initilize_ui()

    def _connect_buttons(self):
        self.ui.save_btn.clicked.connect(self.validate_form)
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.clearSignature_btn.clicked.connect(self.clear_signature)
        self.ui.editSignature_btn.clicked.connect(self.handle_edit_signature)

    def initilize_ui(self):
        self.ui.editSignature_btn.hide()
        self._setup_validators()
        self._handle_edit_mode()
        self._connect_buttons()

    def _handle_edit_mode(self):
        if self.patient_id:
            self.load_patient_data()
            self.ui.save_btn.setText("ویرایش")
            if os.path.exists(get_patient_signature_image_path(self.patient_id)):
                self.ui.editSignature_btn.show()
                self.ui.patientSignature_widget.setDisabled(True)
                self.ui.clearSignature_btn.hide()

    def handle_edit_signature(self):
        msg_box, yes_button = Messages.show_confirm_delete_msg()
        if msg_box.clickedButton() != yes_button:
            msg_box.close()
            return

        signature_path = get_patient_signature_image_path(self.patient_id)
        try:
            Images.delete_image(signature_path)
        except Exception as e:
            error_msg = f"""
                حذف امضاء بیمار با خطا مواجه شده است. 
                f{str(e)}
            """
            Messages.show_error_msg(error_msg)
            return
        self.clear_signature()
        self.ui.patientSignature_widget.setDisabled(False)
        self.ui.clearSignature_btn.show()
        self.ui.editSignature_btn.hide()
        Messages.show_success_msg("امضاء بیمار با موفقیت حذف شد. لطفا امضاء جدیدی ثبت نمایید.")

    def clear_signature(self):
        self.ui.patientSignature_widget.clear()

    def _setup_validators(self):
        identity_code_validator = QRegExpValidator(QRegExp(r"^\d{10}$"))
        self.ui.identityCode_txtbox.setValidator(identity_code_validator)

        phone_number_validator = QRegExpValidator(QRegExp(r"^\d{11}$"))
        self.ui.phoneNumber_txtbox.setValidator(phone_number_validator)

        self.ui.extraInfo_txtbox.textChanged.connect(
            lambda: Validators.limit_text_edit(self.ui.extraInfo_txtbox)
        )
        self.ui.address_txtbox.textChanged.connect(
            lambda: Validators.limit_text_edit(self.ui.address_txtbox)
        )

        self.ui.firstName_txtbox.setMaxLength(50)
        self.ui.lastName_txtbox.setMaxLength(50)
        self.ui.job_txtbox.setMaxLength(50)
        self.ui.allergyOtherItems_txtbox.setMaxLength(50)
        self.ui.disaseOtherItems_txtbox.setMaxLength(50)
        self.ui.medicationsOtherItems_txtbox.setMaxLength(50)
        self.ui.specialCondition_txtbox.setMaxLength(50)

    def load_patient_data(self):
        self._start_worker(
            Patients.get_by_id, [self.patient_id], self.handle_patient_data
        )

    def handle_patient_data(self,patient):
        self.display_patient_data(patient)
        self.patient_identity_code = patient["identityCode"]

    def display_patient_data(self, patient):
        # Convert numbers
        identity_code = Numbers.english_to_persian_numbers(patient["identityCode"])
        phoneNumber = Numbers.english_to_persian_numbers(patient["phoneNumber"])

        self.ui.firstName_txtbox.setText(patient["firstName"])
        self.ui.lastName_txtbox.setText(patient["lastName"])
        self.ui.job_txtbox.setText(patient["job"])
        self.ui.age_txtbox.setValue(patient["age"])
        self.ui.phoneNumber_txtbox.setText(phoneNumber)
        self.ui.address_txtbox.setPlainText(patient["address"])
        self.ui.identityCode_txtbox.setText(identity_code)
        self.ui.extraInfo_txtbox.setPlainText(patient["extraInfo"])
        self.ui.specialCondition_txtbox.setText(patient["specialCondition"])
        self.ui.pregnant_cmbox.setCurrentText(patient["pregnant"])
        self.ui.marialStatus_cmbox.setCurrentText(patient["maritalStatus"])

        self._set_patient_allergies(patient["allergy"])
        self._set_patient_diseases(patient["disease"])
        self._set_patient_medications(patient["medication"])
        self._set_patient_signature()

    def _set_patient_signature(self):
        signature_path = get_patient_signature_image_path(self.patient_id)
        if os.path.exists(signature_path):
            signature_pixmap = QPixmap(signature_path)
            self.ui.patientSignature_widget.image = signature_pixmap
            self.ui.patientSignature_widget.update()

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

        if self.ui.patientSignature_widget.is_blank():
            Messages.show_warning_msg("امضای بیمار گرفته نشده است.")

        self._check_if_patient_exist(identity_code)

    def save_patient(self):
        patient = self._collect_patient_data()

        if self.patient_id:
            patient["id"] = self.patient_id
            self.update_patient(patient)
            self.save_patient_signature_image(self.patient_id)
        else:
            self.add_patient(patient)

    def add_patient(self, patient):
        self._start_worker(
            Patients.add_patient,
            [patient],
            result_callback=self.handle_patient_added_success,
            success_callback=lambda: self.operation_successful(
                "بیمار با موفقیت اضافه شد."
            ),
        )

    def handle_patient_added_success(self,patient_id):
        create_patient_directory_if_not_exist(str(patient_id))
        self.save_patient_signature_image(patient_id)

    def save_patient_signature_image(self,patient_id):
        if not self.ui.patientSignature_widget.is_blank():
            signature_path = get_patient_signature_image_path(patient_id)
            signature_image = self.ui.patientSignature_widget.get_signature_image()
            signature_image.save(signature_path)

    def update_patient(self, patient):
        self._start_worker(
            Patients.update_patient,
            [patient],
            success_callback=self.handle_patient_update_success,
        )

    def handle_patient_update_success(self):
        self.operation_successful("بیمار با موفقیت ویرایش شد.")
        self.save_patient_signature_image(self.patient_id)

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
        inserted_identity_code = Numbers.persian_to_english_numbers(
            self.ui.identityCode_txtbox.text().strip()
        )

        if is_exist and inserted_identity_code != self.patient_identity_code:
            Messages.show_error_msg("یک بیمار قبلا با این شماره ملی ثبت شده است.")
            return

        self.save_patient()

    def _collect_patient_data(self):
        identity_code = Numbers.persian_to_english_numbers(
            self.ui.identityCode_txtbox.text()
        )
        phone_number = Numbers.persian_to_english_numbers(
            self.ui.phoneNumber_txtbox.text()
        )

        allergy = self._get_patient_allergies()
        disease = self._get_patient_diseases()
        medicaitons = self._get_patient_medications()

        patient = {
            "firstName": self.ui.firstName_txtbox.text().strip(),
            "lastName": self.ui.lastName_txtbox.text().strip(),
            "job": self.ui.job_txtbox.text().strip(),
            "age": self.ui.age_txtbox.value(),
            "phoneNumber": phone_number.strip(),
            "maritalStatus": self.ui.marialStatus_cmbox.currentText().strip(),
            "address": self.ui.address_txtbox.toPlainText().strip(),
            "identityCode": identity_code.strip(),
            "extraInfo": self.ui.extraInfo_txtbox.toPlainText().strip(),
            "specialCondition": self.ui.specialCondition_txtbox.text().strip(),
            "pregnant": self.ui.pregnant_cmbox.currentText().strip(),
            "allergy": allergy,
            "disease": disease,
            "medication": medicaitons,
        }

        return patient

    def _get_patient_allergies(self):
        allergies = [
            (
                "antibioticsAllergy"
                if self.ui.antibioticsAllergy_chkbox.isChecked()
                else ""
            ),
            "localAnesthetic" if self.ui.localAnesthetic_chkbox.isChecked() else "",
            "painkiller" if self.ui.painkiller_chkbox.isChecked() else "",
            "specialFood" if self.ui.specialFood_chkbox.isChecked() else "",
            self.ui.allergyOtherItems_txtbox.text().strip(),
        ]

        return "-".join(filter(None, allergies))

    def _get_patient_diseases(self):
        diseases = [
            "gastrointestinal" if self.ui.gastrointestinal_chkbox.isChecked() else "",
            "thyroidDisease" if self.ui.thyroidDisease_chkbox.isChecked() else "",
            "MS" if self.ui.MS_chkbox.isChecked() else "",
            "respiratory" if self.ui.respiratory_chkbox.isChecked() else "",
            "blood" if self.ui.blood_chkbox.isChecked() else "",
            "herpes" if self.ui.herpes_chkbox.isChecked() else "",
            "hepatitis" if self.ui.hepatitis_chkbox.isChecked() else "",
            "cancer" if self.ui.cancer_chkbox.isChecked() else "",
            "kidney" if self.ui.kidney_chkbox.isChecked() else "",
            "hormone" if self.ui.hormone_chkbox.isChecked() else "",
            self.ui.disaseOtherItems_txtbox.text().strip(),
        ]
        return "-".join(filter(None, diseases))

    def _get_patient_medications(self):
        mediciations = [
            "contraceptive" if self.ui.contraceptive_chkbox.isChecked() else "",
            "aspirin" if self.ui.aspirin_chkbox.isChecked() else "",
            "roaccutane" if self.ui.roaccutane_chkbox.isChecked() else "",
            "sedative" if self.ui.sedative_chkbox.isChecked() else "",
            "heart" if self.ui.heart_chkbox.isChecked() else "",
            "anticoagulants" if self.ui.anticoagulants_chkbox.isChecked() else "",
            "insulin" if self.ui.insulin_chkbox.isChecked() else "",
            "thyroidMedicine" if self.ui.thyroidMedicine_chkbox.isChecked() else "",
            (
                "antibioticsMedicine"
                if self.ui.antibioticsMedicine_chkbox.isChecked()
                else ""
            ),
            "Minoxidil" if self.ui.Minoxidil_chkbox.isChecked() else "",
            self.ui.medicationsOtherItems_txtbox.text().strip(),
        ]
        return "-".join(filter(None, mediciations))

    def _set_patient_allergies(self, allergies):
        allergy_list = allergies.split("-")
        for allergy in allergy_list:
            checkbox_name = f"{allergy}_chkbox"
            checkbox = getattr(self.ui, checkbox_name, None)
            if checkbox:
                checkbox.setChecked(True)
            else:
                self.ui.allergyOtherItems_txtbox.setText(allergy.strip())

    def _set_patient_diseases(self, diseases):
        disease_list = diseases.split("-")
        for disease in disease_list:
            checkbox_name = f"{disease}_chkbox"
            checkbox = getattr(self.ui, checkbox_name, None)
            if checkbox:
                checkbox.setChecked(True)
            else:
                self.ui.disaseOtherItems_txtbox.setText(disease.strip())

    def _set_patient_medications(self, medications):
        medication_list = medications.split("-")
        for medication in medication_list:
            checkbox_name = f"{medication}_chkbox"
            checkbox = getattr(self.ui, checkbox_name, None)
            if checkbox:
                checkbox.setChecked(True)
            else:
                self.ui.medicationsOtherItems_txtbox.setText(medication.strip())
