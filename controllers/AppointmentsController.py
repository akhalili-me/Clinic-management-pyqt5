from PyQt5.QtWidgets import QDialog
from ui import Ui_addEditAppointment_form
from models.db import DatabaseManager
from PyQt5.QtWidgets import QMessageBox
from models import Doctors,Services,Appointments
from jdatetime import date
from PyQt5.QtCore import pyqtSignal

class AddEditAppointmentController(QDialog):
    refresh_appointment_list = pyqtSignal()

    def __init__(self,patient_id):
        super(AddEditAppointmentController, self).__init__()
        self.ui = Ui_addEditAppointment_form()
        self.ui.setupUi(self)
        self.setModal(True)

        self.patient_id = patient_id

        self._load_combo_box_valoues()
        self._load_spin_box_values()

        self.ui.save_btn.clicked.connect(self.save_appointment)
        self.ui.cancel_btn.clicked.connect(self.close)

    def _load_combo_box_valoues(self):
        with DatabaseManager() as db:
            self.ui.doctor_cmbox.clear()
            doctors =  Doctors.get_all(db)
            for doctor in doctors:
                full_name = f"{doctor["firstName"]} {doctor["lastName"]}"
                self.ui.doctor_cmbox.addItem(f"دکتر {full_name}", doctor["id"])

            self.ui.service_cmbox.clear()
            services = Services.get_all(db)
            for service in services:
                self.ui.service_cmbox.addItem(service["name"],service["id"])

    def _load_spin_box_values(self):
        current_date = date.today()
        self.ui.year_spnbox.setValue(current_date.year)
        self.ui.month_spnbox.setValue(current_date.month)
        self.ui.day_spnbox.setValue(current_date.day)
     

    def save_appointment(self):
        year = self.ui.year_spnbox.value()
        month = self.ui.month_spnbox.value()
        day = self.ui.day_spnbox.value()
        date_str = f"{year}-{month}-{day}"

        hour = self.ui.hour_spnbox.value()
        minute = self.ui.minute_spnbox.value()
        time_str = f"{hour}:{minute}"

        appointment = {
            'status': self.ui.status_cmbox.currentText().strip(),
            'date': date_str.strip(),
            "time": time_str.strip(),
            "doctor": self.ui.doctor_cmbox.currentData(),
            "service": self.ui.service_cmbox.currentData(),
            "description": self.ui.description_txtbox.toPlainText().strip(),
            "patient": self.patient_id,
        }

        print(appointment)
        with DatabaseManager() as db:
            Appointments.add_appointment(db,appointment)
            QMessageBox.information(self, "موفقیت", "نوبت با موفقیت اضافه شد.")
            self.refresh_appointment_list.emit()
            self.close()



