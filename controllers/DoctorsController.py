# controllers/add_patient_controller.py
from PyQt5.QtWidgets import QDialog
from ui import Ui_addEditDeleteDoctor_form,Ui_MainWindow
from models.db import DatabaseManager,DatabaseWorker
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSignal
from models.Doctors import Doctors
from PyQt5.QtWidgets import QListWidgetItem
from utility import Messages,BaseController

class DoctorsTabController(BaseController):
    def __init__(self, ui:Ui_MainWindow):
        self.ui = ui
        self.active_workers = []
        self.load_doctors_list()
        self.ui.addDoctor_btn.clicked.connect(self.open_add_doctor)
        self.ui.doctors_lst.itemDoubleClicked.connect(self.open_edit_delete_doctor)

    def open_edit_delete_doctor(self,item):
        doctor_id = item.data(1)
        self.edit_delete_doctor_controller = AddEditDeleteDoctorController(doctor_id)
        self.edit_delete_doctor_controller.refresh_doctors_list.connect(self.load_doctors_list)
        self.edit_delete_doctor_controller.show()

    def open_add_doctor(self):
        self.add_doctor_controller = AddEditDeleteDoctorController()
        self.add_doctor_controller.refresh_doctors_list.connect(self.load_doctors_list)
        self.add_doctor_controller.show()

    def load_doctors_list(self):
        self._start_worker(Doctors.get_all, [], self.display_doctors_list)

    def display_doctors_list(self,doctors):
        self.ui.doctors_lst.clear()
        for doctor in doctors:
            full_name = f"{doctor['firstName']} {doctor['lastName']}"
            item_txt = f"دکتر {full_name} | {doctor['specialization']}"
            item = QListWidgetItem(item_txt)
            item.setData(1, doctor['id'])
            self.ui.doctors_lst.addItem(item)


class AddEditDeleteDoctorController(BaseController,QDialog):
    refresh_doctors_list = pyqtSignal()

    def __init__(self, doctor_id=None):
        super(AddEditDeleteDoctorController, self).__init__()
        self.ui = Ui_addEditDeleteDoctor_form()
        self.ui.setupUi(self)
        self.setModal(True)
        self._setup_validators()
        self.active_workers = []

        # Check if it's a edit window
        self.doctor_id = doctor_id
        if doctor_id:
            self.load_doctor_data()
        else:
            self.ui.deleteDoctor_btn.hide()

        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.save_btn.clicked.connect(self.save_doctor)
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.deleteDoctor_btn.clicked.connect(self.delete_doctor)

    def _setup_validators(self):
        self.ui.firstName_txtbox.setMaxLength(50)
        self.ui.lastName_txtbox.setMaxLength(50)
        self.ui.specialization_txtbox.setMaxLength(50)

    def load_doctor_data(self):
        self._start_worker(Doctors.get_by_id, [self.doctor_id], self.display_doctor_data)

    def display_doctor_data(self,doctor):
        self.ui.firstName_txtbox.setText(doctor["firstName"])
        self.ui.lastName_txtbox.setText(doctor["lastName"])
        self.ui.specialization_txtbox.setText(doctor["specialization"])

    def save_doctor(self):
        doctor_data = {
            'firstName': self.ui.firstName_txtbox.text().strip(),
            'lastName': self.ui.lastName_txtbox.text().strip(),
            "specialization": self.ui.specialization_txtbox.text().strip(),
        }

        if self.doctor_id:
            doctor_data['id'] = self.doctor_id
            self.update_doctor(doctor_data)
        else:
            self.add_doctor(doctor_data)

    def delete_doctor(self):
        msg_box, yes_button = Messages.show_confirm_delete_msg()
        if msg_box.clickedButton() != yes_button:
            msg_box.close()
            return

        self._start_worker(
            Doctors.delete_doctor,
            [self.doctor_id],
            success_callback=lambda: self.operation_successful(
                "پزشک با موفقیت حذف شد."
            ),
        )

    def add_doctor(self, doctor):
        self._start_worker(
            Doctors.add_doctor,
            [doctor],
            success_callback=lambda: self.operation_successful(
                "پزشک با موفقیت اضافه شد."
            ),
        )

    def update_doctor(self,doctor):
        self._start_worker(
            Doctors.update_doctor,
            [doctor],
            success_callback=lambda: self.operation_successful(
                "پزشک با موفقیت ویرایش شد."
            ),
        )

    def operation_successful(self,success_msg):
        Messages.show_success_msg(success_msg)
        self.refresh_doctors_list.emit()
        self.close()
