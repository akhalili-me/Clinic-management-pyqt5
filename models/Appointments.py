from .db import DatabaseManager, DatabaseError


class Appointments:

    @staticmethod
    def get_by_patient_id(db: DatabaseManager, patient_id):
        # query = f"SELECT * Where patient={patient_id} ORDER BY greg_datetime ASC"
        query = f"""
            SELECT 
                A.id,
                A.jalali_date,
                A.status,
                A.time,
                S.name AS service_name,
                D.lastName as doctor_lastname
            FROM Appointment A
            JOIN Service S ON A.service = S.id
            JOIN Doctor D ON A.doctor = D.id
            Where A.patient={patient_id}
            ORDER BY greg_datetime ASC
        """
        try:
             return db.fetchall(query)
        except Exception:
            error_msg = "واکشی نوبت‌های بیمار با خطا مواجه شده است."
            raise DatabaseError(error_msg)
    
    @staticmethod
    def get_by_id(db: DatabaseManager, appointment_Id):
        query = f"""
            SELECT 
                A.*,
                S.name AS service_name,
                D.firstName || ' ' || D.lastName AS doctor_name
            FROM Appointment A
            JOIN Patient P ON A.patient = P.id
            JOIN Service S ON A.service = S.id
            JOIN Doctor D ON A.doctor = D.id
            Where A.id={appointment_Id}; 
            """
        try:
             return db.fetchone(query)
        except Exception:
            error_msg = "واکشی نوبت با خطا مواجه شده است."
            raise DatabaseError(error_msg)

    @staticmethod
    def get_by_jalali_date(db: DatabaseManager, date):
        query = f""" 
            SELECT      
                A.id,
                A.status,
                A.jalali_date,
                A.greg_datetime,
                A.time,
                A.description,
                P.firstName || ' ' || P.lastName AS patient_name,
                P.phoneNumber AS phone_number,
                S.name AS service_name,
                D.firstName || ' ' || D.lastName AS doctor_name
            FROM Appointment A
            JOIN Patient P ON A.patient = P.id
            JOIN Service S ON A.service = S.id
            JOIN Doctor D ON A.doctor = D.id
            Where A.jalali_date='{date}' 
            ORDER BY A.greg_datetime ASC
        """
        
        try:
            return db.fetchall(query)
        except Exception:
            error_msg = "واکشی نوبت‌ها با خطا مواجه شده است."
            raise DatabaseError(error_msg)


    @staticmethod
    def get_appointment_details_by_id(db:DatabaseManager, id):
        query = f""" 
            SELECT      
                A.*,
                P.firstName || ' ' || P.lastName AS patient_name,
                P.phoneNumber AS phone_number,
                S.name AS service_name,
                S.price AS service_price,
                D.firstName || ' ' || D.lastName AS doctor_name
            FROM Appointment A
            JOIN Patient P ON A.patient = P.id
            JOIN Service S ON A.service = S.id
            JOIN Doctor D ON A.doctor = D.id
            Where A.id='{id}' 
        """
        try:
            return db.fetchone(query)
        except Exception:
            error_msg = "واکشی نوبت‌ با خطا مواجه شده است."
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