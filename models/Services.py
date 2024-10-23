from .db import DatabaseManager,DatabaseError

class Services:
    
    @staticmethod
    def get_all(db: DatabaseManager):
        query = "SELECT * FROM Service"
        try:
            return db.fetchall(query)
        except Exception as e:
            error_msg = f"""
                واکشی اطلاعات سرویس‌‌ها با خطا مواجه شده است.
                {str(e)}
            """   
            raise DatabaseError(error_msg)
        
    @staticmethod
    def get_name_price_by_id(db,service_id):
        query = f"SELECT name,price FROM Service Where id={service_id}"
        try:
            return db.fetchone(query)
        except Exception as e:
            error_msg = f"""
                واکشی نام و قیمت سرویس‌‌ با خطا مواجه شده است.
                {str(e)}
            """   
            raise DatabaseError(error_msg)

    @staticmethod
    def get_by_id(db: DatabaseManager,service_id):
        query = f"SELECT * FROM Service Where id={service_id}"
        try:
            return db.fetchone(query)
        except Exception as e:
            error_msg = f"""
                واکشی اطلاعات سرویس‌ با خطا مواجه شده است.
                {str(e)}
            """   
            raise DatabaseError(error_msg)
   
    
    @staticmethod
    def add_service(db:DatabaseManager, service):
        query = "INSERT INTO Service(name,price) VALUES (?,?)"
        values = (service["name"], service["price"])
        try:
            return db.execute_query(query, values)
        except Exception as e:
            error_msg = f"""
                اضافه کردن سرویس با خطا مواجه شده است.
                {str(e)}
            """   
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
        except Exception as e:
            error_msg = f"""
                ثبت تغییرات با خطا مواجه شده است.
                {str(e)}
            """   
           
            raise DatabaseError(error_msg)

    @staticmethod
    def delete_service(db: DatabaseManager, service_id):
        query = f"DELETE FROM Service WHERE id = {service_id};"
        try:
            return db.execute_query(query)
        except Exception as e:
            error_msg = f"""
                حذف سرویس با خطا مواجه شده است.
                {str(e)}
            """   
            raise DatabaseError(error_msg)
        
    @staticmethod
    def search_service_by_name(db,service_name):
        query = f"SELECT * FROM Service Where name Like '%{service_name}%'"
        try:
            return db.fetchall(query)
        except Exception as e:
            error_msg = f"""
                جستجو سرویس‌ها با خطا مواجه شده است.
                {str(e)}
            """      
            raise DatabaseError(error_msg)

