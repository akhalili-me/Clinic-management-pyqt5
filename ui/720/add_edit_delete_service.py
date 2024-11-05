# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_edit_delete_service.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aedService(object):
    def setupUi(self, addEditDeleteService_form):
        addEditDeleteService_form.setObjectName("addEditDeleteService_form")
        addEditDeleteService_form.resize(427, 142)
        addEditDeleteService_form.setMinimumSize(QtCore.QSize(427, 142))
        addEditDeleteService_form.setMaximumSize(QtCore.QSize(427, 142))
        self.label_5 = QtWidgets.QLabel(addEditDeleteService_form)
        self.label_5.setGeometry(QtCore.QRect(340, 20, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.serviceName_txtbox = QtWidgets.QLineEdit(addEditDeleteService_form)
        self.serviceName_txtbox.setGeometry(QtCore.QRect(20, 10, 321, 31))
        self.serviceName_txtbox.setMinimumSize(QtCore.QSize(321, 31))
        self.serviceName_txtbox.setMaximumSize(QtCore.QSize(321, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        self.serviceName_txtbox.setFont(font)
        self.serviceName_txtbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.serviceName_txtbox.setStyleSheet("/* Basic LineEdit styling */\n"
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
        self.serviceName_txtbox.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.serviceName_txtbox.setObjectName("serviceName_txtbox")
        self.label_6 = QtWidgets.QLabel(addEditDeleteService_form)
        self.label_6.setGeometry(QtCore.QRect(340, 49, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.servicePrice_spnbox = QtWidgets.QSpinBox(addEditDeleteService_form)
        self.servicePrice_spnbox.setGeometry(QtCore.QRect(20, 50, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn,sans-serif")
        font.setPointSize(13)
        self.servicePrice_spnbox.setFont(font)
        self.servicePrice_spnbox.setStyleSheet("")
        self.servicePrice_spnbox.setAlignment(QtCore.Qt.AlignCenter)
        self.servicePrice_spnbox.setMinimum(100)
        self.servicePrice_spnbox.setMaximum(1000000000)
        self.servicePrice_spnbox.setProperty("value", 100000)
        self.servicePrice_spnbox.setObjectName("servicePrice_spnbox")
        self.save_btn = QtWidgets.QPushButton(addEditDeleteService_form)
        self.save_btn.setGeometry(QtCore.QRect(164, 100, 91, 31))
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
        self.cancel_btn = QtWidgets.QPushButton(addEditDeleteService_form)
        self.cancel_btn.setGeometry(QtCore.QRect(260, 100, 75, 31))
        self.cancel_btn.setMinimumSize(QtCore.QSize(75, 0))
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
        self.deleteService_btn = QtWidgets.QPushButton(addEditDeleteService_form)
        self.deleteService_btn.setEnabled(True)
        self.deleteService_btn.setGeometry(QtCore.QRect(20, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.deleteService_btn.setFont(font)
        self.deleteService_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.deleteService_btn.setStyleSheet("QPushButton{\n"
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
        self.deleteService_btn.setObjectName("deleteService_btn")

        self.retranslateUi(addEditDeleteService_form)
        QtCore.QMetaObject.connectSlotsByName(addEditDeleteService_form)

    def retranslateUi(self, addEditDeleteService_form):
        _translate = QtCore.QCoreApplication.translate
        addEditDeleteService_form.setWindowTitle(_translate("addEditDeleteService_form", "سرویس"))
        self.label_5.setText(_translate("addEditDeleteService_form", "نام سرویس:"))
        self.label_6.setText(_translate("addEditDeleteService_form", "قیمت:"))
        self.save_btn.setText(_translate("addEditDeleteService_form", "ثبت"))
        self.cancel_btn.setText(_translate("addEditDeleteService_form", "لغو"))
        self.deleteService_btn.setText(_translate("addEditDeleteService_form", "حذف سرویس"))


