from PyQt5.QtWidgets import QMessageBox
from models import DatabaseManager,Doctors,Services
import jdatetime
from datetime import timedelta

class Messages:
    @staticmethod
    def show_error_msg(message):
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
    def load_date_spin_box_values(ui):
        current_date = jdatetime.date.today()
        ui.year_spnbox.setValue(current_date.year)
        ui.month_spnbox.setValue(current_date.month)
        ui.day_spnbox.setValue(current_date.day)


