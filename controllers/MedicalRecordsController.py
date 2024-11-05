from PyQt5.QtWidgets import QDialog, QFileDialog,QListWidgetItem
from ui import get_ui_class
from models import MedicalRecords,MedicalRecordImages
import jdatetime
from PyQt5.QtCore import pyqtSignal
from utility import (
    Messages,
    Dates,
    Numbers,
    Validators,
    Images,
    BaseController,
    LoadSpinBox,
    LoadComboBox,
)
from PyQt5.QtGui import QPixmap,QDesktopServices
from PyQt5.QtCore import Qt, QUrl
import logging


class MedicalRecordsTabController(BaseController):
    def __init__(self, ui, dispatcher):
        self.ui = ui
        self.active_workers = []
        self.dispatcher = dispatcher
        self.dispatcher.load_today_medical_records_list.connect(
            self.load_today_medical_records_list
        )
        self.load_today_medical_records_list()
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.medicalRecords_list.itemDoubleClicked.connect(
            self.open_medical_record_info
        )
        self.ui.medicalRecordsSearchByDate_btn.clicked.connect(self.search_medical_records)
        self.ui.refreshMedicalRecordsList_btn.clicked.connect(self.refresh_medical_records_list)

    def refresh_medical_records_list(self):
        self.load_today_medical_records_list()

    def search_medical_records(self):
        selected_date = self.get_selected_jalali_date()
        self.load_medical_records_list_by_date(selected_date)

    def open_medical_record_info(self, item):
        medical_record_id = item.data(1)
        self.medical_record_info_controller = MedicalRecordInfoController(
            medical_record_id, self.dispatcher
        )
        self.medical_record_info_controller.load_today_medical_records_list.connect(
            self.load_today_medical_records_list
        )
        self.medical_record_info_controller.show()

    def load_today_medical_records_list(self):
        self.set_current_date_into_medical_records_spinboxes()
        today_date = jdatetime.date.today().strftime("%Y-%m-%d")
        self.load_medical_records_list_by_date(today_date)

    def load_medical_records_list_by_date(self,date):
        self._start_worker(
            MedicalRecords.get_by_date, [date], self.display_medical_records_data
        )

    def set_current_date_into_medical_records_spinboxes(self):
        medica_record_date_spnbox_names = {
            "year": "medicalRecordsYear_spnbox",
            "month": "medicalRecordsMonth_spnbox",
            "day": "medicalRecordsDay_spnbox",
        }
        LoadSpinBox.set_current_date_into_date_spin_boxes(
            self.ui, medica_record_date_spnbox_names
        )

    def display_medical_records_data(self, medical_records):
        self.ui.medicalRecords_list.clear()
        for medical_record in medical_records:
            persian_price = Numbers.int_to_persian_with_separators(medical_record["price"])
            persian_date_format = Dates.convert_to_jalali_format(medical_record["jalali_date"])
            item_txt = f"{medical_record['patient_name']} | {medical_record["service_name"]} | دکتر {medical_record["doctor_lastname"]} | {persian_date_format} | قیمت: {persian_price} تومان "
            item = QListWidgetItem(item_txt)
            item.setData(1, medical_record["id"])
            self.ui.medicalRecords_list.addItem(item)

    def get_selected_jalali_date(self):
        selected_year = str(self.ui.medicalRecordsYear_spnbox.value())
        selected_month = f"{self.ui.medicalRecordsMonth_spnbox.value():02}"
        selected_day = f"{self.ui.medicalRecordsDay_spnbox.value():02}"
        return f"{selected_year}-{selected_month}-{selected_day}"

