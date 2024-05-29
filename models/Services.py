from .db import DatabaseManager,DatabaseError

class Services:
    
    @staticmethod
    def get_all(db: DatabaseManager):
        query = "SELECT * FROM Service"
        try:
            return db.fetchall(query)
        except DatabaseError as e:
            print(f"Database error: {e}")
            return []
        
    @staticmethod
    def get_by_id(db: DatabaseManager,service_id):
        query = f"SELECT * FROM Service Where id={service_id}"
        try:
            return db.fetchone(query)
        except DatabaseError as e:
            print(f"Database error: {e}")
            return []
    
    @staticmethod
    def add_service(db:DatabaseManager, service):
        query = "INSERT INTO Service(name,price) VALUES (?,?)"
        values = (service["name"], service["price"])
        try:
            return db.execute_query(query, values)
        except DatabaseError as e:
            print(f"Database error: {e}")
            return []

    


