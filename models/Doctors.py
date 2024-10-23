from .db import DatabaseManager,DatabaseError

class Doctors:
    
    @staticmethod
    def get_all(db: DatabaseManager):
        query = "SELECT * FROM Doctor ORDER BY id DESC"
        try:
            return db.fetchall(query)
        except Exception as e:
            error_msg = f"""
                واکشی اطلاعات پزشک‌ها با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)
        
    @staticmethod
    def get_by_id(db: DatabaseManager, doctor_id):
        query = f"SELECT * FROM Doctor Where id={doctor_id}"
        try:
            return db.fetchone(query)
        except Exception as e:
            error_msg = f"""
                واکشی اطلاعات پزشک‌ با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)
        
    @staticmethod
    def add_doctor(db: DatabaseManager, doctor):
        query = query = "INSERT INTO Doctor(firstName, lastName, specialization) VALUES (?,?,?)"
        values = (doctor["firstName"],doctor["lastName"],doctor["specialization"])
        try:
            return db.execute_query(query, values)
        except Exception as e:
            error_msg = f"""
                اضافه کردن پزشک‌ با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)

    @staticmethod
    def get_full_name_by_id(db,doctor_id):
        query = f"SELECT firstName,lastName FROM Doctor Where id={doctor_id}"
        try:
            return db.fetchone(query)
        except Exception as e:
            error_msg = f"""
                واکشی نام و نام خانوادگی پزشک‌ با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)
    
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
        except Exception as e:
            error_msg = f"""
                ذخیره کردن تغییرات پزشک‌ با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)

    @staticmethod
    def delete_doctor(db: DatabaseManager, doctor_id):
        query = f"DELETE FROM Doctor WHERE id = {doctor_id};"
        try:
            return db.execute_query(query)
        except Exception as e:
            error_msg = f"""
                حذف پزشک‌ با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)

    


