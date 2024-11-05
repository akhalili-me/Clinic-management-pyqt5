# controllers/add_patient_controller.py
from PyQt5.QtWidgets import QDialog, QFileDialog,QCheckBox
from ui import get_ui_class
from models import (
    Patients,
    MedicalRecords,
    Appointments,
    DatabaseWorker,
)
import os
from PyQt5.QtWidgets import QListWidgetItem
from utility import (
    Numbers,
    Dates,
    Messages,
    Images,
    BaseController,
    delete_patient_directory,
    get_patient_signature_image_path,
)
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from utility import (
    create_patient_file_pdf,
    PatientTranslations,
    get_patient_signature_image_path,
    MEDIA_DIR,
)


class PatientFileController(BaseController, QDialog):
    refresh_patients_list = pyqtSignal()

    def __init__(self, patient_id, dispatcher):
        super(PatientFileController, self).__init__()
        self.ui = get_ui_class("patientFile")()
        self.ui.setupUi(self)
        self.setModal(True)
        self.active_workers = []
        self.dispatcher = dispatcher
        self.dispatcher.refresh_patient_medical_records_list.connect(
            self.load_patient_medical_records_list
        )
        self.patient_id = patient_id
        self.patient_file_pdf_dir = None
        self._load_initial_data()
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.editPatient_btn.clicked.connect(self.open_edit_patient)
        self.ui.addAppointment_btn.clicked.connect(self.open_add_appointment)
        self.ui.addNewMedicalRecord_btn.clicked.connect(self.open_add_medical_record)
        self.ui.deletePatient_btn.clicked.connect(self.open_delete_message_box)
        self.ui.userAppointments_lst.itemDoubleClicked.connect(
            self.open_appointment_info
        )
        self.ui.userMedicalRecords_lst.itemDoubleClicked.connect(
            self.open_medical_record_info
        )
        self.ui.printPatientFIle_btn.clicked.connect(self.generate_patient_pdf)
        self.ui.openPatientFolder_btn.clicked.connect(self.open_patient_folder)

    def open_patient_folder(self):
        patient_folder_path = f"{MEDIA_DIR}/{self.patient_id}"
        os.makedirs(patient_folder_path, exist_ok=True)
        os.startfile(patient_folder_path)

    def generate_patient_pdf(self):
        options = QFileDialog.Options()
        directory = QFileDialog.getExistingDirectory(
            self, "Select Directory", "", options=options
        )

        if directory:
            self._start_worker(
                Patients.get_patient_and_medical_records,
                [self.patient_id],
                self.create_pdf_file,
            )
            self.patient_file_pdf_dir = directory

    def create_pdf_file(self, patient_medical_data):
        patient, medical_records = patient_medical_data

        translated_allergies = PatientTranslations.translate_allergies(
            patient["allergy"]
        )
        patient["allergy"] = translated_allergies
        translated_diseases = PatientTranslations.translate_diseases(patient["disease"])
        patient["disease"] = translated_diseases
        translated_medications = PatientTranslations.translate_medications(
            patient["medication"]
        )
        patient["medication"] = translated_medications
        patient["signature"] = get_patient_signature_image_path(patient["id"])

        create_patient_file_pdf(patient, medical_records, self.patient_file_pdf_dir)
        Messages.show_success_msg("فایل پرونده بیمار با موفقیت ذخیره شد")
        self.close()

    def _load_initial_data(self):
        self.load_patient_info()
        self.load_patient_medical_records_list()
        self.load_patient_appointments_list()

    def open_medical_record_info(self, item):
        medical_record_id = item.data(1)
        from controllers import MedicalRecordInfoController

        self.appointment_info_controller = MedicalRecordInfoController(
            medical_record_id, self.dispatcher
        )
        self.appointment_info_controller.load_user_medical_records_list.connect(
            self.load_patient_appointments_list
        )
        self.appointment_info_controller.show()

    def open_appointment_info(self, item):
        appointment_id = item.data(1)
        from controllers import AppointmentInfoController

        self.appointment_info_controller = AppointmentInfoController(
            appointment_id, self.dispatcher
        )
        self.appointment_info_controller.load_user_appointment_list.connect(
            self.load_patient_appointments_list
        )
        self.appointment_info_controller.load_user_medical_records_list.connect(
            self.load_patient_medical_records_list
        )
        self.appointment_info_controller.show()

    def open_delete_message_box(self):
        msg_box, yes_button = Messages.show_confirm_delete_msg()
        if msg_box.clickedButton() != yes_button:
            msg_box.close()
            return

        self._start_worker(
            Patients.delete_patient,
            [self.patient_id],
            success_callback=self.handle_patient_delete,
        )

    def handle_patient_delete(self):
        delete_patient_directory(str(self.patient_id))
        self.operation_successful("بیمار با موفقیت حذف شد.")

    def delete_all_patients_medical_record_images(self, images):
        for image in images:
            Images.delete_image(image["path"])

    def operation_successful(self, success_msg):
        Messages.show_success_msg(success_msg)
        self.refresh_patients_list.emit()
        self.close()

    def open_add_medical_record(self):
        from controllers import AddEditMedicalRecordsController

        self.add_medical_record_controller = AddEditMedicalRecordsController(
            self.dispatcher, self.patient_id
        )
        self.add_medical_record_controller.show()

    def open_add_appointment(self):
        from controllers import AddEditAppointmentController

        self.add_appointment_controller = AddEditAppointmentController(
            self.dispatcher, self.patient_id
        )
        self.add_appointment_controller.refresh_user_appointment_list_data.connect(
            self.load_patient_appointments_list
        )
        self.add_appointment_controller.load_today_appointments_list.connect(
            self.dispatcher.refresh_appointments_list
        )
        self.add_appointment_controller.show()

    def open_edit_patient(self):
        from controllers import AddEditPatientController

        self.edit_patient_controller = AddEditPatientController(self.patient_id)
        self.edit_patient_controller.refresh_patient_file_data.connect(
            self.load_patient_info
        )
        self.edit_patient_controller.refresh_patients_list.connect(
            self.refresh_patients_list
        )
        self.edit_patient_controller.show()

    def load_patient_info(self):
        self._start_worker(
            Patients.get_by_id, [self.patient_id], self.display_patient_info
        )

    def display_patient_info(self, patient):
        self._set_extraItem_default_text()
        if patient:
            age = Numbers.english_to_persian_numbers(str(patient["age"]))
            self.ui.fileNumber_lbl.setText(
                Numbers.english_to_persian_numbers(str(patient["id"]))
            )
            self.ui.firstName_lbl.setText(patient["firstName"])
            self.ui.lastName_lbl.setText(patient["lastName"])
            self.ui.age_lbl.setText(age)
            self.ui.address_lbl.setText(patient["address"])
            self.ui.identityCode_lbl.setText(
                Numbers.english_to_persian_numbers(patient["identityCode"])
            )
            self.ui.job_lbl.setText(patient["job"])
            self.ui.phoneNumber_lbl.setText(
                Numbers.english_to_persian_numbers(patient["phoneNumber"])
            )
            self.ui.extraInfo_lbl.setText(patient["extraInfo"])
            self.ui.maritalStatus_lbl.setText(patient["maritalStatus"])
            self.ui.specialCondition_lbl.setText(patient["specialCondition"])
            self.ui.pregnant_lbl.setText(patient["pregnant"])

            self._uncheck_checkboxes()
            self._set_patient_allergies(patient["allergy"])
            self._set_patient_diseases(patient["disease"])
            self._set_patient_medications(patient["medication"])
            self._display_patient_signature()

    def _display_patient_signature(self):
        signature_path = get_patient_signature_image_path(self.patient_id)
        if os.path.exists(signature_path):
            signature_pixmap = QPixmap(signature_path)
            self.ui.signatureImage_lbl.setPixmap(signature_pixmap)
        else:
            self.ui.signatureImage_lbl.setText("بدون امضاء")

    def load_patient_medical_records_list(self):
        self._start_worker(
            MedicalRecords.get_by_patient_id,
            [self.patient_id],
            self.display_patient_medical_records_list,
        )

    def display_patient_medical_records_list(self, medical_records):
        self.ui.userMedicalRecords_lst.clear()
        for record in medical_records:
            jalali_date = Dates.convert_to_jalali_format(record["jalali_date"])
            item_text = f"{record['service_name']}  |  دکتر {record['doctor_lastname']}  |  تاریخ: {jalali_date}"
            item = QListWidgetItem(item_text)
            item.setData(1, record["id"])
            self.ui.userMedicalRecords_lst.addItem(item)

    def load_patient_appointments_list(self):
        worker = DatabaseWorker(Appointments.get_by_patient_id, self.patient_id)
        worker.result_signal.connect(self.display_patient_appointments_list)
        worker.error_signal.connect(self.handle_error)
        self.active_workers.append(worker)
        worker.start()

    def load_patient_appointments_list(self):
        self._start_worker(
            Appointments.get_by_patient_id,
            [self.patient_id],
            self.display_patient_appointments_list,
        )

    def display_patient_appointments_list(self, appointments):
        self.ui.userAppointments_lst.clear()
        for appointment in appointments:
            jalali_date = Dates.convert_to_jalali_format(appointment["jalali_date"])
            time = Numbers.english_to_persian_numbers(appointment["time"])
            item_text = f"{appointment['service_name']} | دکتر {appointment['doctor_lastname']} | {appointment['status']} | {jalali_date} | {time}"
            item = QListWidgetItem(item_text)
            item.setData(1, appointment["id"])
            self.ui.userAppointments_lst.addItem(item)

    def _set_patient_allergies(self, allergies):
        allergy_list = allergies.split("-")
        for allergy in allergy_list:
            checkbox_name = f"{allergy}_chkbox"
            checkbox = getattr(self.ui, checkbox_name, None)
            if checkbox:
                checkbox.setChecked(True)
            else:
                self.ui.allergyOtherItems_lbl.setText(allergy)

    def _set_patient_diseases(self, diseases):
        disease_list = diseases.split("-")
        for disease in disease_list:
            checkbox_name = f"{disease}_chkbox"
            checkbox = getattr(self.ui, checkbox_name, None)
            if checkbox:
                checkbox.setChecked(True)
            else:
                self.ui.diseaseOtherItems_lbl.setText(disease)

    def _set_patient_medications(self, medications):
        medication_list = medications.split("-")
        for medication in medication_list:
            checkbox_name = f"{medication}_chkbox"
            checkbox = getattr(self.ui, checkbox_name, None)
            if checkbox:
                checkbox.setChecked(True)
            else:
                self.ui.medicationOtherItems_lbl.setText(medication)

    def _set_extraItem_default_text(self):
        self.ui.allergyOtherItems_lbl.setText("-")
        self.ui.diseaseOtherItems_lbl.setText("-")
        self.ui.medicationOtherItems_lbl.setText("-")

    def _uncheck_checkboxes(self):
        checkboxes = self.findChildren(QCheckBox) 
        for checkbox in checkboxes:
            checkbox.setChecked(False)
