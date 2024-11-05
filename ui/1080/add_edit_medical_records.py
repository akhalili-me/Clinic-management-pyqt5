# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_edit_medical_records.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aeMedicalRecord(object):
    def setupUi(self, addEditMedicalRecords_form):
        addEditMedicalRecords_form.setObjectName("addEditMedicalRecords_form")
        addEditMedicalRecords_form.resize(442, 363)
        addEditMedicalRecords_form.setMinimumSize(QtCore.QSize(442, 363))
        addEditMedicalRecords_form.setMaximumSize(QtCore.QSize(442, 363))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        addEditMedicalRecords_form.setFont(font)
        addEditMedicalRecords_form.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_3 = QtWidgets.QGroupBox(addEditMedicalRecords_form)
        self.groupBox_3.setGeometry(QtCore.QRect(40, 110, 331, 71))
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
        self.label_42.setGeometry(QtCore.QRect(180, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        self.label_42.setFont(font)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.year_spnbox = QtWidgets.QSpinBox(self.groupBox_3)
        self.year_spnbox.setGeometry(QtCore.QRect(10, 30, 91, 31))
        self.year_spnbox.setMinimum(1400)
        self.year_spnbox.setMaximum(1500)
        self.year_spnbox.setObjectName("year_spnbox")
        self.label_43 = QtWidgets.QLabel(self.groupBox_3)
        self.label_43.setGeometry(QtCore.QRect(90, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        self.label_43.setFont(font)
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
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
        self.label_14 = QtWidgets.QLabel(addEditMedicalRecords_form)
        self.label_14.setGeometry(QtCore.QRect(370, 40, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.cancel_btn = QtWidgets.QPushButton(addEditMedicalRecords_form)
        self.cancel_btn.setGeometry(QtCore.QRect(300, 310, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(14)
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
        self.label_16 = QtWidgets.QLabel(addEditMedicalRecords_form)
        self.label_16.setGeometry(QtCore.QRect(370, 190, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.doctor_cmbox = QtWidgets.QComboBox(addEditMedicalRecords_form)
        self.doctor_cmbox.setEnabled(True)
        self.doctor_cmbox.setGeometry(QtCore.QRect(40, 30, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(11)
        self.doctor_cmbox.setFont(font)
        self.doctor_cmbox.setAcceptDrops(False)
        self.doctor_cmbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.doctor_cmbox.setStyleSheet("")
        self.doctor_cmbox.setEditable(False)
        self.doctor_cmbox.setCurrentText("")
        self.doctor_cmbox.setMaxVisibleItems(3)
        self.doctor_cmbox.setDuplicatesEnabled(False)
        self.doctor_cmbox.setObjectName("doctor_cmbox")
        self.save_btn = QtWidgets.QPushButton(addEditMedicalRecords_form)
        self.save_btn.setGeometry(QtCore.QRect(200, 310, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(14)
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
"    font-weight: bold; /* Bold text */\n"
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
        self.service_cmbox = QtWidgets.QComboBox(addEditMedicalRecords_form)
        self.service_cmbox.setEnabled(True)
        self.service_cmbox.setGeometry(QtCore.QRect(40, 70, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(11)
        self.service_cmbox.setFont(font)
        self.service_cmbox.setAcceptDrops(False)
        self.service_cmbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.service_cmbox.setStyleSheet("")
        self.service_cmbox.setEditable(False)
        self.service_cmbox.setCurrentText("")
        self.service_cmbox.setMaxVisibleItems(10)
        self.service_cmbox.setDuplicatesEnabled(False)
        self.service_cmbox.setObjectName("service_cmbox")
        self.label_17 = QtWidgets.QLabel(addEditMedicalRecords_form)
        self.label_17.setGeometry(QtCore.QRect(360, 70, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.description_txtbox = QtWidgets.QTextEdit(addEditMedicalRecords_form)
        self.description_txtbox.setGeometry(QtCore.QRect(40, 190, 331, 111))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        self.description_txtbox.setFont(font)
        self.description_txtbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.description_txtbox.setStyleSheet("/* Basic LineEdit styling */\n"
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
        self.description_txtbox.setObjectName("description_txtbox")

        self.retranslateUi(addEditMedicalRecords_form)
        QtCore.QMetaObject.connectSlotsByName(addEditMedicalRecords_form)

    def retranslateUi(self, addEditMedicalRecords_form):
        _translate = QtCore.QCoreApplication.translate
        addEditMedicalRecords_form.setWindowTitle(_translate("addEditMedicalRecords_form", "خدمات"))
        self.groupBox_3.setTitle(_translate("addEditMedicalRecords_form", "تاریخ"))
        self.label_41.setText(_translate("addEditMedicalRecords_form", "روز:"))
        self.label_42.setText(_translate("addEditMedicalRecords_form", "ماه:"))
        self.label_43.setText(_translate("addEditMedicalRecords_form", "سال:"))
        self.label_14.setText(_translate("addEditMedicalRecords_form", "نام پزشک: "))
        self.cancel_btn.setText(_translate("addEditMedicalRecords_form", "لغو"))
        self.label_16.setText(_translate("addEditMedicalRecords_form", "توضیحات:"))
        self.save_btn.setText(_translate("addEditMedicalRecords_form", "ثبت"))
        self.label_17.setText(_translate("addEditMedicalRecords_form", "سرویس:"))

