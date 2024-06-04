# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_edit_delete_expense.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addEditDeleteExpense_form(object):
    def setupUi(self, addEditDeleteExpense_form):
        addEditDeleteExpense_form.setObjectName("addEditDeleteExpense_form")
        addEditDeleteExpense_form.resize(440, 395)
        addEditDeleteExpense_form.setMinimumSize(QtCore.QSize(440, 395))
        addEditDeleteExpense_form.setMaximumSize(QtCore.QSize(440, 395))
        self.label_10 = QtWidgets.QLabel(addEditDeleteExpense_form)
        self.label_10.setGeometry(QtCore.QRect(350, 230, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.description_txtbox = QtWidgets.QTextEdit(addEditDeleteExpense_form)
        self.description_txtbox.setGeometry(QtCore.QRect(30, 230, 331, 101))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn,sans-serif")
        font.setPointSize(-1)
        self.description_txtbox.setFont(font)
        self.description_txtbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.description_txtbox.setStyleSheet("/* Basic LineEdit styling */\n"
"QTextEdit {\n"
"    background-color: #ffffff; /* White background */\n"
"    border: 1px solid #dee2e6; /* Light grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \'Vazirmatn\', sans-serif; /* Font family */\n"
"    font-size: 16px; /* Font size */\n"
"    color: #343a40; /* Dark grey text color */\n"
"    outline: none; /* Remove default outline */\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QTextEdit:hover {\n"
"    border: 1px solid #007bff; /* Blue border on hover */\n"
"}\n"
"\n"
"/* Focus effect */\n"
"QTextEdit:focus {\n"
"    border: 1px solid #007bff; /* Blue border on focus */\n"
"}\n"
"\n"
"/* Disabled state */\n"
"QTextEdit:disabled {\n"
"    background-color: #e9ecef; /* Light grey background when disabled */\n"
"    color: #6c757d; /* Grey text color when disabled */\n"
"}\n"
"\n"
"")
        self.description_txtbox.setObjectName("description_txtbox")
        self.label_9 = QtWidgets.QLabel(addEditDeleteExpense_form)
        self.label_9.setGeometry(QtCore.QRect(360, 130, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(addEditDeleteExpense_form)
        self.label_5.setGeometry(QtCore.QRect(360, 90, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.name_txtbox = QtWidgets.QLineEdit(addEditDeleteExpense_form)
        self.name_txtbox.setGeometry(QtCore.QRect(30, 80, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn,sans-serif")
        font.setPointSize(-1)
        self.name_txtbox.setFont(font)
        self.name_txtbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.name_txtbox.setStyleSheet("/* Basic LineEdit styling */\n"
"QLineEdit {\n"
"    background-color: #ffffff; /* White background */\n"
"    border: 1px solid #dee2e6; /* Light grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \'Vazirmatn\', sans-serif; /* Font family */\n"
"    font-size: 16px; /* Font size */\n"
"    color: #343a40; /* Dark grey text color */\n"
"    outline: none; /* Remove default outline */\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QLineEdit:hover {\n"
"    border: 1px solid #007bff; /* Blue border on hover */\n"
"}\n"
"\n"
"/* Focus effect */\n"
"QLineEdit:focus {\n"
"    border: 1px solid #007bff; /* Blue border on focus */\n"
"}\n"
"\n"
"/* Disabled state */\n"
"QLineEdit:disabled {\n"
"    background-color: #e9ecef; /* Light grey background when disabled */\n"
"    color: #6c757d; /* Grey text color when disabled */\n"
"}\n"
"\n"
"")
        self.name_txtbox.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.name_txtbox.setObjectName("name_txtbox")
        self.price_txtbox = QtWidgets.QSpinBox(addEditDeleteExpense_form)
        self.price_txtbox.setGeometry(QtCore.QRect(30, 120, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.price_txtbox.setFont(font)
        self.price_txtbox.setAlignment(QtCore.Qt.AlignCenter)
        self.price_txtbox.setMinimum(1)
        self.price_txtbox.setMaximum(999999999)
        self.price_txtbox.setProperty("value", 200000)
        self.price_txtbox.setObjectName("price_txtbox")
        self.title_lbl = QtWidgets.QLabel(addEditDeleteExpense_form)
        self.title_lbl.setGeometry(QtCore.QRect(90, 20, 191, 41))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(15)
        self.title_lbl.setFont(font)
        self.title_lbl.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.title_lbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_lbl.setObjectName("title_lbl")
        self.groupBox_3 = QtWidgets.QGroupBox(addEditDeleteExpense_form)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 150, 331, 71))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_41 = QtWidgets.QLabel(self.groupBox_3)
        self.label_41.setGeometry(QtCore.QRect(270, 30, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        self.label_41.setFont(font)
        self.label_41.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.groupBox_3)
        self.label_42.setGeometry(QtCore.QRect(180, 30, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        self.label_42.setFont(font)
        self.label_42.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_42.setObjectName("label_42")
        self.year_spnbox = QtWidgets.QSpinBox(self.groupBox_3)
        self.year_spnbox.setGeometry(QtCore.QRect(10, 30, 91, 31))
        self.year_spnbox.setMinimum(1400)
        self.year_spnbox.setMaximum(1500)
        self.year_spnbox.setObjectName("year_spnbox")
        self.label_43 = QtWidgets.QLabel(self.groupBox_3)
        self.label_43.setGeometry(QtCore.QRect(90, 30, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        self.label_43.setFont(font)
        self.label_43.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_43.setObjectName("label_43")
        self.month_spnbox = QtWidgets.QSpinBox(self.groupBox_3)
        self.month_spnbox.setGeometry(QtCore.QRect(150, 30, 51, 31))
        self.month_spnbox.setMinimum(1)
        self.month_spnbox.setMaximum(12)
        self.month_spnbox.setProperty("value", 5)
        self.month_spnbox.setObjectName("month_spnbox")
        self.day_spnbox = QtWidgets.QSpinBox(self.groupBox_3)
        self.day_spnbox.setGeometry(QtCore.QRect(240, 30, 51, 31))
        self.day_spnbox.setMinimum(1)
        self.day_spnbox.setMaximum(31)
        self.day_spnbox.setProperty("value", 15)
        self.day_spnbox.setObjectName("day_spnbox")
        self.cancel_btn = QtWidgets.QPushButton(addEditDeleteExpense_form)
        self.cancel_btn.setGeometry(QtCore.QRect(290, 350, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cancel_btn.setStyleSheet("QPushButton {\n"
"    background-color: #cccccc; /* Light grey */\n"
"    color: #212529; /* Dark text */\n"
"    border: none;\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-size: 16px; /* Font size */\n"
"    font-weight: bold; /* Bold text */\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-family: \'Vazirmatn\', sans-serif; /* Font family */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b3b3b3; /* Darker grey on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #999999; /* Even darker grey on press */\n"
"}\n"
"")
        self.cancel_btn.setCheckable(False)
        self.cancel_btn.setObjectName("cancel_btn")
        self.save_btn = QtWidgets.QPushButton(addEditDeleteExpense_form)
        self.save_btn.setGeometry(QtCore.QRect(194, 350, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet("QPushButton {\n"
"    background-color: #28a745; /* Bootstrap success green */\n"
"    color: white; /* White text */\n"
"    border: none;\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-size: 16px; /* Font size */\n"
"    font-weight: bold; /* Bold text */\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-family: \'Vazirmatn\', sans-serif; /* Font family */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #218838; /* Darker green on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1e7e34; /* Even darker green on press */\n"
"}\n"
"")
        self.save_btn.setObjectName("save_btn")
        self.delete_btn = QtWidgets.QPushButton(addEditDeleteExpense_form)
        self.delete_btn.setEnabled(True)
        self.delete_btn.setGeometry(QtCore.QRect(30, 350, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn,sans-serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.delete_btn.setFont(font)
        self.delete_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.delete_btn.setStyleSheet("QPushButton{\n"
"    background-color: #dc3545; /* Bootstrap danger red */\n"
"    color: white; /* White text */\n"
"    border: none;\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-weight: bold; /* Bold text */\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-family: \'Vazirmatn\', sans-serif; /* Font family */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #c82333; /* Darker red on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #bd2130; /* Even darker red on press */\n"
"}\n"
"")
        self.delete_btn.setObjectName("delete_btn")

        self.retranslateUi(addEditDeleteExpense_form)
        QtCore.QMetaObject.connectSlotsByName(addEditDeleteExpense_form)

    def retranslateUi(self, addEditDeleteExpense_form):
        _translate = QtCore.QCoreApplication.translate
        addEditDeleteExpense_form.setWindowTitle(_translate("addEditDeleteExpense_form", "هزینه"))
        self.label_10.setText(_translate("addEditDeleteExpense_form", "توضیحات:"))
        self.label_9.setText(_translate("addEditDeleteExpense_form", "قیمت:"))
        self.label_5.setText(_translate("addEditDeleteExpense_form", "نام هزینه:"))
        self.title_lbl.setText(_translate("addEditDeleteExpense_form", "اضافه کردن هزینه"))
        self.groupBox_3.setTitle(_translate("addEditDeleteExpense_form", "تاریخ"))
        self.label_41.setText(_translate("addEditDeleteExpense_form", "روز:"))
        self.label_42.setText(_translate("addEditDeleteExpense_form", "ماه:"))
        self.label_43.setText(_translate("addEditDeleteExpense_form", "سال:"))
        self.cancel_btn.setText(_translate("addEditDeleteExpense_form", "لغو"))
        self.save_btn.setText(_translate("addEditDeleteExpense_form", "ثبت"))
        self.delete_btn.setText(_translate("addEditDeleteExpense_form", "حذف هزینه"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addEditDeleteExpense_form = QtWidgets.QWidget()
    ui = Ui_addEditDeleteExpense_form()
    ui.setupUi(addEditDeleteExpense_form)
    addEditDeleteExpense_form.show()
    sys.exit(app.exec_())
