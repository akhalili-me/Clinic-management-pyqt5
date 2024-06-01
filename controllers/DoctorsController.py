# controllers/add_patient_controller.py
from PyQt5.QtWidgets import QDialog
from ui import Ui_addEditDeleteDoctor_form,Ui_MainWindow
from models.db import DatabaseManager
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSignal
from models.Doctors import Doctors
from PyQt5.QtWidgets import QListWidgetItem
from utility import Messages

class DoctorsTabController:
    def __init__(self, ui:Ui_MainWindow):
        self.ui = ui
        self._load_doctors_list()
        self.ui.addDoctor_btn.clicked.connect(self.open_add_doctor)
        self.ui.doctors_lst.itemDoubleClicked.connect(self.open_edit_delete_doctor)

    def open_edit_delete_doctor(self,item):
        doctor_id = item.data(1)
        with DatabaseManager() as db:
            doctor = Doctors.get_by_id(db,doctor_id)
        self.edit_delete_doctor_controller = AddEditDeleteDoctorController(doctor)
        self.edit_delete_doctor_controller.refresh_doctors_list.connect(self._load_doctors_list)
        self.edit_delete_doctor_controller.show()

    def open_add_doctor(self):
        self.add_doctor_controller = AddEditDeleteDoctorController()
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



class AddEditDeleteDoctorController(QDialog):
    refresh_doctors_list = pyqtSignal()

    def __init__(self, doctor=None):
        super(AddEditDeleteDoctorController, self).__init__()
        self.ui = Ui_addEditDeleteDoctor_form()
        self.ui.setupUi(self)
        self.setModal(True)

        #Check if it's a edit window
        self.doctor = doctor
        if doctor:
            self.load_doctor_data_into_txtboxes()
            self.ui.title_lbl.setText("ویرایش پزشک")
        else:
            self.ui.deleteDoctor_btn.hide()

        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.save_btn.clicked.connect(self.save_doctor)
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.deleteDoctor_btn.clicked.connect(self.delete_doctor)

    def load_doctor_data_into_txtboxes(self):
        self.ui.firstName_txtbox.setText(self.doctor["firstName"])
        self.ui.lastName_txtbox.setText(self.doctor["lastName"])
        self.ui.specialization_txtbox.setText(self.doctor["specialization"])

    def save_doctor(self):
        doctor_data = {
            'firstName': self.ui.firstName_txtbox.text().strip(),
            'lastName': self.ui.lastName_txtbox.text().strip(),
            "specialization": self.ui.specialization_txtbox.text().strip(),
        }

        with DatabaseManager() as db:
            if self.doctor:
                doctor_data['id'] = self.doctor["id"]
                Doctors.update_doctor(db, doctor_data)
                success_message = "پزشک با موفقیت ویرایش شد."
            else:
                Doctors.add_doctor(db, doctor_data)
                success_message = "پزشک با موفقیت اضافه شد."

            QMessageBox.information(self, "موفقیت", success_message)
            self.refresh_doctors_list.emit()
            self.close()


    def delete_doctor(self):
        msg_box, yes_button = Messages.show_confirm_delete_msg()
        if msg_box.clickedButton() == yes_button:
            with DatabaseManager() as db:
                Doctors.delete_doctor(db,self.doctor["id"])
                Messages.show_success_msg("پزشک با موفقیت حذف شد.")
                self.close()
                self.refresh_doctors_list.emit()
        else:
            msg_box.close()