from PyQt5.QtWidgets import QDialog
from ui import Ui_addEditMedicalRecords_form
from models.db import DatabaseManager
from PyQt5.QtWidgets import QMessageBox
from models import MedicalRecords
import jdatetime
from PyQt5.QtCore import pyqtSignal
from utility import LoadingValues

class AddEditMedicalRecordsController(QDialog):
    refresh_medical_records_list = pyqtSignal()

    def __init__(self,patient_id):
        super(AddEditMedicalRecordsController, self).__init__()
        self.ui = Ui_addEditMedicalRecords_form()
        self.ui.setupUi(self)
        self.setModal(True)

        self.patient_id = patient_id

        LoadingValues.load_date_spin_box_values(self.ui)
        LoadingValues.load_doctors_services_combo_boxes(self.ui)

        self.ui.save_btn.clicked.connect(self.save_medical_record)
        self.ui.cancel_btn.clicked.connect(self.close)

    def save_medical_record(self):
        year = self.ui.year_spnbox.value()
        month = self.ui.month_spnbox.value()
        day = self.ui.day_spnbox.value()
        jalali_date_obj = jdatetime.date(year,month,day)
        jalali_date_str = jalali_date_obj.strftime("%Y-%m-%d")
        greg_date = jalali_date_obj.togregorian().strftime('%Y-%m-%d')

        record = {
            'jalali_date': jalali_date_str.strip(),
            'greg_date': greg_date.strip(),
            "doctor": self.ui.doctor_cmbox.currentData(),
            "service": self.ui.service_cmbox.currentData(),
            "description": self.ui.description_txtbox.toPlainText().strip(),
            "patient": self.patient_id,
        }

        # print(record)
        with DatabaseManager() as db:
            MedicalRecords.add_medical_record(db,record)
            QMessageBox.information(self, "موفقیت", "خدمات با موفقیت اضافه شد.")
            self.refresh_medical_records_list.emit()
            self.close()





         
