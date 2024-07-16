from PyQt5.QtSql import QSqlDatabase, QSqlQuery


# BASE_DIR = Path(__file__).resolve().parent.parent
# DB_DIR = BASE_DIR / "resources" / "ClinicDB.db"



class DatabaseError(Exception):
    """Custom exception for database errors."""
    pass

class DatabaseManager:
    def __init__(self):
        if QSqlDatabase.contains('qt_sql_default_connection'):
            self.db = QSqlDatabase.database('qt_sql_default_connection')
        else:
            self.db = QSqlDatabase.addDatabase('QSQLITE')

        from utility import DatabaseUtils
        DB_DIR = DatabaseUtils.get_database_path()
        
        self.db.setDatabaseName(str(DB_DIR))

        if not self.db.open():
            raise DatabaseError("Error: Unable to open database")
        
        # Enable foreign key support
        self.enable_foreign_keys()

    def enable_foreign_keys(self):
        """Enable foreign key support for the SQLite database."""
        query = QSqlQuery()
        if not query.exec_("PRAGMA foreign_keys = ON;"):
            raise DatabaseError(f"Error enabling foreign keys: {query.lastError().text()}")

    def _execute(self, query_str, params=()):
        """Helper method to prepare and execute a query."""
        query = QSqlQuery()
        query.prepare(query_str)
        for param in params:
            query.addBindValue(param)
        if not query.exec_():
            raise DatabaseError(f"Error executing query: {query.lastError().text()}")
        return query

    def execute_query(self, query_str, params=()):
        """Executes a query without returning any results."""
        self._execute(query_str, params)

    def fetchall(self, query_str, params=()):
        """Executes a query and returns all results as a list of dictionaries."""
        query = self._execute(query_str, params)
        results = []
        record = query.record()
        while query.next():
            row = {record.fieldName(i): query.value(i) for i in range(record.count())}
            results.append(row)
        return results

    def fetchone(self, query_str, params=()):
        """Executes a query and returns a single result as a dictionary."""
        query = self._execute(query_str, params)
        if query.next():
            record = query.record()
            return {record.fieldName(i): query.value(i) for i in range(record.count())}
        return None

    def close(self):
        """Closes the database connection."""
        self.db.close()

    def __enter__(self):
        """Enter the runtime context related to this object."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the runtime context related to this object."""
        self.close()
