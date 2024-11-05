import os
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import sys
import sqlite3
import re
from utility import Messages, ConfigUtils, RESOURCES_DIR
from pathlib import Path
import logging


class DatabaseUtils:
    def save_new_path(new_db_path):
        ConfigUtils.set_value("database_path",new_db_path) 

    def check_database():
        db_path = ConfigUtils.get_value("database_path")

        if not db_path or not os.path.exists(db_path):
            db_path = DatabaseUtils.create_or_import_database()

        if not DatabaseUtils.validate_database(db_path):
            Messages.show_error_msg("پایگاه داده معتبر نیست، برنامه را مجددا اجرا کنید.")
            ConfigUtils.set_value("database_path","")
            sys.exit()

        DatabaseUtils.save_new_path(db_path)

    def create_or_import_database():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText("هیچ پایگاه داده‌ای یافت نشد.")

        create_button = msg_box.addButton("ساختن پایگاه داده جدید", QMessageBox.ActionRole)
        import_button = msg_box.addButton("وارد کردن پایگاه داده", QMessageBox.ActionRole)
        cancel_button = msg_box.addButton("لغو", QMessageBox.RejectRole)
        msg_box.setDefaultButton(create_button)

        msg_box.exec_()

        if msg_box.clickedButton() == create_button:
            return DatabaseUtils.create_database()
        elif msg_box.clickedButton() == import_button:
            return DatabaseUtils.import_database()
        elif msg_box.clickedButton() == cancel_button or msg_box.clickedButton() is None:
            sys.exit()

    def create_database():
        db_path, _ = QFileDialog.getSaveFileName(None, "Create Database", "", "SQLite Database Files (*.sqlite)")
        if db_path:
            schema = DatabaseUtils.get_default_sql_scheme()
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.executescript(schema)
            conn.commit()
            conn.close()
            return db_path

    def import_database():
        db_path, _ = QFileDialog.getOpenFileName(None, "Import Database", "", "SQLite Database Files (*.sqlite *.db *.sqlite3)")
        return db_path if db_path else None

    def get_database_path():
        return ConfigUtils.get_value("database_path")

    def get_default_sql_scheme():
        db_scheme_path = Path.joinpath(RESOURCES_DIR,'ClinicDB_scheme.sql')
        with open(db_scheme_path, 'r') as f:
            schema = f.read()
        return schema

    def parse_schema():
        schema = DatabaseUtils.get_default_sql_scheme()
        table_definitions = re.findall(r'CREATE TABLE IF NOT EXISTS "([^"]+)" \((.*?)\);', schema, re.S)
        schema_dict = {}
        for table_name, fields in table_definitions:
            fields = fields.split(",")
            schema_dict[table_name] = {}
            for field in fields:
                match = re.match(r'\s*"([^"]+)"\s+([A-Z]+)', field.strip())
                if match:
                    field_name, field_type = match.groups()
                    schema_dict[table_name][field_name] = field_type
        return schema_dict

    def validate_database(db_path):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = list(cursor.fetchall())

            
            default_schema = DatabaseUtils.parse_schema()

            
            for table in tables:
                table_name = table[0]
               
                if table_name == "sqlite_sequence":
                    continue
                
                if table_name not in default_schema:
                    return False

                cursor.execute(f"PRAGMA table_info({table_name});")
                columns = cursor.fetchall()

                for column in columns:
                    column_name, column_type = column[1], column[2].upper()
                    if column_name not in default_schema[table_name] or default_schema[table_name][column_name] != column_type:
                        return False

            conn.close()
            return True
        except Exception as e:
            logging.error(f"Error occured: {str(e)}")
            return False
