from .db import DatabaseManager, DatabaseError


class Appointments:

    # @staticmethod
    # def get_all(db: DatabaseManager):
    #     query = "SELECT * FROM Patient ORDER BY id DESC"
    #     try:
    #         return db.fetchall(query)
    #     except DatabaseError as e:
    #         print(f"Database error: {e}")
    #         return []

    @staticmethod
    def get_by_patient_id(db: DatabaseManager, patient_id):
        query = f"SELECT * FROM Appointment Where patient={patient_id}"
        try:
             return db.fetchall(query)
        except DatabaseError as e:
            print(f"Database error: {e}")
        return []

    # @staticmethod
    # def get_by_identity_code(db: DatabaseManager, identityCode):
    #     query = f"SELECT * FROM Patient Where identityCode='{identityCode}'"
    #     try:
    #         return db.fetchone(query)
    #     except DatabaseError as e:
    #         print(f"Database error: {e}")
    #         return []

    # @staticmethod
    # def get_by_last_name(db: DatabaseManager, lastName):
    #     query = f"SELECT * FROM Patient Where lastName='{lastName}'"
    #     try:
    #         return db.fetchall(query)
    #     except DatabaseError as e:
    #         print(f"Database error: {e}")
    #         return []

    @staticmethod
    def add_appointment(db: DatabaseManager, appointment):
        query = """INSERT INTO Appointment(status, date, time, doctor, patient, service, description)
                VALUES (?,?,?,?,?,?,?)
                """
        
        values = (
            appointment["status"],
            appointment["date"],
            appointment["time"],
            appointment["doctor"],
            appointment["patient"],
            appointment["service"],
            appointment["description"],
        )
        try:
            return db.execute_query(query, values)
        except DatabaseError as e:
            print(f"Database error: {e}")
            return []
