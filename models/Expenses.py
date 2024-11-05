from .db import DatabaseError

class Expenses:
    
    @staticmethod
    def get_by_id(db, expense_id):
        query = f"SELECT * FROM Expense Where id={expense_id}"
        try:
            return db.fetchone(query)
        except Exception as e:
            error_msg = f"""
                واکشی هزینه با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)
        
    @staticmethod
    def add_expense(db, expense):
        query = query = "INSERT INTO Expense(name, price, description, jalali_date,greg_date) VALUES (?,?,?,?,?)"
        values = (expense["name"],expense["price"],expense["description"],expense["jalali_date"],expense["greg_date"])
        try:
            return db.execute_query(query, values)
        except Exception as e:
            error_msg = f"""
                اضافه کردن هزینه با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)

    @staticmethod
    def get_by_date(db , from_date, to_date):
        query = f"SELECT * FROM Expense WHERE greg_date BETWEEN '{from_date}' AND '{to_date}' ORDER BY greg_date DESC"
       
        try:
            return db.fetchall(query)
        except Exception as e:
            error_msg = f"""
                واکشی هزینه‌ها با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)
        
    @staticmethod
    def search_by_name(db, name):
        query = f"SELECT * FROM Expense Where name Like '%{name}%'"
        try:
            return db.fetchall(query)
        except Exception as e:
            error_msg = f"""
                جستجو هزینه‌ها با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)
    
    @staticmethod
    def update_expense(db, expense):
        query = """UPDATE Expense
                    SET name = ?, 
                        price = ?, 
                        description = ?,
                        jalali_date = ?,
                        greg_date = ?
                    WHERE id = ?
                """
        values = (
            expense["name"],
            expense["price"],
            expense["description"],
            expense["jalali_date"],
            expense["greg_date"],
            expense["id"],
        )

        try:
            return db.execute_query(query, values)
        except Exception as e:
            error_msg = f"""
                ثبت تغییرات هزینه با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)

    @staticmethod
    def delete_expense(db, expense_id):
        query = f"DELETE FROM Expense WHERE id = {expense_id};"
        try:
            return db.execute_query(query)
        except Exception as e:
            error_msg = f"""
                حذف هزینه با خطا مواجه شده است.
                {str(e)}
            """
            raise DatabaseError(error_msg)
