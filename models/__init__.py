from .db import *
from .Doctors import *
from .Patients import *
from .Services import *
from .MedicalRecords import *
from .Appointments import *
from .Expenses import *
from .Reports import *

def delete_appointment_add_medical_record_transaction(db, appointment_id, medical_record):
    appointment_delete_query = "DELETE FROM Appointment WHERE id = ?;"
    appointment_delete_params = [appointment_id]
    
    medical_record_insert_query = """
        INSERT INTO MedicalRecords(jalali_date, greg_date, doctor, patient, service, description, price)
        VALUES (?, ?, ?, ?, ?, ?, ?);
    """
    medical_record_insert_params = (
        medical_record["jalali_date"],
        medical_record["greg_date"],
        medical_record["doctor"],
        medical_record["patient"],
        medical_record["service"],
        medical_record["description"],
        medical_record["price"]
    )
    
    try:
        db.execute_transaction([
            (appointment_delete_query, appointment_delete_params),
            (medical_record_insert_query, medical_record_insert_params)
        ])
    except Exception:
        error_msg = "اضافه کردن نوبت به خدمات به خطا مواجه شده است."
        raise DatabaseError(error_msg)
   