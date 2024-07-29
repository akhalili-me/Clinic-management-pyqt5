from .db import DatabaseManager, DatabaseError


class Appointments:

    @staticmethod
    def get_by_patient_id(db: DatabaseManager, patient_id):
        query = f"SELECT * FROM Appointment Where patient={patient_id} ORDER BY greg_datetime ASC"
        try:
             return db.fetchall(query)
        except Exception:
            error_msg = "واکشی نوبت‌های بیمار با خطا مواجه شده است."
            raise DatabaseError(error_msg)
    
    @staticmethod
    def get_by_id(db: DatabaseManager, appointment_Id):
        query = f"SELECT * FROM Appointment Where id={appointment_Id}"
        try:
             return db.fetchone(query)
        except Exception:
            error_msg = "واکشی نوبت با خطا مواجه شده است."
            raise DatabaseError(error_msg)

    @staticmethod
    def get_by_date(db: DatabaseManager, date):
        query = f"SELECT * FROM Appointment Where jalali_date='{date}' ORDER BY greg_datetime ASC"
        try:
            return db.fetchall(query)
        except Exception:
            error_msg = "واکشی نوبت‌ها با خطا مواجه شده است."
            raise DatabaseError(error_msg)

    @staticmethod
    def add_appointment(db: DatabaseManager, appointment):
        query = """INSERT INTO Appointment(status, jalali_date,greg_datetime, time, doctor, patient, service, description)
                VALUES (?,?,?,?,?,?,?,?)
                """
        
        values = (
            appointment["status"],
            appointment["jalali_date"],
            appointment["greg_datetime"],
            appointment["time"],
            appointment["doctor"],
            appointment["patient"],
            appointment["service"],
            appointment["description"],
        )
        try:
            return db.execute_query(query, values)
        except Exception:
            error_msg = "اضافه کردن نوبت با خطا مواجه شده است."
            raise DatabaseError(error_msg)

    
    @staticmethod
    def update_appointment(db: DatabaseManager, appointment):
        query = """UPDATE Appointment
                    SET status = ?, 
                        jalali_date = ?, 
                        greg_datetime = ?, 
                        time = ?, 
                        doctor = ?, 
                        patient = ?, 
                        service = ?, 
                        description = ?
                    WHERE id = ?
                """
        
        values = (
            appointment["status"],
            appointment["jalali_date"],
            appointment["greg_datetime"],
            appointment["time"],
            appointment["doctor"],
            appointment["patient"],
            appointment["service"],
            appointment["description"],
            appointment["id"]
        )
        try:
            return db.execute_query(query, values)
        except Exception:
            error_msg = "ذخیره کردن نوبت با خطا مواجه شده است."
            raise DatabaseError(error_msg)
        
    @staticmethod
    def delete_appointment(db: DatabaseManager, appointment_id):
        query = f"DELETE FROM Appointment WHERE id = {appointment_id};"
        try:
            return db.execute_query(query)
        except Exception:
            error_msg = "حذف نوبت با خطا مواجه شده است."
            raise DatabaseError(error_msg)