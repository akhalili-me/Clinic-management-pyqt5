from .db import DatabaseManager, DatabaseError


class Patients:

    @staticmethod
    def get_all(db: DatabaseManager):
        query = "SELECT * FROM Patient ORDER BY id DESC"
        try:
            return db.fetchall(query)
        except Exception as e:
            error_msg = f"""
                واکشی بیماران با خطا مواجه شده است.
                {str(e)}
            """      
            raise DatabaseError(error_msg)

    @staticmethod
    def get_by_id(db: DatabaseManager, patient_id):
        query = f"SELECT * FROM Patient WHERE id={patient_id}"
        try:
            return db.fetchone(query)
        except Exception as e:
            error_msg = f"""
                واکشی اطلاعات بیمار با خطا مواجه شده است.
                {str(e)}
            """      
            raise DatabaseError(error_msg)

    @staticmethod
    def get_full_name_phone_number_by_id(db,patient_id):
        query = f"SELECT firstName, lastName, phoneNumber FROM Patient Where id={patient_id}"
        try:
            return db.fetchone(query)
        except Exception as e:
            error_msg = "واکشی شماره تلفن بیمار خطا مواجه شده است."
            raise DatabaseError(error_msg)

    @staticmethod
    def get_by_identity_code(db: DatabaseManager, identityCode):
        query = f"SELECT * FROM Patient Where identityCode='{identityCode}'"
        try:
            return db.fetchone(query)
        except Exception as e:
            error_msg = f"""
                واکشی بیمار با خطا مواجه شده است.
                {str(e)}
            """      
            raise DatabaseError(error_msg)

    @staticmethod
    def get_by_last_name(db: DatabaseManager, lastName):
        query = f"SELECT * FROM Patient Where lastName Like '%{lastName}%'"
        try:
            return db.fetchall(query)
        except Exception as e:
            error_msg = f"""
                جستجو بیمارها با خطا مواجه شده است.
                {str(e)}
            """      
            raise DatabaseError(error_msg)

    def patient_exist_identity_code(db: DatabaseManager, identityCode):
        query = f"SELECT 1 FROM Patient WHERE identityCode = '{identityCode}' LIMIT 1"
        try:
            return db.fetchone(query)
        except Exception as e:
            error_msg = f"""
                چک کردن وجود اطلاعات بیمار با خطا مواجه شده است.
                {str(e)}
            """      
            raise DatabaseError(error_msg)
        
    def get_patient_id_by_identity_code(db: DatabaseManager, identity_code):
        query = f"SELECT id FROM Patient WHERE identityCode = '{identity_code}'"
        try:
            return db.fetchone(query)
        except Exception as e:
            error_msg = f"""
                واکشی شماره پرونده بیمار با خطا مواجه شده است.
                {str(e)}
            """      
            raise DatabaseError(error_msg)

    @staticmethod
    def add_patient(db: DatabaseManager, patient):
        query = """INSERT INTO Patient(firstName, lastName, job, age, phoneNumber, address, identityCode, extraInfo,
                                    maritalStatus, specialCondition, pregnant, allergy, disease, medication)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """
        
        values = (
            patient["firstName"],
            patient["lastName"],
            patient["job"],
            patient["age"],
            patient["phoneNumber"],
            patient["address"],
            patient["identityCode"],
            patient["extraInfo"],
            patient["maritalStatus"],
            patient["specialCondition"],
            patient["pregnant"],
            patient["allergy"],
            patient["disease"],
            patient["medication"]
        )

        try:
            patient_id = db.execute_query(query, values)
            return patient_id
        except Exception as e:
            error_msg = f"""
            اضافه کردن بیمار با خطا مواجه شده است.
            {str(e)}
            """
            raise DatabaseError(error_msg)


    @staticmethod
    def update_patient(db: DatabaseManager, patient):
        query = """UPDATE Patient
                    SET firstName = ?, 
                        lastName = ?, 
                        age = ?, 
                        phoneNumber = ?, 
                        address = ?, 
                        extraInfo = ?,
                        identityCode = ?,
                        maritalStatus = ?,
                        specialCondition = ?,
                        pregnant = ?,
                        allergy = ?,
                        disease = ?,
                        medication = ?
                    WHERE id = ?
                """

        values = (
            patient["firstName"],
            patient["lastName"],
            patient["age"],
            patient["phoneNumber"],
            patient["address"],
            patient["extraInfo"],
            patient["identityCode"],
            patient["maritalStatus"],
            patient["specialCondition"],
            patient["pregnant"],
            patient["allergy"],
            patient["disease"],
            patient["medication"],
            patient["id"]
        )

        try:
            return db.execute_query(query, values)
        except Exception as e:
            error_msg = f"""
                ذخیره تغییرات اطلاعات بیمار با خطا مواجه شده است.
                {str(e)}
            """      
            raise DatabaseError(error_msg)

    @staticmethod
    def delete_patient(db: DatabaseManager, patient_id):
        query = f"DELETE FROM Patient WHERE id = {patient_id};"
        try:
            return db.execute_query(query)
        except Exception as e:
            error_msg = f"""
                حذف بیمار با خطا مواجه شده است.
                {str(e)}
            """      
            raise DatabaseError(error_msg)
