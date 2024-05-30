# controllers/add_patient_controller.py
from PyQt5.QtWidgets import QDialog
from ui import Ui_medicalRecordsInfo_form
from models import Patients,DatabaseManager,MedicalRecords,Services,Doctors,Appointments
from PyQt5.QtWidgets import QListWidgetItem
from utility import Numbers,Dates


class MedicalRecordsInfoController(QDialog):
    def __init__(self,patientId):
        super(MedicalRecordsInfoController, self).__init__()
        self.ui = Ui_medicalRecordsInfo_form()
        self.ui.setupUi(self)
        self.setModal(True)

        self.db = DatabaseManager()
        self.patient = Patients.get_by_id(self.db, patientId)
        medical_records = MedicalRecords.get_by_patient_id(self.db,patientId)
        

        self._load_patient_data(self.patient)
        self._load_medical_records_list(medical_records)
        self.load_appointments_list()

        # Connecting_buttons
        self.ui.editPatient_btn.clicked.connect(self.open_edit_patient)
        self.ui.addAppointment_btn.clicked.connect(self.open_add_appointment)

        self.db.close()

    def open_add_appointment(self):
        from controllers import AddEditAppointmentController
        self.add_appointment_controller = AddEditAppointmentController(self.patient["id"])
        self.add_appointment_controller.refresh_appointment_list.connect(self.load_appointments_list)
        self.add_appointment_controller.show()

    def open_edit_patient(self):
        from controllers import AddEditPatientController
        self.edit_patient_controller = AddEditPatientController(self.patient)
        self.edit_patient_controller.refresh_patient_md_records_data.connect(self._load_patient_data)
        self.edit_patient_controller.show()

    def _load_patient_data(self,patient=None):

        if patient==None:
            with DatabaseManager() as db:
                patient = Patients.get_by_id(db,self.patient["id"])

        identity_code = Numbers.english_to_persian_numbers(patient["identityCode"])
        phone_number = Numbers.english_to_persian_numbers(patient["phoneNumber"])

        self.ui.firstName_lbl.setText(patient['firstName'])
        self.ui.lastName_lbl.setText(patient['lastName'])
        self.ui.age_lbl.setText(str(patient["age"]))
        self.ui.address_lbl.setText(patient["address"])
        self.ui.identityCode_lbl.setText(identity_code)
        self.ui.gender_lbl.setText(patient["gender"])
        self.ui.phoneNumber_lbl.setText(phone_number)
        self.ui.extraInfo_lbl.setText(patient["extraInfo"])

    def _load_medical_records_list(self, medical_records):
        self.ui.medicalRecords_lst.clear()
        for record in medical_records:
            service = Services.get_by_id(self.db,record["service"])
            doctor = Doctors.get_by_id(self.db, record["doctor"])
            item = QListWidgetItem(f"{service["name"]}  -  دکتر {doctor["lastName"]}  -  تاریخ: {record["visitDate"]}")
            item.setData(1,record["id"])
            self.ui.medicalRecords_lst.addItem(item)

    def load_appointments_list(self):
        self.ui.appointments_lst.clear()
        with DatabaseManager() as db:
            appointments = Appointments.get_by_patient_id(db,self.patient["id"])
            for appointment in appointments:
                service = Services.get_by_id(self.db,appointment["service"])
                doctor = Doctors.get_by_id(self.db, appointment["doctor"])
                date = Dates.convert_to_jalali_format(appointment["date"])
                time = Numbers.english_to_persian_numbers(appointment["time"])
                item_txt = f"{service["name"]} | دکتر {doctor["lastName"]} | {appointment["status"]} | {date} | {time}"
                item = QListWidgetItem(item_txt)
                item.setData(1,appointment["id"])
                self.ui.appointments_lst.addItem(item)


         
