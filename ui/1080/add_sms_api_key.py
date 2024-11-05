# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sms_api_key.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aSmsApi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(431, 233)
        Form.setMinimumSize(QtCore.QSize(431, 233))
        Form.setMaximumSize(QtCore.QSize(431, 233))
        self.apiKey_txtbox = QtWidgets.QTextEdit(Form)
        self.apiKey_txtbox.setGeometry(QtCore.QRect(10, 40, 411, 131))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        self.apiKey_txtbox.setFont(font)
        self.apiKey_txtbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.apiKey_txtbox.setStyleSheet("/* Basic LineEdit styling */\n"
"QTextEdit {\n"
"    background-color: #ffffff; /* White background */\n"
"    border: 1px solid #dee2e6; /* Light grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
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
        self.apiKey_txtbox.setObjectName("apiKey_txtbox")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(220, -20, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.save_btn = QtWidgets.QPushButton(Form)
        self.save_btn.setGeometry(QtCore.QRect(250, 180, 91, 41))
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
        self.cancel_btn = QtWidgets.QPushButton(Form)
        self.cancel_btn.setGeometry(QtCore.QRect(350, 180, 71, 41))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "API key"))
        self.label_11.setText(_translate("Form", "کلید سرویس پیامکی کاوه‌نگار"))
        self.save_btn.setText(_translate("Form", "ذخیره"))
        self.cancel_btn.setText(_translate("Form", "لغو"))
