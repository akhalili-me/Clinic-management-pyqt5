from PyQt5.QtWidgets import QDialog, QFileDialog
from ui import (
    Ui_addEditMedicalRecords_form,
    Ui_medicalRecordInfo_form,
    Ui_medicalRecordImages_form,
    Ui_addEditImage_form,
)
from models import DatabaseManager
from models import MedicalRecords, Services,Patients,MedicalRecordImages
import jdatetime
from PyQt5.QtCore import pyqtSignal
from utility import LoadingValues, Messages, Dates, Numbers, Validators, Images
from PyQt5.QtGui import QPixmap

class MedicalRecordInfoController(QDialog):
    load_user_medical_records_list = pyqtSignal()

    def __init__(self, medical_record_id):
        super(MedicalRecordInfoController, self).__init__()
        self.ui = Ui_medicalRecordInfo_form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.medical_record_id = medical_record_id

        self.load_medical_record_data()
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.deleteMedicalRecord_btn.clicked.connect(self.delete_medical_record)
        self.ui.showPictures_btn.clicked.connect(self.show_medical_record_images)
        self.ui.editMedicalRecord_btn.clicked.connect(self.open_edit_medical_record)

    def delete_medical_record(self):
        msg_box, yes_button = Messages.show_confirm_delete_msg()
        if msg_box.clickedButton() == yes_button:
            with DatabaseManager() as db:
                try:
                    record_images = MedicalRecordImages.get_by_medical_record_id(db,self.medical_record_id)
                    for image in record_images:
                        Images.delete_image(image["path"])

                    MedicalRecords.delete_medical_record(db, self.medical_record_id)
                except Exception as e:
                    Messages.show_error_msg(str(e))
                    return self.close()
                Messages.show_success_msg("خدمات با موفقیت حذف شد.")
                self.close()
                self.load_user_medical_records_list.emit()
        else:
            msg_box.close()

    def open_edit_medical_record(self):
        with DatabaseManager() as db:
            try:
                medical_record = MedicalRecords.get_by_id(db, self.medical_record_id)
            except Exception as e:
                Messages.show_error_msg(str(e))
                return
            
        self.edit_medical_record_controller = AddEditMedicalRecordsController(
            medical_record=medical_record
        )
        self.edit_medical_record_controller.refresh_user_medical_records_list.connect(
            self.load_user_medical_records_list
        )
        self.edit_medical_record_controller.refresh_medical_record_info.connect(
            self.load_medical_record_data
        )
        self.edit_medical_record_controller.show()

    def show_medical_record_images(self):
        with DatabaseManager() as db:
            try:
                medical_record = MedicalRecords.get_by_id(db,self.medical_record_id)
                patient = Patients.get_by_id(db,medical_record["patient"])
            except Exception as e:
                Messages.show_error_msg(str(e))
                return

    
        patient_full_name = f"{patient["firstName"]} {patient["lastName"]}"
        self.medical_record_images_controller = MedicalRecordImagesInfoController(patient_full_name,self.medical_record_id)
        self.medical_record_images_controller.show()

    def load_medical_record_data(self):
        medical_record_id = self.medical_record_id

        with DatabaseManager() as db:
            try:
                medical_record = MedicalRecords.get_by_id(db, medical_record_id)
                patient, service, doctor_full_name = (
                    UtilityFetcher.get_patient_service_doctor_names(
                        db,
                        medical_record["patient"],
                        medical_record["service"],
                        medical_record["doctor"],
                    )
                )
            except Exception as e:
                Messages.show_error_msg(str(e))
                return
     
        jalali_date = Dates.convert_to_jalali_format(medical_record["jalali_date"])
        description = medical_record["description"] or "بدون توضیحات"
        price = Numbers.int_to_persian_with_separators(medical_record["price"])

        self.ui.patientFullName_lbl.setText(patient["fullName"])
        self.ui.serviceName_lbl.setText(service["name"])
        self.ui.doctorName_lbl.setText(f"دکتر {doctor_full_name}")
        self.ui.date_lbl.setText(jalali_date)
        self.ui.description_lbl.setText(description)
        self.ui.price_lbl.setText(f"{price} تومان")


