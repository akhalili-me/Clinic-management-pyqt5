from .db import DatabaseManager, DatabaseError


class Appointments:

    @staticmethod
    def get_by_patient_id(db: DatabaseManager, patient_id):
        query = f"SELECT * FROM Appointment Where patient={patient_id} ORDER BY greg_datetime ASC"
        try:
             return db.fetchall(query)
        except DatabaseError as e:
            raise e
    
    @staticmethod
    def get_by_id(db: DatabaseManager, appointment_Id):
        query = f"SELECT * FROM Appointment Where id={appointment_Id}"
        try:
             return db.fetchone(query)
        except DatabaseError as e:
            raise e

    @staticmethod
    def get_by_date(db: DatabaseManager, date):
        query = f"SELECT * FROM Appointment Where jalali_date='{date}' ORDER BY greg_datetime ASC"
        try:
            return db.fetchall(query)
        except DatabaseError as e:
            raise e

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
        except DatabaseError as e:
            raise e

    
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
        except DatabaseError as e:
            raise e
        
    @staticmethod
    def delete_appointment(db: DatabaseManager, appointment_id):
        query = f"DELETE FROM Appointment WHERE id = {appointment_id};"
        try:
            return db.execute_query(query)
        except DatabaseError as e:
            raise e