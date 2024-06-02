from PyQt5.QtWidgets import QDialog
from ui import Ui_addEditMedicalRecords_form,Ui_medicalRecordInfo_form
from models import DatabaseManager,UtilityFetcher
from PyQt5.QtWidgets import QMessageBox
from models import MedicalRecords
import jdatetime
from PyQt5.QtCore import pyqtSignal
from utility import LoadingValues,Messages,Dates,Numbers

class MedicalRecordInfoController(QDialog):
    load_user_medical_records_list = pyqtSignal()

    def __init__(self,medical_record_id):
        super(MedicalRecordInfoController, self).__init__()
        self.ui = Ui_medicalRecordInfo_form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.medical_record_id = medical_record_id

        self.load_medical_record_data()
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.deleteMedicalRecord_btn.clicked.connect(self.delete_medical_record)
        self.ui.showPictures_btn.clicked.connect(self.show_medical_record_pictures)
        self.ui.editMedicalRecord_btn.clicked.connect(self.open_edit_medical_record)

    def delete_medical_record(self):
        msg_box, yes_button = Messages.show_confirm_delete_msg()
        if msg_box.clickedButton() == yes_button:
            with DatabaseManager() as db:
                MedicalRecords.delete_medical_record(db,self.medical_record_id)
                Messages.show_success_msg("خدمات با موفقیت حذف شد.")
                self.close()
                self.load_user_medical_records_list.emit()
        else:
            msg_box.close()

    def open_edit_medical_record(self):
        with DatabaseManager() as db:
            medical_record = MedicalRecords.get_by_id(db,self.medical_record_id)
        self.edit_medical_record_controller = AddEditMedicalRecordsController(medical_record=medical_record)
        self.edit_medical_record_controller.refresh_user_medical_records_list.connect(self.load_user_medical_records_list)
        self.edit_medical_record_controller.show()
   
    
    def show_medical_record_pictures(self):
        pass

    def load_medical_record_data(self):
        medical_record_id = self.medical_record_id

        with DatabaseManager() as db:
            medical_record = MedicalRecords.get_by_id(db,medical_record_id)
            patient, service_name, doctor_full_name = (
                UtilityFetcher.get_patient_service_doctor_names(
                    db,
                    medical_record["patient"],
                    medical_record["service"],
                    medical_record["doctor"],
                )
            )

        jalali_date = Dates.convert_to_jalali_format(medical_record["jalali_date"])
        description = medical_record["description"] or "بدون توضیحات"
        price = Numbers.int_to_persian_with_separators(medical_record["price"])

        self.ui.patientFullName_lbl.setText(patient["fullName"])
        self.ui.serviceName_lbl.setText(service_name)
        self.ui.doctorName_lbl.setText(f"دکتر {doctor_full_name}")
        self.ui.date_lbl.setText(jalali_date)
        self.ui.description_lbl.setText(description)
        self.ui.price_lbl.setText(f"{price} تومان")


class AddEditMedicalRecordsController(QDialog):
    refresh_user_medical_records_list = pyqtSignal()

    def __init__(self,patient_id=None,medical_record=None):
        super(AddEditMedicalRecordsController, self).__init__()
        self.ui = Ui_addEditMedicalRecords_form()
        self.ui.setupUi(self)
        self.setModal(True)

        self.patient_id = patient_id
        self.medical_record = medical_record
        self._load_initial_values()

        if medical_record:
            self.patient_id = medical_record["patient"]
            self.ui.title_lbl.setText("ویرایش خدمات")
            self.load_record_data_into_txtboxes()
        
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.save_btn.clicked.connect(self.save_medical_record)
        self.ui.cancel_btn.clicked.connect(self.close)

    def _load_initial_values(self):
        LoadingValues.load_doctors_services_combo_boxes(self.ui)
        LoadingValues.load_current_date_spin_box_values(self.ui)

    def load_record_data_into_txtboxes(self):
        medical_record = self.medical_record
        with DatabaseManager() as db:
            _, service_name, doctor_full_name = UtilityFetcher.get_patient_service_doctor_names(
                db, None, medical_record["service"], medical_record["doctor"]
            )

        self.ui.doctor_cmbox.setCurrentText(f"دکتر {doctor_full_name}")
        self.ui.service_cmbox.setCurrentText(service_name)
        self.ui.description_txtbox.setText(medical_record["description"])

        LoadingValues.load_date_into_date_spinbox(self.ui, medical_record["jalali_date"])

    def save_medical_record(self):
        jalali_date_str = self._get_jalali_date()
        greg_date = self._get_gregorian_date()

        record_data = {
            'jalali_date': jalali_date_str.strip(),
            'greg_date': greg_date.strip(),
            "doctor": self.ui.doctor_cmbox.currentData(),
            "service": self.ui.service_cmbox.currentData(),
            "description": self.ui.description_txtbox.toPlainText().strip(),
            "patient": self.patient_id,
        }

        
        with DatabaseManager() as db:

            if self.medical_record:
                record_data["id"] = self.medical_record["id"]
                MedicalRecords.update_medical_record(db, record_data)
                success_msg = "خدمات با موفقیت ویرایش شد."
            else:
                MedicalRecords.add_medical_record(db, record_data)
                success_msg = "خدمات با موفقیت اضافه شد."

            Messages.show_success_msg(success_msg)
            self.refresh_user_medical_records_list.emit()
            self.close()

    def _get_jalali_date(self):
        year = self.ui.year_spnbox.value()
        month = self.ui.month_spnbox.value()
        day = self.ui.day_spnbox.value()
        return jdatetime.date(year, month, day).strftime("%Y-%m-%d")

    def _get_time_str(self):
        hour = self.ui.hour_spnbox.value()
        minute = self.ui.minute_spnbox.value()
        return f"{hour}:{minute}"

    def _get_gregorian_date(self, jalali_date_str):
        year, month, day = map(int, jalali_date_str.split('-'))
        return jdatetime.datetime(year, month, day).togregorian().strftime('%Y-%m-%d %H:%M')



         
