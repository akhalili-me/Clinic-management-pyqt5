from .db import DatabaseManager,DatabaseError

class Doctors:
    
    @staticmethod
    def get_all(db: DatabaseManager):
        query = "SELECT * FROM Doctor ORDER BY id DESC"
        try:
            return db.fetchall(query)
        except DatabaseError as e:
            print(f"Database error: {e}")
            return []
        
    @staticmethod
    def get_by_id(db: DatabaseManager, doctor_id):
        query = f"SELECT * FROM Doctor Where id={doctor_id}"
        try:
            return db.fetchone(query)
        except DatabaseError as e:
            print(f"Database error: {e}")
            return []
        
    @staticmethod
    def add_doctor(db: DatabaseManager, doctor):
        query = query = "INSERT INTO Doctor(firstName, lastName, specialization) VALUES (?,?,?)"
        values = (doctor["firstName"],doctor["lastName"],doctor["specialization"])
        try:
            return db.execute_query(query, values)
        except DatabaseError as e:
            print(f"Database error: {e}")
            return []


    
 

    


