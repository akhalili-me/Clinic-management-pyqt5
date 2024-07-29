import json
import os
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import sys
import sqlite3
import re
from utility import Messages

CONFIG_FILE = 'config.json'

class DatabaseUtils:
    def load_or_create_config():
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        else:
            # Create a default config if it doesn't exist
            default_config = {"database_path": ""}
            DatabaseUtils.save_config(default_config)
            return default_config

    def save_new_path(new_path):
        config = DatabaseUtils.load_or_create_config()
        config["database_path"] = new_path
        DatabaseUtils.save_config(config)
        
    def save_config(config):
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f)

    def check_database():
        config = DatabaseUtils.load_or_create_config()
        db_path = config['database_path']

        if not db_path or not os.path.exists(db_path):
            db_path = DatabaseUtils.create_or_import_database()

        if not DatabaseUtils.validate_database(db_path):
            Messages.show_error_msg("پایگاه داده معتبر نیست، برنامه را مجددا اجرا کنید.")
            config["database_path"] = ''
            DatabaseUtils.save_config(config)
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
        if db_path:
            return db_path

    def get_database_path():
        config = DatabaseUtils.load_or_create_config()
        return config['database_path']

    def get_default_sql_scheme():
        with open('ClinicDB_scheme.sql', 'r') as f:
            schema = f.read()
        return schema

    def validate_database(db_path):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = list(cursor.fetchall())
            conn.close()

            default_statements = DatabaseUtils.get_default_sql_scheme()
            default_table_names = re.findall(r'CREATE TABLE IF NOT EXISTS "([^"]+)"', default_statements)
            default_table_names.append("sqlite_sequence")

            
            for table in tables:
                if table[0] not in default_table_names:
                    return False

            return True
        except:
            return False