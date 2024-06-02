# controllers/add_patient_controller.py
from PyQt5.QtWidgets import QDialog
from ui import Ui_patientFile_form
from models import Patients,DatabaseManager,MedicalRecords,Services,Doctors,Appointments
from PyQt5.QtWidgets import QListWidgetItem
from utility import Numbers,Dates,Messages
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal

class PatientFileController(QDialog):
    refresh_patients_list = pyqtSignal()
    load_today_appointments_list = pyqtSignal()

    def __init__(self, patient_id):
        super(PatientFileController, self).__init__()
        self.ui = Ui_patientFile_form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.patient_id = patient_id

        self.load_patient_data()
        self.load_user_medical_records_list()
        self.load_user_appointments_list()

        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.editPatient_btn.clicked.connect(self.open_edit_patient)
        self.ui.addAppointment_btn.clicked.connect(self.open_add_appointment)
        self.ui.addNewMedicalRecord_btn.clicked.connect(self.open_add_medical_record)
        self.ui.deletePatient_btn.clicked.connect(self.open_delete_message_box)
        self.ui.userAppointments_lst.itemDoubleClicked.connect(self.open_appointment_info)
        self.ui.userMedicalRecords_lst.itemDoubleClicked.connect(self.open_medical_record_info)


    def open_medical_record_info(self,item):
        medical_record_id = item.data(1)
        from controllers import MedicalRecordInfoController
        self.appointment_info_controller = MedicalRecordInfoController(medical_record_id)
        self.appointment_info_controller.load_user_medical_records_list.connect(self.load_user_medical_records_list)
        self.appointment_info_controller.show()

    def open_appointment_info(self,item):
        appointment_id = item.data(1)
        from controllers import AppointmentInfoController
        self.appointment_info_controller = AppointmentInfoController(appointment_id)
        self.appointment_info_controller.load_user_appointment_list.connect(self.load_user_appointments_list)
        self.appointment_info_controller.load_user_medical_records_list.connect(self.load_user_medical_records_list)
        self.appointment_info_controller.load_today_appointments_list.connect(self.load_today_appointments_list)
        self.appointment_info_controller.show()

    def open_delete_message_box(self):
        msg_box, yes_button = Messages.show_confirm_delete_msg()
        if msg_box.clickedButton() == yes_button:
            with DatabaseManager() as db:
                Patients.delete_patient(db, self.patient_id)
                Messages.show_success_msg("پرونده بیمار با موفقیت حذف شد.")
                self.close()
                self.refresh_patients_list.emit()
        else:
            msg_box.close()

    def open_add_medical_record(self):
        from controllers import AddEditMedicalRecordsController
        self.add_medical_record_controller = AddEditMedicalRecordsController(self.patient_id)
        self.add_medical_record_controller.refresh_medical_records_list.connect(self.load_user_medical_records_list)
        self.add_medical_record_controller.show()

    def open_add_appointment(self):
        from controllers import AddEditAppointmentController
        self.add_appointment_controller = AddEditAppointmentController(self.patient_id)
        self.add_appointment_controller.refresh_user_appointment_list_data.connect(self.load_user_appointments_list)
        self.add_appointment_controller.load_today_appointments_list.connect(self.load_today_appointments_list)
        self.add_appointment_controller.show()

    def open_edit_patient(self):
        from controllers import AddEditPatientController
        with DatabaseManager() as db:
            patient = Patients.get_by_id(db, self.patient_id)
        self.edit_patient_controller = AddEditPatientController(patient)
        self.edit_patient_controller.refresh_patient_file_data.connect(self.load_patient_data)
        self.edit_patient_controller.refresh_patients_list.connect(self.refresh_patients_list)
        self.edit_patient_controller.show()

    def load_patient_data(self):
        with DatabaseManager() as db:
            patient = Patients.get_by_id(db, self.patient_id)

        self.ui.firstName_lbl.setText(patient['firstName'])
        self.ui.lastName_lbl.setText(patient['lastName'])
        self.ui.age_lbl.setText(str(patient["age"]))
        self.ui.address_lbl.setText(patient["address"])
        self.ui.identityCode_lbl.setText(Numbers.english_to_persian_numbers(patient["identityCode"]))
        self.ui.gender_lbl.setText(patient["gender"])
        self.ui.phoneNumber_lbl.setText(Numbers.english_to_persian_numbers(patient["phoneNumber"]))
        self.ui.extraInfo_lbl.setText(patient["extraInfo"])

    def load_user_medical_records_list(self):
        self.ui.userMedicalRecords_lst.clear()
        with DatabaseManager() as db:
            medical_records = MedicalRecords.get_by_patient_id(db, self.patient_id)
            for record in medical_records:
                service = Services.get_by_id(db, record["service"])
                doctor = Doctors.get_by_id(db, record["doctor"])
                jalali_date = Dates.convert_to_jalali_format(record["jalali_date"])
                item_text = f"{service['name']}  |  دکتر {doctor['lastName']}  |  تاریخ: {jalali_date}"
                item = QListWidgetItem(item_text)
                item.setData(1, record["id"])
                self.ui.userMedicalRecords_lst.addItem(item)

    def load_user_appointments_list(self):
        self.ui.userAppointments_lst.clear()
        with DatabaseManager() as db:
            appointments = Appointments.get_by_patient_id(db, self.patient_id)
            for appointment in appointments:
                service = Services.get_by_id(db, appointment["service"])
                doctor = Doctors.get_by_id(db, appointment["doctor"])
                date = Dates.convert_to_jalali_format(appointment["jalali_date"])
                time = Numbers.english_to_persian_numbers(appointment["time"])
                item_text = f"{service['name']} | دکتر {doctor['lastName']} | {appointment['status']} | {date} | {time}"
                item = QListWidgetItem(item_text)
                item.setData(1, appointment["id"])
                self.ui.userAppointments_lst.addItem(item)



         