class AddEditMedicalRecordsController(QDialog):
    refresh_user_medical_records_list = pyqtSignal()
    refresh_medical_record_info = pyqtSignal()

    def __init__(self, patient_id=None, medical_record=None):
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
            try:
                _, service, doctor_full_name = (
                UtilityFetcher.get_patient_service_doctor_names(
                    db, None, medical_record["service"], medical_record["doctor"]
                )
                )
            except Exception as e:
                Messages.show_error_msg(str(e))
                return
           

        self.ui.doctor_cmbox.setCurrentText(f"دکتر {doctor_full_name}")
        self.ui.service_cmbox.setCurrentText(service["name"])
        self.ui.description_txtbox.setText(medical_record["description"])
        LoadingValues.load_date_into_date_spinbox(
            self.ui, medical_record["jalali_date"]
        )

    def save_medical_record(self):
        jalali_date_str = self._get_jalali_date().strip()
        greg_date = self._get_gregorian_date(jalali_date_str).strip()

        with DatabaseManager() as db:
            try:
                service_id = self.ui.service_cmbox.currentData()
                selected_service = Services.get_by_id(db, service_id)
                price = selected_service["price"]

                record_data = {
                    "jalali_date": jalali_date_str,
                    "greg_date": greg_date,
                    "doctor": self.ui.doctor_cmbox.currentData(),
                    "service": service_id,
                    "description": self.ui.description_txtbox.toPlainText().strip(),
                    "patient": self.patient_id,
                    "price": price,
                }

                if self.medical_record:
                    record_data["id"] = self.medical_record["id"]
                    MedicalRecords.update_medical_record(db, record_data)
                    success_msg = "خدمات با موفقیت ویرایش شد."
                else:
                    MedicalRecords.add_medical_record(db, record_data)
                    success_msg = "خدمات با موفقیت اضافه شد."

                Messages.show_success_msg(success_msg)
                self.refresh_user_medical_records_list.emit()
                self.refresh_medical_record_info.emit()
                self.close()
            except Exception as e:
                Messages.show_error_msg(str(e))
                return self.close()

    def _get_jalali_date(self):
        year = self.ui.year_spnbox.value()
        month = self.ui.month_spnbox.value()
        day = self.ui.day_spnbox.value()
        return jdatetime.date(year, month, day).strftime("%Y-%m-%d")

    def _get_gregorian_date(self, jalali_date_str):
        year, month, day = map(int, jalali_date_str.split("-"))
        return (
            jdatetime.date(year, month, day)
            .togregorian()
            .strftime("%Y-%m-%d")
        )


