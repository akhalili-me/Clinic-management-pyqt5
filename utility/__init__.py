from PyQt5.QtWidgets import QMessageBox

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
