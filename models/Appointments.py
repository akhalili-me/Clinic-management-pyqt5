from .db import DatabaseError


class Appointments:

    @staticmethod
    def get_by_patient_id(db, patient_id):
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
        except Exception as e:
            error_msg  = f"""
                واکشی نوبت‌های بیمار با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)

    @staticmethod
    def get_by_id(db, appointment_Id):
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
        except Exception as e:
            error_msg = f"""
                واکشی نوبت با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)

    @staticmethod
    def get_by_jalali_date(db, date, status):
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
            AND A.status='{status}'
            ORDER BY A.greg_datetime ASC
        """

        try:
            return db.fetchall(query)
        except Exception as e:
            error_msg = f"""
                واکشی نوبت‌ها با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)

    @staticmethod
    def get_appointment_details_by_id(db, id):
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
        except Exception as e:
            error_msg = f"""
                واکشی نوبت‌ با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)

    @staticmethod
    def add_appointment(db, appointment):
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
        except Exception as e:
            error_msg = f"""
                اضافه کردن نوبت با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)

    @staticmethod
    def update_appointment(db, appointment):
        base_query = "UPDATE Appointment SET "
        conditions = []
        values = []

        for field in [
            "status",
            "jalali_date",
            "greg_datetime",
            "time",
            "doctor",
            "service",
            "description",
            "sms",
        ]:
            if field in appointment:
                conditions.append(f"{field} = ?")
                values.append(appointment[field])

        if "id" not in appointment:
            raise DatabaseError("شناسه نوبت برای آپدیت نیاز است.")
        values.append(appointment["id"])

        query = base_query + ", ".join(conditions) + " WHERE id = ?"

        try:
            return db.execute_query(query, tuple(values))
        except Exception as e:
            error_msg = f"""
                ذخیره کردن نوبت با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)

    @staticmethod
    def delete_appointment(db, appointment_id):
        query = f"DELETE FROM Appointment WHERE id = {appointment_id};"
        try:
            return db.execute_query(query)
        except Exception as e:
            error_msg = f"""
                حذف نوبت با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)

    @staticmethod
    def get_appointments_for_auto_send_sms(db, start_date, end_date):
        query = f"""
            SELECT    
                A.id,  
                A.jalali_date,
                A.time,
                A.sms,
                P.firstName || ' ' || P.lastName AS patient_name,
                P.phoneNumber AS phone_number,
                S.name AS service_name
            FROM Appointment A
            JOIN Patient P ON A.patient = P.id
            JOIN Service S ON A.service = S.id
            WHERE greg_datetime BETWEEN '{start_date}' AND '{end_date}'
                AND sms = 0
                AND status = 'فعال';
        """

        try:
            return db.fetchall(query)
        except Exception as e:
            error_msg = f"""
                واکشی نوبت‌ها برای ارسال پیامک با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)

    @staticmethod
    def get_appointments_for_send_sms(db, jalali_date):
        query = f"""
            SELECT    
                A.id,  
                A.jalali_date,
                A.time,
                A.sms,
                P.firstName || ' ' || P.lastName AS patient_name,
                P.phoneNumber AS phone_number,
                S.name AS service_name
            FROM Appointment A
            JOIN Patient P ON A.patient = P.id
            JOIN Service S ON A.service = S.id
            Where A.jalali_date='{jalali_date}'
                AND status = 'فعال';
        """

        try:
            return db.fetchall(query)
        except Exception as e:
            error_msg = f"""
                واکشی نوبت‌ها برای ارسال پیامک با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)