class MedicalRecordInfoController(BaseController,QDialog):
    load_user_medical_records_list = pyqtSignal()
    load_today_medical_records_list = pyqtSignal()

    def __init__(self, medical_record_id, dispatcher):
        super(MedicalRecordInfoController, self).__init__()
        self.ui = get_ui_class("iMedicalRecord")()
        self.ui.setupUi(self)
        self.active_workers = []
        self.dispatcher = dispatcher
        self.setModal(True)
        self.medical_record_id = medical_record_id
        self.medical_record_images = None
        self.current_image_id = None
        self.current_image_index = 0
        self.load_all_medical_record_data()
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.deleteMedicalRecord_btn.clicked.connect(self.open_delete_medical_record)
        self.ui.editMedicalRecord_btn.clicked.connect(self.open_edit_medical_record)
        self.ui.addImage_btn.clicked.connect(self.open_add_image)
        self.ui.nextImage_btn.clicked.connect(self.next_image)
        self.ui.deleteImage_btn.clicked.connect(self.open_delete_image)
        self.ui.viewImage_btn.clicked.connect(self.view_image_full_size)

    def view_image_full_size(self):
        relative_image_path = self._get_image_path_by_id(self.current_image_id)
        current_image_abs_path = Images.get_media_directory() / relative_image_path
        QDesktopServices.openUrl(QUrl.fromLocalFile(str(current_image_abs_path)))

    def open_delete_medical_record(self):
        msg_box, yes_button = Messages.show_confirm_delete_msg()
        if msg_box.clickedButton() != yes_button:
            msg_box.close()
            return

        self._start_worker(
            MedicalRecordImages.get_all_image_paths_by_medical_record_id,
            [self.medical_record_id],
            self.handle_medical_record_delete,
        )

    def handle_medical_record_delete(self,medical_record_images):
        for image in medical_record_images:
            Images.delete_image(image["path"])

        self._start_worker(
            MedicalRecords.delete_medical_record,
            [self.medical_record_id],
            success_callback=lambda: self.operation_successful(
                "خدمات با موفقیت حذف شد."
            ),
        )

    def operation_successful(self, success_msg, delete_operation=False):
        Messages.show_success_msg(success_msg)
        self.load_user_medical_records_list.emit()
        self._get_medical_record_images()
        self.dispatcher.refresh_main_tab_reports.emit()
        if not delete_operation:
            self.close()

    def open_edit_medical_record(self):
        self.edit_medical_record_controller = AddEditMedicalRecordsController(
            self.dispatcher, medical_record_id=self.medical_record_id
        )
        self.edit_medical_record_controller.refresh_medical_record_info.connect(
            self.load_all_medical_record_data
        )
        self.edit_medical_record_controller.show()

    def open_add_image(self):
        self.add_image_controller = AddMedicalRecordImage(self.medical_record_id)
        self.add_image_controller.refresh_medical_record_images.connect(self._get_medical_record_images)
        self.add_image_controller.show()

    def load_all_medical_record_data(self):
        self._start_worker(
            MedicalRecords.get_by_id,
            [self.medical_record_id],
            result_callback=self.display_medical_record_data,
        )
        self._get_medical_record_images()

    def _get_medical_record_images(self):
        self._start_worker(
            MedicalRecordImages.get_details_by_medical_record_id,
            [self.medical_record_id],
            self.handle_medical_record_images_data,
        )

    def display_medical_record_images(self, medical_record_images):
        if not medical_record_images:
            self._update_ui_no_images()
            return
        self.current_image_index = 0
        self.current_image_id = medical_record_images[0]["id"]
        self.set_image_into_label(medical_record_images[0])
        image_count = Numbers.english_to_persian_numbers(str(len(medical_record_images)))
        self.ui.imageCount_lbl.setText(image_count)
        self._enable_disable_image_buttons(len(medical_record_images))

    def display_medical_record_data(self,medical_record):
        if medical_record:
            jalali_date = Dates.convert_to_jalali_format(medical_record["jalali_date"])
            description = medical_record["description"] or "بدون توضیحات"
            price = Numbers.int_to_persian_with_separators(medical_record["price"])

            self.ui.patientFullName_lbl.setText(medical_record["patient_name"])
            self.ui.serviceName_lbl.setText(medical_record["service_name"])
            self.ui.doctorName_lbl.setText(f"دکتر {medical_record["doctor_name"]}")
            self.ui.date_lbl.setText(jalali_date)
            self.ui.description_lbl.setText(description)
            self.ui.price_lbl.setText(f"{price} تومان")

    def handle_medical_record_images_data(self,medical_record_images):
        self.display_medical_record_images(medical_record_images)
        self.medical_record_images = medical_record_images

    def _update_ui_no_images(self):
        default_image_path = Images.get_default_image_path()
        default_image = {
            "name": "بدون تصویر",
            "path": str(default_image_path)
        }

        self.set_image_into_label(default_image)
        self.ui.imageCount_lbl.setText("۰")
        self._enable_disable_image_buttons(0)

    def _enable_disable_image_buttons(self, image_count):
        is_image_available = image_count > 0
        is_multiple_images = image_count > 1

        self.ui.deleteImage_btn.setEnabled(is_image_available)
        self.ui.nextImage_btn.setEnabled(is_multiple_images)
        self.ui.viewImage_btn.setEnabled(is_image_available)

    def set_image_into_label(self, image):
        media_dir = Images.get_media_directory()
        image_pix_map = QPixmap(str(media_dir / image["path"]))
        scaled_pix_map = image_pix_map.scaled(
            self.ui.image_lbl.size(),
            Qt.KeepAspectRatio,  # Maintain aspect ratio
            Qt.SmoothTransformation,  # Smooth scaling
        )
        self.ui.image_lbl.setPixmap(scaled_pix_map)
        self.ui.imageName_lbl.setText(image["name"])

    def open_delete_image(self):
        msg_box, yes_button = Messages.show_confirm_delete_msg()
        if msg_box.clickedButton() != yes_button:
            msg_box.close()
            return

        self.handle_delete_image()

    def handle_delete_image(self):
        relative_image_path = self._get_image_path_by_id(self.current_image_id)
        abs_image_dir = Images.get_media_directory() / relative_image_path
        Images.delete_image(abs_image_dir)
        self.delete_current_medical_record_image()

    def _get_image_path_by_id(self,image_id):
        id_to_image_path = {
            item["id"]: item["path"] for item in self.medical_record_images
        }
        return id_to_image_path.get(image_id,None)

    def delete_current_medical_record_image(self):
        self._start_worker(
            MedicalRecordImages.delete_medical_record_image,
            [self.current_image_id],
            success_callback=lambda: self.operation_successful(
                "تصویر با موفقیت حذف شد.", True
            ),
        )

    def next_image(self):
        medical_record_images = self.medical_record_images
        if not medical_record_images:
            return

        self.current_image_index = (self.current_image_index + 1) % len(medical_record_images)
        self.current_image_id = medical_record_images[self.current_image_index]["id"]
        self.set_image_into_label(medical_record_images[self.current_image_index])
        self._enable_disable_image_buttons(len(medical_record_images))

