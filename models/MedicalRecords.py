from .db import DatabaseManager,DatabaseError

class MedicalRecords:

    @staticmethod
    def get_by_patient_id(db: DatabaseManager, patient_id):
        query = f"SELECT * FROM MedicalRecords Where patient={patient_id} ORDER BY greg_date DESC"
        try:
            return db.fetchall(query)
        except DatabaseError as e:
            print(f"Database error: {e}")
            return []

    @staticmethod
    def add_medical_record(db:DatabaseManager,record):
        query = """INSERT INTO MedicalRecords(jalali_date,greg_date, doctor, patient, service, description)
                VALUES (?,?,?,?,?,?)
                """

        values = (
            record["jalali_date"],
            record["greg_date"],
            record["doctor"],
            record["patient"],
            record["service"],
            record["description"],
        )
        try:
            return db.execute_query(query, values)
        except DatabaseError as e:
            print(f"Database error: {e}")
            return []
