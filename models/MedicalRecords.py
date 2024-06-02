from .db import DatabaseManager,DatabaseError

class MedicalRecords:

    @staticmethod
    def get_by_id(db: DatabaseManager, id):
        query = f"SELECT * FROM MedicalRecords Where id={id}"
        try:
            return db.fetchone(query)
        except DatabaseError as e:
            raise e
        
    @staticmethod
    def get_by_patient_id(db: DatabaseManager, patient_id):
        query = f"SELECT * FROM MedicalRecords Where patient={patient_id} ORDER BY greg_date DESC"
        try:
            return db.fetchall(query)
        except DatabaseError as e:
            raise e 

    @staticmethod
    def add_medical_record(db:DatabaseManager,record):
        query = """INSERT INTO MedicalRecords(jalali_date,greg_date, doctor, patient, service, description,price)
                VALUES (?,?,?,?,?,?,?)
                """

        values = (
            record["jalali_date"],
            record["greg_date"],
            record["doctor"],
            record["patient"],
            record["service"],
            record["description"],
            record["price"],
        )
        try:
            return db.execute_query(query, values)
        except DatabaseError as e:
            raise e
        
    @staticmethod
    def update_medical_record(db: DatabaseManager, record):
        query = """UPDATE MedicalRecords
                    SET jalali_date = ?, 
                        greg_date = ?,
                        doctor = ?,
                        patient = ?,
                        service = ?,
                        description = ?,
                        price = ?,
                    WHERE id = ?
                """
        values = (
            record["jalali_date"],
            record["greg_date"],
            record["doctor"],
            record["patient"],
            record["service"],
            record["description"],
            record["price"],
            record["id"]
        )
        try:
            return db.execute_query(query, values)
        except DatabaseError as e:
            raise e

    @staticmethod
    def delete_medical_record(db: DatabaseManager, record_id):
        query = f"DELETE FROM MedicalRecords WHERE id = {record_id};"
        try:
            return db.execute_query(query)
        except DatabaseError as e:
            print(f"Database error: {e}")
            raise e