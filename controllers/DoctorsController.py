# controllers/add_patient_controller.py
from PyQt5.QtWidgets import QDialog
from ui import Ui_addEditDoctor_form
from models.db import DatabaseManager
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSignal
from models.Doctors import Doctors
from PyQt5.QtWidgets import QListWidgetItem

class DoctorsTabController:
    def __init__(self, ui):
        self.ui = ui
        self._load_doctors_list()
        self.ui.addDoctor_btn.clicked.connect(self.open_add_doctor)

    def open_add_doctor(self):
        from controllers.DoctorsController import AddDoctorController
        self.add_doctor_controller = AddDoctorController()
        self.add_doctor_controller.refresh_doctors_list.connect(self._load_doctors_list)
        self.add_doctor_controller.show()

    def _load_doctors_list(self):
        self.ui.doctors_lst.clear()
        with DatabaseManager() as db:
            all_doctors = Doctors.get_all(db)
            for doctor in all_doctors:
                full_name = f"{doctor['firstName']} {doctor['lastName']}"
                item_txt = f"دکتر {full_name} | {doctor['specialization']}"
                item = QListWidgetItem(item_txt)
                item.setData(1, doctor['id'])
                self.ui.doctors_lst.addItem(item)



class AddDoctorController(QDialog):
    refresh_doctors_list = pyqtSignal()

    def __init__(self):
        super(AddDoctorController, self).__init__()
        self.ui = Ui_addEditDoctor_form()
        self.ui.setupUi(self)

        self.setModal(True)

        # Connecting the buttons 
        self.ui.save_btn.clicked.connect(self.save_patient)
        self.ui.cancel_btn.clicked.connect(self.close)

    def save_patient(self):
        doctor = {
            'firstName': self.ui.firstName_txtbox.text(),
            'lastName': self.ui.lastName_txtbox.text(),
            "specialization": self.ui.specialization_txtbox.text(),
        }

        with DatabaseManager() as db:
            Doctors.add_doctor(db,doctor)
            QMessageBox.information(self, "موفقیت", "پزشک با موفقیت اضافه شد.")
            self.refresh_doctors_list.emit()
            self.close()



