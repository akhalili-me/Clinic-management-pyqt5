from PyQt5.QtWidgets import QMessageBox
from models import DatabaseManager,Doctors,Services
import jdatetime
from datetime import timedelta
import os
import uuid
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
IMAGES_DIR = BASE_DIR / "resources" / "images"

class Images:
    @staticmethod
    def create_image_directory_if_not_exist(patient_name):
        directory = Path.joinpath(IMAGES_DIR,patient_name)
        os.makedirs(directory, exist_ok=True)
        return directory

    @staticmethod
    def save_image_to_new_directory(current_image_path,image_directory):
            unique_filename = str(uuid.uuid4()) + os.path.splitext(current_image_path)[1]
            new_image_path = os.path.join(image_directory, unique_filename)
            shutil.copy(current_image_path, new_image_path)
            return new_image_path
   
    def delete_image(image_path):
        try:
            if os.path.exists(image_path):
                os.remove(image_path)
            else:
                raise
        except Exception:
            raise
    
    @staticmethod
    def get_default_image_path():
        return IMAGES_DIR / "default.png"

class Validators:
    @staticmethod
    def validate_empty_txt_boxes(txtboxes):
        for txtbox in txtboxes:
            name = txtbox["name"]
            text = txtbox["text"]
            if len(text.strip()) == 0:
                Messages.show_error_msg(f"{name} نباید خالی باشد.")
                return False
        return True
        
class Messages:
    @staticmethod
    def show_error_msg(message="عملیات با خطا مواجه شد، مجدداً امتحان کنید."):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText(message)
        msg_box.setWindowTitle("خطا")
        msg_box.exec_()

    @staticmethod
    def show_success_msg(message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(message)
        msg_box.setWindowTitle("موفقیت")
        msg_box.exec_()

    @staticmethod
    def show_confirm_delete_msg():
        msg_box = QMessageBox()
        msg_box.setWindowTitle('تایید حذف')
        msg_box.setText('آیا از حذف مطمئن هستید؟')
        msg_box.setIcon(QMessageBox.Question)
        yes_button = msg_box.addButton('آره', QMessageBox.YesRole)
        no_button = msg_box.addButton('خیر', QMessageBox.NoRole)
        msg_box.setDefaultButton(no_button)
        msg_box.exec_()  
        return msg_box, yes_button  
    
    @staticmethod
    def show_confirm_msg():
        msg_box = QMessageBox()
        msg_box.setWindowTitle('تایید عملیات')
        msg_box.setText('آیا از انجام عملیات مطمئن هستید؟')
        msg_box.setIcon(QMessageBox.Question)
        yes_button = msg_box.addButton('آره', QMessageBox.YesRole)
        no_button = msg_box.addButton('خیر', QMessageBox.NoRole)
        msg_box.setDefaultButton(no_button)
        msg_box.exec_()  
        return msg_box, yes_button  
  


class Numbers:
    @staticmethod
    def int_to_persian_with_separators(number):
        persian_numbers = {'0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'}
        persian_number_str = format(number, ',d').replace(',', '،')
        return ''.join(persian_numbers.get(char, char) for char in persian_number_str)
    
    @staticmethod
    def persian_to_english_numbers(input_string):
        persian_numbers = '۰۱۲۳۴۵۶۷۸۹'
        english_numbers = '0123456789'
        translation_table = str.maketrans(persian_numbers, english_numbers)
        return input_string.translate(translation_table)
    
    @staticmethod
    def english_to_persian_numbers(input_string):
        persian_numbers = '۰۱۲۳۴۵۶۷۸۹'
        english_numbers = '0123456789'
        translation_table = str.maketrans(english_numbers, persian_numbers)
        return input_string.translate(translation_table)

class Dates:
    @staticmethod
    def convert_to_jalali_format(date_str: str) -> str:
        year, month, day = map(int, date_str.split('-'))
        date_obj = jdatetime.date(year, month, day)
        
        weekday_number = date_obj.weekday()
        weekday_persian = Dates.get_persian_weekday(weekday_number)

        persian_date = date_obj.strftime("%Y/%m/%d")
        persian_date_formatted = Numbers.english_to_persian_numbers(persian_date)

        return f"{weekday_persian} {persian_date_formatted}"
    
    @staticmethod
    def get_future_date(days_ahead) -> str:
        tomorrow = jdatetime.date.today() + timedelta(days=days_ahead)
        return tomorrow.strftime("%Y-%m-%d")
    
    @staticmethod
    def get_persian_weekday(weekday_number: int) -> str:
        weekday_persian_mapping = {
            0: 'شنبه',
            1: 'یک‌شنبه',
            2: 'دوشنبه',
            3: 'سه‌شنبه',
            4: 'چهارشنبه',
            5: 'پنج‌شنبه',
            6: 'جمعه'
        }
        return weekday_persian_mapping[weekday_number]

    @staticmethod
    def get_jalali_current_month_interval_based_on_greg():
        today = jdatetime.date.today()
        if today.month < 7:
            last_day = 31
        elif today.month < 12:
            last_day = 30
        else:
            # Esfand has 29 days in a common year and 30 days in a leap year
            last_day = 30 if jdatetime.date.isleap(today.year) else 29
        first_day_of_month = jdatetime.date(today.year, today.month, 1).togregorian()
        last_day_of_month = jdatetime.date(today.year, today.month, last_day).togregorian()
        return first_day_of_month, last_day_of_month

    
class LoadingValues:
    @staticmethod
    def load_doctors_services_combo_boxes(ui):
        with DatabaseManager() as db:
            ui.doctor_cmbox.clear()
            doctors =  Doctors.get_all(db)
            for doctor in doctors:
                full_name = f"{doctor["firstName"]} {doctor["lastName"]}"
                ui.doctor_cmbox.addItem(f"دکتر {full_name}", doctor["id"])

            ui.service_cmbox.clear()
            services = Services.get_all(db)
            for service in services:
                ui.service_cmbox.addItem(service["name"],service["id"])
        
    @staticmethod
    def load_current_date_spin_box_values(ui, date_spnbox_names=None):
        if not date_spnbox_names:
            date_spnbox_names = {
                "year": "year_spnbox",
                "month": "month_spnbox",
                "day": "day_spnbox"
            }

        current_date = jdatetime.date.today()
        from PyQt5.QtWidgets import QSpinBox
        ui.findChild(QSpinBox, date_spnbox_names["year"]).setValue(current_date.year)
        ui.findChild(QSpinBox, date_spnbox_names["month"]).setValue(current_date.month)
        ui.findChild(QSpinBox, date_spnbox_names["day"]).setValue(current_date.day)

    @staticmethod
    def load_date_into_date_spinbox(ui,date: str):
        year, month, day = map(int, date.split('-'))
        ui.year_spnbox.setValue(year)
        ui.month_spnbox.setValue(month)
        ui.day_spnbox.setValue(day)

    @staticmethod
    def load_time_into_time_spnbox(ui,time: str):
        hour, minute = map(int, time.split(':'))
        ui.hour_spnbox.setValue(hour)
        ui.minute_spnbox.setValue(minute)
