from .db import DatabaseManager,DatabaseError

class MedicalRecords:
        
    @staticmethod
    def get_by_patient_id(db: DatabaseManager, patient_id):
        query = f"SELECT * FROM MedicalRecords Where patient={patient_id}"
        try:
            return db.fetchall(query)
        except DatabaseError as e:
            print(f"Database error: {e}")
            return []

