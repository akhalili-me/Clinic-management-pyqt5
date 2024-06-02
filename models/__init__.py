from .db import *
from .Doctors import *
from .Patients import *
from .Services import *
from .MedicalRecords import *
from .Appointments import *

class UtilityFetcher:
    @staticmethod
    def get_patient_service_doctor_names(db, patient_id=None, service_id=None, doctor_id=None):
        patient = {}
        service_name = None
        doctor_full_name = None

        if patient_id:
            patient_obj = Patients.get_full_name_phone_number_by_id(db, patient_id)
            patient["fullName"]= f"{patient_obj["firstName"]} {patient_obj["lastName"]}"
            patient["phoneNumber"] = patient_obj["phoneNumber"]

        if service_id:
            service = Services.get_name_by_id(db, service_id)
            service_name = service["name"]

        if doctor_id:
            doctor = Doctors.get_full_name_by_id(db, doctor_id)
            doctor_full_name = f"{doctor["firstName"]} {doctor["lastName"]}"

        return patient,service_name,doctor_full_name