class MedicalRecordImagesInfoController(QDialog):

    def __init__(self, patient_name, medical_record_id):
        super().__init__()
        self.ui = Ui_medicalRecordImages_form()
        self.ui.setupUi(self)
        self.setModal(True)

        self.patient_name = patient_name
        self.medical_record_id = medical_record_id
        self.current_image_index = 0
        self.current_image_id = None

        self.load_medical_record_images()
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.addImage_btn.clicked.connect(self.open_add_image)
        self.ui.nextImage_btn.clicked.connect(self.next_image)
        self.ui.deleteImage_btn.clicked.connect(self.delete_image)

    def open_add_image(self):
        self.add_image_controller = AddMedicalRecordImage(self.patient_name, self.medical_record_id)
        self.add_image_controller.refresh_medical_record_images.connect(self.load_medical_record_images)
        self.add_image_controller.show()

    def next_image(self):
        medical_record_images = self._fetch_medical_record_images()
        if not medical_record_images:
            return

        self.current_image_index = (self.current_image_index + 1) % len(medical_record_images)
        self.current_image_id = medical_record_images[self.current_image_index]["id"]
        self._load_image_data_into_label(medical_record_images[self.current_image_index])
        self._enable_disable_buttons(len(medical_record_images))

    def delete_image(self):
        msg_box, yes_button = Messages.show_confirm_delete_msg()
        if msg_box.clickedButton() == yes_button:
            with DatabaseManager() as db:
                try:
                    current_image = MedicalRecordImages.get_by_id(db, self.current_image_id)
                    MedicalRecordImages.delete_medical_record_image(db, self.current_image_id)
                    Images.delete_image(current_image["path"])
                except Exception as e:
                    Messages.show_error_msg(str(e))
                    return
                Messages.show_success_msg("تصویر با موفقیت حذف شد.")
                self.load_medical_record_images()
        else:
            msg_box.close()

    def load_medical_record_images(self):
        medical_record_images = self._fetch_medical_record_images()

        if not medical_record_images:
            self._update_ui_no_images()
            return

        self.current_image_index = 0
        self.current_image_id = medical_record_images[0]["id"]
        self._load_image_data_into_label(medical_record_images[0])
        image_count = Numbers.english_to_persian_numbers(str(len(medical_record_images)))
        self.ui.imageCount_lbl.setText(image_count)
        self._enable_disable_buttons(len(medical_record_images))

    def _fetch_medical_record_images(self):
        with DatabaseManager() as db:
            try:
                return MedicalRecordImages.get_by_medical_record_id(db, self.medical_record_id)
            except Exception as e:
                Messages.show_error_msg(str(e))
                return
                
            

    def _load_image_data_into_label(self, image):
        image_pix_map = QPixmap(image["path"])
        self.ui.image_lbl.setPixmap(image_pix_map)
        self.ui.imageName_txtbox.setText(image["name"])

    def _update_ui_no_images(self):
        default_image_path = Images.get_default_image_path()
        default_image = {
            "name": "بدون تصویر",
            "path": str(default_image_path)
        }

        self._load_image_data_into_label(default_image)
        self.ui.imageCount_lbl.setText("۰")
        self._enable_disable_buttons(0)

    def _enable_disable_buttons(self, image_count):
        is_image_available = image_count > 0
        is_multiple_images = image_count > 1

        self.ui.deleteImage_btn.setVisible(is_image_available)
        self.ui.nextImage_btn.setVisible(is_multiple_images)
       

class AddMedicalRecordImage(QDialog):
    refresh_medical_record_images = pyqtSignal()

    def __init__(self, patient_name,medical_record_id):
        super(AddMedicalRecordImage, self).__init__()
        self.ui = Ui_addEditImage_form()
        self.ui.setupUi(self)
        self.setModal(True)

        self.patient_name = patient_name
        self.medical_record_id = medical_record_id
        self.selected_image_path = ""
        self.saved_image_path = ""

        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.chooseImage_btn.clicked.connect(self.open_file_dialog)
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.save_btn.clicked.connect(self.validate_form)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)", options=options)
        if file_name:
            self.selected_image_path = file_name
            self.ui.imagePath_txtbox.setText(self.selected_image_path)

    def validate_form(self):
        name_txtbox = self.ui.imageName_txtbox.text()

        txtboxes = [
            {"text": name_txtbox, "name": "نام تصویر"},
            {"text": self.selected_image_path, "name": "تصویر انتخاب شده"},
        ]

        if Validators.validate_empty_txt_boxes(txtboxes):
            self.save_image()

    def save_image(self):
        try:
            image_directory = Images.create_image_directory_if_not_exist(self.patient_name)
            self.saved_image_path = Images.save_image_to_new_directory(self.selected_image_path,image_directory)
        except Exception as e:
            Messages.show_error_msg(str(e))
            return self.close()
            
        
        self.save_image_into_database()

    def save_image_into_database(self):
        image_info = {
            "name": self.ui.imageName_txtbox.text().strip(),
            "path": self.saved_image_path,
            "medical_record": self.medical_record_id
        }
        
        with DatabaseManager() as db:
            try:
                MedicalRecordImages.add_medical_record_image(db,image_info)
            except Exception as e:
                Messages.show_error_msg(str(e))
                return

        Messages.show_success_msg("تصویر با موفقیت اضافه شد")
        self.refresh_medical_record_images.emit()
        self.close()
        

