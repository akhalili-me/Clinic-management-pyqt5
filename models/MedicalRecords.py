from .db import DatabaseManager,DatabaseError

class MedicalRecordImages:
    @staticmethod
    def get_by_id(db:DatabaseManager,id):
        query = f"SELECT * FROM MedicalRecordImages Where id={id}"
        try:
            return db.fetchone(query)
        except Exception:
            error_msg = "واکشی تصویر خدمات با خطا مواجه شده است."
            raise DatabaseError(error_msg)
        
    @staticmethod
    def get_by_medical_record_id(db:DatabaseManager,medical_record_id):
        query = f"SELECT * FROM MedicalRecordImages Where medical_record={medical_record_id}"
        try:
            return db.fetchall(query)
        except Exception:
            error_msg = "واکشی تصاویر خدمات با خطا مواجه شده است."
            raise DatabaseError(error_msg)

    @staticmethod
    def add_medical_record_image(db:DatabaseManager,medical_record_image):
        query = """INSERT INTO MedicalRecordImages(path,name,medical_record)
                VALUES (?,?,?)
                """
        values = (
            medical_record_image["path"],
            medical_record_image["name"],
            medical_record_image["medical_record"],
        )
        try:
            return db.execute_query(query, values)
        except Exception:
            error_msg = "اضافه کردن تصویر خدمات با خطا مواجه شده است."
            raise DatabaseError(error_msg)
        
    @staticmethod
    def delete_medical_record_image(db: DatabaseManager, image_id):
        query = f"DELETE FROM MedicalRecordImages WHERE id = {image_id};"
        try:
            return db.execute_query(query)
        except Exception:
            error_msg = "حذف تصویر خدمات با خطا مواجه شده است."
            raise DatabaseError(error_msg)
        
class MedicalRecords:

    @staticmethod
    def get_by_id(db: DatabaseManager, id):
        query = f"SELECT * FROM MedicalRecords Where id={id}"
        try:
            return db.fetchone(query)
        except Exception:
            error_msg = "واکشی خدمات با خطا مواجه شده است."
            raise DatabaseError(error_msg)

    @staticmethod
    def get_by_patient_id(db: DatabaseManager, patient_id):
        query = f"SELECT * FROM MedicalRecords Where patient={patient_id} ORDER BY greg_date DESC"
        try:
            return db.fetchall(query)
        except Exception:
            error_msg = "واکشی خدمات با خطا مواجه شده است."
            raise DatabaseError(error_msg)

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
        except Exception:
            error_msg = "اضافه کردن خدمات با خطا مواجه شده است."
            raise DatabaseError(error_msg)
        
    @staticmethod
    def update_medical_record(db: DatabaseManager, record):
        query = """UPDATE MedicalRecords
                    SET jalali_date = ?, 
                        greg_date = ?,
                        doctor = ?,
                        patient = ?,
                        service = ?,
                        description = ?,
                        price = ?
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
        except Exception:
            error_msg = "ذخیره تغییرات خدمات با خطا مواجه شده است."
            raise DatabaseError(error_msg)

    @staticmethod
    def delete_medical_record(db: DatabaseManager, record_id):
        query = f"DELETE FROM MedicalRecords WHERE id = {record_id};"
        try:
            return db.execute_query(query)
        except Exception:
            error_msg = "حذف خدمات با خطا مواجه شده است."
            raise DatabaseError(error_msg)