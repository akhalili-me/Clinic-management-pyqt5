from .db import *
from .Doctors import *
from .Patients import *
from .Services import *
from .MedicalRecords import *
from .Appointments import *

class UtilityFetcher:
    @staticmethod
    def get_patient_service_doctor_names(db, patient_id=None, service_id=None, doctor_id=None):
        patient_full_name = None
        service_name = None
        doctor_full_name = None

        if patient_id:
            patient = Patients.get_full_name_by_id(db, patient_id)
            patient_full_name = f"{patient["firstName"]} {patient["lastName"]}"

        if service_id:
            service = Services.get_name_by_id(db, service_id)
            service_name = service["name"]

        if doctor_id:
            doctor = Doctors.get_full_name_by_id(db, doctor_id)
            doctor_full_name = f"{doctor["firstName"]} {doctor["lastName"]}"

        return patient_full_name,service_name,doctor_full_name
