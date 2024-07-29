from .db import DatabaseManager, DatabaseError


class Patients:

    @staticmethod
    def get_all(db: DatabaseManager):
        query = "SELECT * FROM Patient ORDER BY id DESC"
        try:
            return db.fetchall(query)
        except Exception:
            error_msg = "واکشی بیماران با خطا مواجه شده است."
            raise DatabaseError(error_msg)

    @staticmethod
    def get_by_id(db: DatabaseManager, patient_id):
        query = f"SELECT * FROM Patient WHERE id={patient_id}"
        try:
            return db.fetchone(query)
        except Exception:
            error_msg = "واکشی اطلاعات بیمار با خطا مواجه شده است."
            raise DatabaseError(error_msg)
        
    @staticmethod
    def get_full_name_phone_number_by_id(db,patient_id):
        query = f"SELECT firstName, lastName, phoneNumber FROM Patient Where id={patient_id}"
        try:
            return db.fetchone(query)
        except Exception:
            error_msg = "واکشی شماره تلفن بیمار خطا مواجه شده است."
            raise DatabaseError(error_msg)

    @staticmethod
    def get_by_identity_code(db: DatabaseManager, identityCode):
        query = f"SELECT * FROM Patient Where identityCode='{identityCode}'"
        try:
            return db.fetchone(query)
        except Exception:
            error_msg = "واکشی بیمار با خطا مواجه شده است."
            raise DatabaseError(error_msg)

    @staticmethod
    def get_by_last_name(db: DatabaseManager, lastName):
        query = f"SELECT * FROM Patient Where lastName Like '%{lastName}%'"
        try:
            return db.fetchall(query)
        except Exception:
            error_msg = "جستجو بیمارها با خطا مواجه شده است."
            raise DatabaseError(error_msg)

    def patient_exist_identity_code(db: DatabaseManager, identityCode):
        query = f"SELECT 1 FROM Patient WHERE identityCode = '{identityCode}' LIMIT 1"
        try:
            return db.fetchone(query)
        except Exception:
            error_msg = "چک کردن وجود اطلاعات بیمار با خطا مواجه شده است."
            raise DatabaseError(error_msg)

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
        except Exception:
            error_msg = "اضافه کردن بیمار با خطا مواجه شده است."
            raise DatabaseError(error_msg)

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
        except Exception:
            error_msg = "ذخیره تغییرات اطلاعات بیمار با خطا مواجه شده است."
            raise DatabaseError(error_msg)
        
    @staticmethod
    def delete_patient(db: DatabaseManager, patient_id):
        query = f"DELETE FROM Patient WHERE id = {patient_id};"
        try:
            return db.execute_query(query)
        except Exception:
            error_msg = "حذف بیمار با خطا مواجه شده است."
            raise DatabaseError(error_msg)