class AddEditMedicalRecordsController(BaseController,QDialog):
    refresh_medical_record_info = pyqtSignal()

    def __init__(self, dispatcher, patient_id=None, medical_record_id=None):
        super(AddEditMedicalRecordsController, self).__init__()
        self.ui = get_ui_class("aeMedicalRecord")()
        self.ui.setupUi(self)
        self.setModal(True)
        self.dispatcher = dispatcher
        self.active_workers = []
        self.patient_id = patient_id
        self.medical_record_id = medical_record_id
        self._initialize_ui()

    def _setup_validators(self):
        self.ui.description_txtbox.textChanged.connect(
            lambda: Validators.limit_text_edit(self.ui.description_txtbox)
        )

    def _initialize_ui(self):
        self._setup_validators()
        self._load_initial_values()
        self._handle_edit_mode()
        self._connect_buttons()

    def _handle_edit_mode(self):
        if self.medical_record_id:
            self.load_medical_record_data()
            self.ui.save_btn.setText("ویرایش")

    def _connect_buttons(self):
        self.ui.save_btn.clicked.connect(self.validate_medical_record)
        self.ui.cancel_btn.clicked.connect(self.close)

    def _load_initial_values(self):
        self.combo_box_loader = LoadComboBox(self.ui,self._start_worker)
        self.combo_box_loader.load_doctors_services_combo_boxes()
        LoadSpinBox.set_current_date_into_date_spin_boxes(self.ui)

    def load_medical_record_data(self):
        self._start_worker(
            MedicalRecords.get_details_by_id,
            [self.medical_record_id],
            self.handle_medical_record_data,
        )

    def handle_medical_record_data(self,medical_record):
        self.display_medical_record_data(medical_record)
        self.patient_id = medical_record["patient"]

    def display_medical_record_data(self,medical_record):
        self.ui.doctor_cmbox.setCurrentText(f"دکتر {medical_record["doctor_name"]}")
        self.ui.service_cmbox.setCurrentText(medical_record["service_name"])
        self.ui.description_txtbox.setText(medical_record["description"])
        LoadSpinBox.load_date_into_date_spinboxes(
            self.ui, medical_record["jalali_date"]
        )

    def validate_medical_record(self):
        try:
            self._get_jalali_date()
        except Exception as e:
            warning_message = f"""
            تاریخ انتخاب شده وجود ندارد. 
            {str(e)}
            """
            Messages.show_warning_msg(warning_message)
            return

        self.save_medical_record()

    def save_medical_record(self):
        medical_record = self._collect_medical_record_data()

        if self.medical_record_id:
            self.update_medical_record(medical_record)
        else:
            self.add_medical_record(medical_record)

    def _collect_medical_record_data(self):
        jalali_date_str = self._get_jalali_date()
        greg_date = self._get_gregorian_date(jalali_date_str)

        selected_service_id = self.ui.service_cmbox.currentData()
        selected_service_price = self.ui.service_cmbox.itemData(
            self.ui.service_cmbox.currentIndex(), Qt.UserRole + 1
        )

        medical_record = {
            "jalali_date": jalali_date_str,
            "greg_date": greg_date,
            "doctor": self.ui.doctor_cmbox.currentData(),
            "service": selected_service_id,
            "price": selected_service_price,
            "description": self.ui.description_txtbox.toPlainText().strip(),
            "patient": self.patient_id,
        }

        if self.medical_record_id:
            medical_record["id"] = self.medical_record_id
            if selected_service_id == medical_record["service"]:
                medical_record.pop("price", None)

        return medical_record

    def add_medical_record(self,medical_record):
        self._start_worker(
            MedicalRecords.add_medical_record,
            [medical_record],
            success_callback=lambda: self.operation_successful(
                "خدمات با موفقیت اضافه شد."
            ),
        )

    def update_medical_record(self,medical_record):
        self._start_worker(
            MedicalRecords.update_medical_record,
            [medical_record],
            success_callback=lambda: self.operation_successful(
                "خدمات با موفقیت ویرایش شد."
            ),
        )

    def operation_successful(self,success_msg):
        Messages.show_success_msg(success_msg)
        self.dispatcher.load_today_medical_records_list.emit()
        self.dispatcher.refresh_main_tab_reports.emit()
        self.dispatcher.refresh_patient_medical_records_list.emit()
        self.refresh_medical_record_info.emit()
        self.close()

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

