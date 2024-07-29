from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from utility import DatabaseUtils,Messages,restart_app,copy_file_to_directory
from PyQt5.QtWidgets import QFileDialog
import jdatetime

from controllers import (
    DoctorsTabController,
    PatientsTabController,
    ServicesTabController,
    AppointmentsTabController,
    ExpenseTabController,
    ReportsTabController
)

class MainController(QMainWindow):
    def __init__(self):
        super(MainController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._connect_buttons()

        #Initilize tabs
        self.appointments_tab_controller = AppointmentsTabController(self.ui)
        self.doctors_tab_controller = DoctorsTabController(self.ui)
        self.patients_tab_controller = PatientsTabController(self.ui,self.appointments_tab_controller)
        self.services_tab_controller = ServicesTabController(self.ui)
        self.expense_tab_controller = ExpenseTabController(self.ui)
        self.report_controller = ReportsTabController(self.ui)


    def _connect_buttons(self):
        self.ui.save_backup.triggered.connect(self.save_database_backup)
        self.ui.import_backup.triggered.connect(self.import_database)

    def save_database_backup(self):
        db_path = DatabaseUtils.get_database_path()

        dir_dialog = QFileDialog(self)
        selected_dir_path = dir_dialog.getExistingDirectory()

        if selected_dir_path:
            current_time = jdatetime.datetime.now().strftime('%Y-%m-%d %H-%M')
            file_name = "backup " + current_time
            copy_file_to_directory(db_path,selected_dir_path,file_name)
            Messages.show_success_msg("پشتیبان پایگاه داده با موفقیت ذخیره شد.")


    def import_database(self):
        new_db_path = DatabaseUtils.import_database()
        
        if not DatabaseUtils.validate_database(new_db_path):
            Messages.show_error_msg("پایگاه داده انتخابی معتبر نمی‌باشد.")
            return
        DatabaseUtils.save_new_path(new_db_path)
        restart_app()

        

        


