from .db import DatabaseManager, DatabaseError


class Patients:

    @staticmethod
    def get_all(db: DatabaseManager):
        query = "SELECT * FROM Patient ORDER BY id DESC"
        try:
            return db.fetchall(query)
        except DatabaseError as e:
            print(f"Database error: {e}")
            return []

    @staticmethod
    def get_by_id(db: DatabaseManager, patient_id):
        query = f"SELECT * FROM Patient Where id={patient_id}"
        try:
            return db.fetchone(query)
        except DatabaseError as e:
            print(f"Database error: {e}")
            return []

    @staticmethod
    def get_by_identity_code(db: DatabaseManager, identityCode):
        query = f"SELECT * FROM Patient Where identityCode='{identityCode}'"
        try:
            return db.fetchone(query)
        except DatabaseError as e:
            print(f"Database error: {e}")
            return []

    @staticmethod
    def get_by_last_name(db: DatabaseManager, lastName):
        query = f"SELECT * FROM Patient Where lastName='{lastName}'"
        try:
            return db.fetchall(query)
        except DatabaseError as e:
            print(f"Database error: {e}")
            return []

    @staticmethod
    def add_patient(db: DatabaseManager, patient):
        query = """INSERT INTO Patient(firstName, lastName, gender, age, phoneNumber, address, identityCode, extraInfo)
          VALUES (?,?,?,?,?,?,?,?)
          """
        values = (
            patient["firstName"],
            patient["lastName"],
            patient["gender"],
            patient["age"],
            patient["phoneNumber"],
            patient["address"],
            patient["identityCode"],
            patient["extraInfo"],
        )
        try:
            return db.execute_query(query, values)
        except DatabaseError as e:
            print(f"Database error: {e}")
            return []

    @staticmethod
    def update_patient(db: DatabaseManager, patient):
        query = """UPDATE Patient
                    SET firstName = ?, 
                        lastName = ?, 
                        gender = ?, 
                        age = ?, 
                        phoneNumber = ?, 
                        address = ?, 
                        extraInfo = ?,
                        identityCode = ?
                    WHERE id = ?
                """
        
        values = (
            patient["firstName"],
            patient["lastName"],
            patient["gender"],
            patient["age"],
            patient["phoneNumber"],
            patient["address"],
            patient["extraInfo"],
            patient["identityCode"],
            patient["id"]
        )

        try:
            return db.execute_query(query, values)
        except DatabaseError as e:
            print(f"Database error: {e}")
            return []
