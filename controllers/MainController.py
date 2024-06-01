from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow


from controllers import (
    DoctorsTabController,
    PatientsTabController,
    ServicesTabController,
    AppointmentsTabController
)

class MainController(QMainWindow):
    def __init__(self):
        super(MainController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        #Initilize tabs
        self.doctors_tab_controller = DoctorsTabController(self.ui)
        self.patients_tab_controller = PatientsTabController(self.ui)
        self.services_tab_controller = ServicesTabController(self.ui)
        self.appointments_tab_controller = AppointmentsTabController(self.ui)
