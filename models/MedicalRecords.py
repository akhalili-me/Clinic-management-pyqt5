from .db import DatabaseManager,DatabaseError

class MedicalRecordImages:
    @staticmethod
    def get_by_id(db:DatabaseManager,id):
        query = f"SELECT * FROM MedicalRecordImages Where id={id}"

        try:
            return db.fetchone(query)
        except Exception as e:
            error_msg = f"""
                واکشی تصویر خدمات با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)
        
    @staticmethod
    def get_details_by_medical_record_id(db:DatabaseManager ,medical_record_id):
        query = f"""
        SELECT 
            mri.*
            FROM 
                MedicalRecordImages mri
            Where 
                mri.medical_record={medical_record_id}
        """
        try:
            return db.fetchall(query)
        except Exception as e:
            error_msg = f"""
                واکشی تصاویر خدمات با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)

    
    @staticmethod
    def get_all_image_paths_by_medical_record_id(db:DatabaseManager,medical_record_id):
        query = f"""
        SELECT 
            mri.path
            FROM 
                MedicalRecordImages mri
            Where 
                mri.medical_record={medical_record_id}
        """
        try:
            return db.fetchall(query)
        except Exception as e:
            error_msg = f"""
                واکشی تصاویر خدمات با خطا مواجه شده است.
                {str(e)}
            """
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
        except Exception as e:
            error_msg = f"""
                اضافه کردن تصویر خدمات با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)
        
    @staticmethod
    def delete_medical_record_image(db: DatabaseManager, image_id):
        query = f"DELETE FROM MedicalRecordImages WHERE id = {image_id};"
        try:
            return db.execute_query(query)
        except Exception as e:
            error_msg = f"""
                حذف تصویر خدمات با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)
        
    @staticmethod
    def get_all_image_paths_by_patient_id(db,patient_id):
        query = f"""
            SELECT 
                mri.path
            FROM 
                MedicalRecordImages mri
                JOIN MedicalRecords mr ON mri.medical_record = mr.id
            WHERE 
                mr.patient = {patient_id};
        """
        try:
            return db.fetchall(query)
        except Exception as e:
            error_msg = f"""
                واکشی تصاویر با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)
        
        
class MedicalRecords:
    @staticmethod
    def get_by_id(db: DatabaseManager, id):
        query = f"""
            SELECT 
                M.id,
                M.jalali_date,
                M.description,
                M.price,
                S.name AS service_name,
                P.firstName || ' ' || P.lastName AS patient_name,
                D.firstName || ' ' || D.lastName AS doctor_name
            FROM MedicalRecords M
            JOIN Service S ON M.service = S.id
            JOIN Doctor D ON M.doctor = D.id
            JOIN Patient P ON M.patient = P.id
            WHERE M.id = {id};
            """
        try:
            return db.fetchone(query)
        except Exception as e:
            error_msg = f"""
                واکشی خدمات با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)
        
    @staticmethod
    def get_details_by_id(db: DatabaseManager, id):
        query = f"""
        SELECT 
            M.*,
            S.name AS service_name,
            S.price AS service_price,
            D.firstName || ' ' || D.lastName AS doctor_name
        FROM MedicalRecords M
        JOIN Service S ON M.service = S.id
        JOIN Doctor D ON M.doctor = D.id
        WHERE M.id = {id};
    """
        try:
            return db.fetchone(query)
        except Exception as e:
            error_msg = f"""
                واکشی خدمات با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)

    @staticmethod
    def get_by_patient_id(db: DatabaseManager, patient_id):
        # query = f"SELECT * FROM MedicalRecords Where patient={patient_id} ORDER BY greg_date DESC"

        query = f"""
            SELECT 
                M.id,
                M.jalali_date,
                D.lastName AS doctor_lastname,
                S.name AS service_name
            From MedicalRecords M
            JOIN Doctor D ON M.doctor = D.id
            JOIN Service S ON M.service = S.id
            WHERE M.patient = {patient_id}
            ORDER BY greg_date DESC
        """
        try:
            return db.fetchall(query)
        except Exception as e:
            error_msg = f"""
                واکشی خدمات بیمار با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)


    @staticmethod
    def get_patient_file_number_medical_id(db,medical_record_id):
        query = f"""
            SELECT
                P.id
            FROM MedicalRecords M
            JOIN Patient P ON M.patient = P.id
            WHERE M.id = {medical_record_id}
        """
        try:
            return db.fetchone(query)
        except Exception as e:
            error_msg = f"""
                واکشی نام بیمار با خطا مواجه شده است.
                {str(e)}
            """       
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
        except Exception as e:
            error_msg = f"""
               اضافه کردن خدمات با خطا مواجه شده است.
                {str(e)}
            """      
            raise DatabaseError(error_msg)
        
    @staticmethod
    def update_medical_record(db: DatabaseManager, record):
        query = """UPDATE MedicalRecords
                    SET jalali_date = ?, 
                        greg_date = ?,
                        doctor = ?,
                        patient = ?,
                        service = ?,
                        description = ?"""
        values = [
            record["jalali_date"],
            record["greg_date"],
            record["doctor"],
            record["patient"],
            record["service"],
            record["description"]
        ]

        # Only include 'price' in the query if it exists in the record
        if "price" in record:
            query += ", price = ?"
            values.append(record["price"])

        query += " WHERE id = ?"
        values.append(record["id"])

        try:
            return db.execute_query(query, values)
        except Exception as e:
            error_msg = f"""
                ذخیره تغییرات خدمات با خطا مواجه شده است.
                {str(e)}
            """      
            raise DatabaseError(error_msg)

    @staticmethod
    def delete_medical_record(db: DatabaseManager, record_id):
        query = f"DELETE FROM MedicalRecords WHERE id = {record_id};"
        try:
            return db.execute_query(query)
        except Exception as e:
            error_msg = f"""
                حذف خدمات با خطا مواجه شده است.
                {str(e)}
            """      
            raise DatabaseError(error_msg)