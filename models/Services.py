from .db import DatabaseManager,DatabaseError

class Services:
    
    @staticmethod
    def get_all(db: DatabaseManager):
        query = "SELECT * FROM Service"
        try:
            return db.fetchall(query)
        except Exception:
            error_msg = "واکشی اطلاعات سرویس‌‌ها با خطا مواجه شده است."
            raise DatabaseError(error_msg)
        
    @staticmethod
    def get_name_price_by_id(db,service_id):
        query = f"SELECT name,price FROM Service Where id={service_id}"
        try:
            return db.fetchone(query)
        except Exception:
            error_msg = "واکشی نام و قیمت سرویس‌‌ با خطا مواجه شده است."
            raise DatabaseError(error_msg)

    @staticmethod
    def get_by_id(db: DatabaseManager,service_id):
        query = f"SELECT 1* FROM Service Where id={service_id}"
        try:
            return db.fetchone(query)
        except Exception:
            error_msg = "واکشی اطلاعات سرویس‌ با خطا مواجه شده است."
            raise DatabaseError(error_msg)
   
    
    @staticmethod
    def add_service(db:DatabaseManager, service):
        query = "INSERT INTO Service(name,price) VALUES (?,?)"
        values = (service["name"], service["price"])
        try:
            return db.execute_query(query, values)
        except Exception:
            error_msg = "اضافه کردن سرویس با خطا مواجه شده است."
            raise DatabaseError(error_msg)

    @staticmethod
    def update_service(db: DatabaseManager, service):
        query = """UPDATE Service
                    SET name = ?, 
                        price = ?
                    WHERE id = ?
                """
        values = (
            service["name"],
            service["price"],
            service["id"]
        )
        try:
            return db.execute_query(query, values)
        except Exception:
            error_msg = "ثبت تغییرات با خطا مواجه شده است."
            raise DatabaseError(error_msg)

    @staticmethod
    def delete_service(db: DatabaseManager, service_id):
        query = f"DELETE FROM Service WHERE id = {service_id};"
        try:
            return db.execute_query(query)
        except Exception:
            error_msg = "حذف سرویس با خطا مواجه شده است."
            raise DatabaseError(error_msg)

