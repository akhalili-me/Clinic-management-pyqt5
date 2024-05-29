# controllers/add_patient_controller.py
from PyQt5.QtWidgets import QDialog
from ui.medical_records import Ui_medicalRecordsInfo_form
from models.db import DatabaseManager
from models.Patients import Patients
from models.MedicalRecords import MedicalRecords
from models.Doctors import Doctors
from models.Services import Services
from PyQt5.QtWidgets import QListWidgetItem

class MedicalRecordsInfoController(QDialog):
    def __init__(self,patientId):
        super(MedicalRecordsInfoController, self).__init__()
        self.ui = Ui_medicalRecordsInfo_form()
        self.ui.setupUi(self)

        self.setModal(True)

        self.db = DatabaseManager()
        patient = Patients.get_by_id(self.db, patientId)
        medical_records = MedicalRecords.get_by_patient_id(self.db,patient["id"])

        self._load_patient_data(patient)
        self._load_medical_records_list(medical_records)
        self.db.close()

    def _load_patient_data(self,patient):
        self.ui.firstName_lbl.setText(patient['firstName'])
        self.ui.lastName_lbl.setText(patient['lastName'])
        self.ui.age_lbl.setText(str(patient["age"]))
        self.ui.address_lbl.setText(patient["address"])
        self.ui.identityCode_lbl.setText(patient["identityCode"])
        self.ui.gender_lbl.setText(patient["gender"])
        self.ui.phoneNumber_lbl.setText(patient["phoneNumber"])
        self.ui.extraInfo_lbl.setText(patient["extraInfo"])

    def _load_medical_records_list(self, medical_records):
        self.ui.medicalRecords_lst.clear()
        for record in medical_records:
            service = Services.get_by_id(self.db,record["service"])
            doctor = Doctors.get_by_id(self.db, record["doctor"])
            item = QListWidgetItem(f"{service["name"]}  -  دکتر {doctor["lastName"]}  -  تاریخ: {record["visitDate"]}")
            item.setData(1,record["id"])
            self.ui.medicalRecords_lst.addItem(item)


         