class AddMedicalRecordImage(BaseController, QDialog):
    refresh_medical_record_images = pyqtSignal()

    def __init__(self, medical_record_id):
        super(AddMedicalRecordImage, self).__init__()
        self.ui = get_ui_class("aeImage")()
        self.ui.setupUi(self)
        self._setup_validators()
        self.setModal(True)
        self.active_workers = []
        self.medical_record_id = medical_record_id
        self.selected_image_path = ""
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.chooseImage_btn.clicked.connect(self.open_file_dialog)
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.save_btn.clicked.connect(self.validate_form)

    def _setup_validators(self):
        self.ui.imageName_txtbox.setMaxLength(50)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Images (*.png *.jpg *.jpeg)", options=options
        )
        if file_name:
            self.selected_image_path = file_name
            self.ui.imagePath_txtbox.setText(self.selected_image_path)

    def validate_form(self):
        name_txtbox = self.ui.imageName_txtbox.text().strip()
        txtboxes = [
            {"text": name_txtbox, "name": "نام تصویر"},
            {"text": self.selected_image_path, "name": "تصویر انتخاب شده"},
        ]

        if Validators.validate_empty_txt_boxes(txtboxes):
            self._get_patient_file_number_code()

    def _get_patient_file_number_code(self):
        self._start_worker(
            MedicalRecords.get_patient_file_number_medical_id,
            [self.medical_record_id],
            result_callback=self.handle_save_image,
        )

    def handle_save_image(self, patient):
        try:
            saved_image_path = self._save_image_file(str(patient["id"]))
        except Exception as e:
            error_msg = f"خطا در ذخیره فایل تصویر: {str(e)}"
            Messages.show_error_msg(error_msg)
            logging.error(error_msg)
            self.close()
        self.save_image_into_database(saved_image_path)

    def _save_image_file(self, patient_identity_code):
        return Images.save_image_to_patient_directory(
            self.selected_image_path, patient_identity_code
        )

    def save_image_into_database(self, saved_image_path):
        image_data = {
            "name": self.ui.imageName_txtbox.text().strip(),
            "path": saved_image_path,
            "medical_record": self.medical_record_id,
        }
        self._start_worker(
            MedicalRecordImages.add_medical_record_image,
            [image_data],
            success_callback=lambda: self.operation_successful(
                "تصویر با موفقیت اضافه شد."
            ),
        )

    def operation_successful(self, success_msg):
        Messages.show_success_msg(success_msg)
        self.refresh_medical_record_images.emit()
        self.close()
