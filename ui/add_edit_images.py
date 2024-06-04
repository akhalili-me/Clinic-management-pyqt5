# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_edit_images.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addEditImage_form(object):
    def setupUi(self, addEditImage_form):
        addEditImage_form.setObjectName("addEditImage_form")
        addEditImage_form.resize(424, 251)
        addEditImage_form.setMinimumSize(QtCore.QSize(424, 251))
        addEditImage_form.setMaximumSize(QtCore.QSize(424, 251))
        self.save_btn = QtWidgets.QPushButton(addEditImage_form)
        self.save_btn.setGeometry(QtCore.QRect(170, 210, 91, 31))
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
        self.cancel_btn = QtWidgets.QPushButton(addEditImage_form)
        self.cancel_btn.setGeometry(QtCore.QRect(270, 210, 75, 31))
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
        self.imageName_txtbox = QtWidgets.QLineEdit(addEditImage_form)
        self.imageName_txtbox.setGeometry(QtCore.QRect(10, 70, 331, 31))
        self.imageName_txtbox.setMinimumSize(QtCore.QSize(0, 0))
        self.imageName_txtbox.setMaximumSize(QtCore.QSize(7777, 7777))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn,sans-serif")
        font.setPointSize(-1)
        self.imageName_txtbox.setFont(font)
        self.imageName_txtbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.imageName_txtbox.setStyleSheet("/* Basic LineEdit styling */\n"
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
        self.imageName_txtbox.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.imageName_txtbox.setObjectName("imageName_txtbox")
        self.label_5 = QtWidgets.QLabel(addEditImage_form)
        self.label_5.setGeometry(QtCore.QRect(330, 80, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.chooseImage_btn = QtWidgets.QPushButton(addEditImage_form)
        self.chooseImage_btn.setGeometry(QtCore.QRect(220, 160, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn,sans-serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.chooseImage_btn.setFont(font)
        self.chooseImage_btn.setStyleSheet("QPushButton {\n"
"    background-color: #0050a5; /* Bootstrap primary blue */\n"
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
"    background-color: #0056b3; /* Darker blue on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #004085; /* Even darker blue on press */\n"
"}\n"
"")
        self.chooseImage_btn.setObjectName("chooseImage_btn")
        self.label_6 = QtWidgets.QLabel(addEditImage_form)
        self.label_6.setGeometry(QtCore.QRect(340, 120, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.imagePath_txtbox = QtWidgets.QLineEdit(addEditImage_form)
        self.imagePath_txtbox.setEnabled(False)
        self.imagePath_txtbox.setGeometry(QtCore.QRect(10, 110, 331, 31))
        self.imagePath_txtbox.setMinimumSize(QtCore.QSize(0, 0))
        self.imagePath_txtbox.setMaximumSize(QtCore.QSize(7777, 7777))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Medium")
        font.setPointSize(10)
        self.imagePath_txtbox.setFont(font)
        self.imagePath_txtbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.imagePath_txtbox.setStyleSheet("/* Basic LineEdit styling */\n"
"QLineEdit {\n"
"    background-color: #ffffff; /* White background */\n"
"    border: 1px solid #dee2e6; /* Light grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
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
        self.imagePath_txtbox.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.imagePath_txtbox.setObjectName("imagePath_txtbox")
        self.title_lbl = QtWidgets.QLabel(addEditImage_form)
        self.title_lbl.setGeometry(QtCore.QRect(60, 10, 191, 41))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(14)
        self.title_lbl.setFont(font)
        self.title_lbl.setObjectName("title_lbl")

        self.retranslateUi(addEditImage_form)
        QtCore.QMetaObject.connectSlotsByName(addEditImage_form)

    def retranslateUi(self, addEditImage_form):
        _translate = QtCore.QCoreApplication.translate
        addEditImage_form.setWindowTitle(_translate("addEditImage_form", "تصویر"))
        self.save_btn.setText(_translate("addEditImage_form", "ثبت"))
        self.cancel_btn.setText(_translate("addEditImage_form", "لغو"))
        self.label_5.setText(_translate("addEditImage_form", "نام تصویر:"))
        self.chooseImage_btn.setText(_translate("addEditImage_form", "انتخاب فایل تصویر"))
        self.label_6.setText(_translate("addEditImage_form", "مسیر تصویر:"))
        self.imagePath_txtbox.setText(_translate("addEditImage_form", "picture path"))
        self.title_lbl.setText(_translate("addEditImage_form", "اضافه کردن تصویر"))