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

    @staticmethod
    def get_full_name_by_id(db,doctor_id):
        query = f"SELECT firstName,lastName FROM Doctor Where id={doctor_id}"
        try:
            return db.fetchone(query)
        except DatabaseError as e:
            print(f"Database error: {e}")
            return []
    
    @staticmethod
    def update_doctor(db: DatabaseManager, doctor):
        query = """UPDATE Doctor
                    SET firstName = ?, 
                        lastName = ?, 
                        specialization = ?
                    WHERE id = ?
                """
        values = (
            doctor["firstName"],
            doctor["lastName"],
            doctor["specialization"],
            doctor["id"],
        )

        try:
            return db.execute_query(query, values)
        except DatabaseError as e:
            print(f"Database error: {e}")
            return []

    @staticmethod
    def delete_doctor(db: DatabaseManager, doctor_id):
        query = f"DELETE FROM Doctor WHERE id = {doctor_id};"
        try:
            return db.execute_query(query)
        except DatabaseError as e:
            print(f"Database error: {e}")
            return []

    


