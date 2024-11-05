from .db import *
from .Doctors import *
from .Patients import *
from .Services import *
from .MedicalRecords import *
from .Appointments import *
from .Expenses import *
from .Reports import *

class Backup:
    @staticmethod
    def add_backup_info(db, backup_date):
        query = "INSERT INTO BackupInfo(date) VALUES (?)"
        values = (backup_date,)
        try:
            return db.execute_query(query, values)
        except Exception as e:
            error_msg = f"""
                اضافه کردن تاریخ پشتیبان با خطا مواجه شده است.
                {str(e)}
            """   
            raise DatabaseError(error_msg)

    @staticmethod
    def get_latest_backup_date(db):
        query = """
        SELECT date FROM BackupInfo 
        ORDER BY date DESC 
        LIMIT 1;
        """

        try:
            return db.fetchone(query)
        except Exception as e:
            error_msg = f"""
                واکشی تاریخ آخرین پشتیبانی باخطا مواجه شده است.
                {str(e)}
            """   
            raise DatabaseError(error_msg)


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
