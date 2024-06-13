from PyQt5.QtWidgets import QMessageBox

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