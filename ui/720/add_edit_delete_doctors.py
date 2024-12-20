# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_edit_delete_doctors.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_aedDoctor(object):
    def setupUi(self, addEditDeleteDoctor_form):
        addEditDeleteDoctor_form.setObjectName("addEditDeleteDoctor_form")
        addEditDeleteDoctor_form.setEnabled(True)
        addEditDeleteDoctor_form.resize(448, 192)
        addEditDeleteDoctor_form.setMinimumSize(QtCore.QSize(448, 192))
        addEditDeleteDoctor_form.setMaximumSize(QtCore.QSize(448, 192))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        addEditDeleteDoctor_form.setFont(font)
        self.cancel_btn = QtWidgets.QPushButton(addEditDeleteDoctor_form)
        self.cancel_btn.setGeometry(QtCore.QRect(280, 150, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
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
"    text-align: center;\n"
"    text-decoration: none;\n"
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
        self.label_6 = QtWidgets.QLabel(addEditDeleteDoctor_form)
        self.label_6.setGeometry(QtCore.QRect(350, 59, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(addEditDeleteDoctor_form)
        self.label_5.setGeometry(QtCore.QRect(350, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setIndent(4)
        self.label_5.setObjectName("label_5")
        self.firstName_txtbox = QtWidgets.QLineEdit(addEditDeleteDoctor_form)
        self.firstName_txtbox.setGeometry(QtCore.QRect(20, 20, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(11)
        self.firstName_txtbox.setFont(font)
        self.firstName_txtbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.firstName_txtbox.setStyleSheet("/* Basic LineEdit styling */\n"
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
        self.firstName_txtbox.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.firstName_txtbox.setText("")
        self.firstName_txtbox.setObjectName("firstName_txtbox")
        self.label_8 = QtWidgets.QLabel(addEditDeleteDoctor_form)
        self.label_8.setGeometry(QtCore.QRect(357, 103, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lastName_txtbox = QtWidgets.QLineEdit(addEditDeleteDoctor_form)
        self.lastName_txtbox.setGeometry(QtCore.QRect(20, 60, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(11)
        self.lastName_txtbox.setFont(font)
        self.lastName_txtbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lastName_txtbox.setStyleSheet("/* Basic LineEdit styling */\n"
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
        self.lastName_txtbox.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.lastName_txtbox.setObjectName("lastName_txtbox")
        self.save_btn = QtWidgets.QPushButton(addEditDeleteDoctor_form)
        self.save_btn.setGeometry(QtCore.QRect(184, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
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
"    text-align: center;\n"
"    text-decoration: none;\n"
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
        self.specialization_txtbox = QtWidgets.QLineEdit(addEditDeleteDoctor_form)
        self.specialization_txtbox.setGeometry(QtCore.QRect(20, 100, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(11)
        self.specialization_txtbox.setFont(font)
        self.specialization_txtbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.specialization_txtbox.setStyleSheet("/* Basic LineEdit styling */\n"
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
        self.specialization_txtbox.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.specialization_txtbox.setObjectName("specialization_txtbox")
        self.deleteDoctor_btn = QtWidgets.QPushButton(addEditDeleteDoctor_form)
        self.deleteDoctor_btn.setEnabled(True)
        self.deleteDoctor_btn.setGeometry(QtCore.QRect(20, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.deleteDoctor_btn.setFont(font)
        self.deleteDoctor_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.deleteDoctor_btn.setStyleSheet("QPushButton{\n"
"    background-color: #dc3545; /* Bootstrap danger red */\n"
"    color: white; /* White text */\n"
"    border: none;\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
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
        self.deleteDoctor_btn.setObjectName("deleteDoctor_btn")

        self.retranslateUi(addEditDeleteDoctor_form)
        QtCore.QMetaObject.connectSlotsByName(addEditDeleteDoctor_form)

    def retranslateUi(self, addEditDeleteDoctor_form):
        _translate = QtCore.QCoreApplication.translate
        addEditDeleteDoctor_form.setWindowTitle(_translate("addEditDeleteDoctor_form", " پزشک"))
        self.cancel_btn.setText(_translate("addEditDeleteDoctor_form", "لغو"))
        self.label_6.setText(_translate("addEditDeleteDoctor_form", "نام خانوادگی: "))
        self.label_5.setText(_translate("addEditDeleteDoctor_form", "نام پزشک : "))
        self.label_8.setText(_translate("addEditDeleteDoctor_form", "تخصص:"))
        self.save_btn.setText(_translate("addEditDeleteDoctor_form", "ثبت"))
        self.deleteDoctor_btn.setText(_translate("addEditDeleteDoctor_form", "حذف پزشک"))

