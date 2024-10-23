from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import QObject, pyqtSignal
import uuid

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

class DatabaseManagerForWorker(QObject):

    def __init__(self):
        super().__init__()
        from utility import DatabaseUtils
        self.db_path = DatabaseUtils.get_database_path()
        self.db = None

    def create_connection(self):
        connection_name = str(uuid.uuid4())
        self.db = QSqlDatabase.addDatabase('QSQLITE', connection_name)
        self.db.setDatabaseName(self.db_path)

        if not self.db.open():
            raise DatabaseError(f"Unable to open database: {self.db.lastError().text()}")
        
        self.enable_foreign_keys()
        return self.db

    def close(self):
        if self.db and self.db.isOpen():
            self.db.close()
            QSqlDatabase.removeDatabase(self.db.connectionName())
    
    def __enter__(self):
        self.create_connection()
        return self
     
    def __exit__(self, exc_type, exc_value, traceback):
        self.close

    def execute_query(self, query_str, params=()):
        query = QSqlQuery(self.db)
        query.prepare(query_str)
        for param in params:
            query.addBindValue(param)
        if not query.exec_():
            raise DatabaseError(f"Error executing query: {query.lastError().text()}")
        
        # Return last inserted row ID if this is an INSERT query
        if query_str.strip().lower().startswith('insert'):
            return query.lastInsertId()

    def fetchall(self, query_str, params=()):
        query = QSqlQuery(self.db)
        query.prepare(query_str)
        for param in params:
            query.addBindValue(param)
        if not query.exec_():
            raise DatabaseError(f"Error executing query: {query.lastError().text()}")

        results = []
        while query.next():
            record = query.record()
            row = {record.fieldName(i): query.value(i) for i in range(record.count())}
            results.append(row)
        return results

    def fetchone(self, query_str, params=()):
        results = self.fetchall(query_str, params)
        return results[0] if results else None
    
    def enable_foreign_keys(self):
        query = QSqlQuery(self.db)
        if not query.exec_("PRAGMA foreign_keys = ON;"):
            raise DatabaseError(f"Error enabling foreign keys: {query.lastError().text()}")
    
    def begin_transaction(self):
        if not self.db.transaction():
            raise DatabaseError(f"Failed to start transaction: {self.db.lastError().text()}")

    def commit(self):
        if not self.db.commit():
            raise DatabaseError(f"Failed to commit transaction: {self.db.lastError().text()}")

    def rollback(self):
        if not self.db.rollback():
            raise DatabaseError(f"Failed to rollback transaction: {self.db.lastError().text()}")

    def execute_transaction(self, queries_with_params):
        """
        Executes multiple queries within a single transaction.
        
        Args:
            queries_with_params (list of tuples): Each tuple contains a query string and its parameters.
            
        Raises:
            DatabaseError: If any query fails, the transaction is rolled back.
        """
        self.begin_transaction()
        try:
            for query_str, params in queries_with_params:
                self.execute_query(query_str, params)
            self.commit()
        except Exception as e:
            self.rollback()
            raise DatabaseError(f"Transaction failed: {str(e)}")

class DatabaseWorker(QThread):
    result_signal = pyqtSignal(object)
    error_signal = pyqtSignal(str)
    success_signal = pyqtSignal()  

    def __init__(self, operation, *args):
        super().__init__()
        self.operation = operation
        self.args = args

    def run(self):
        try:
            with DatabaseManagerForWorker() as db:
                result = self.operation(db, *self.args)
                self.result_signal.emit(result)
                self.success_signal.emit()
        except Exception as e:
            self.error_signal.emit(str(e))
