from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow


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

        #Initilize tabs
        self.appointments_tab_controller = AppointmentsTabController(self.ui)
        self.doctors_tab_controller = DoctorsTabController(self.ui)
        self.patients_tab_controller = PatientsTabController(self.ui,self.appointments_tab_controller)
        self.services_tab_controller = ServicesTabController(self.ui)
        self.expense_tab_controller = ExpenseTabController(self.ui)
        self.report_controller = ReportsTabController(self.ui)
        
