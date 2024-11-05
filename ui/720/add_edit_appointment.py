# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_edit_appointment.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aeAppointment(object):
    def setupUi(self, addEditAppointment_form):
        addEditAppointment_form.setObjectName("addEditAppointment_form")
        addEditAppointment_form.resize(445, 485)
        addEditAppointment_form.setMinimumSize(QtCore.QSize(445, 485))
        addEditAppointment_form.setMaximumSize(QtCore.QSize(445, 485))
        self.doctor_cmbox = QtWidgets.QComboBox(addEditAppointment_form)
        self.doctor_cmbox.setEnabled(True)
        self.doctor_cmbox.setGeometry(QtCore.QRect(40, 20, 331, 31))
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
        self.cancel_btn = QtWidgets.QPushButton(addEditAppointment_form)
        self.cancel_btn.setGeometry(QtCore.QRect(300, 440, 75, 31))
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
        self.save_btn = QtWidgets.QPushButton(addEditAppointment_form)
        self.save_btn.setGeometry(QtCore.QRect(200, 440, 91, 31))
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
        self.label_13 = QtWidgets.QLabel(addEditAppointment_form)
        self.label_13.setGeometry(QtCore.QRect(370, 30, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.groupBox_2 = QtWidgets.QGroupBox(addEditAppointment_form)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 140, 331, 91))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_38 = QtWidgets.QLabel(self.groupBox_2)
        self.label_38.setGeometry(QtCore.QRect(270, 40, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        self.label_38.setFont(font)
        self.label_38.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.groupBox_2)
        self.label_39.setGeometry(QtCore.QRect(180, 40, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        self.label_39.setFont(font)
        self.label_39.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_39.setObjectName("label_39")
        self.year_spnbox = QtWidgets.QSpinBox(self.groupBox_2)
        self.year_spnbox.setGeometry(QtCore.QRect(10, 40, 91, 31))
        self.year_spnbox.setMinimum(1400)
        self.year_spnbox.setMaximum(1500)
        self.year_spnbox.setObjectName("year_spnbox")
        self.label_40 = QtWidgets.QLabel(self.groupBox_2)
        self.label_40.setGeometry(QtCore.QRect(90, 40, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        self.label_40.setFont(font)
        self.label_40.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_40.setObjectName("label_40")
        self.month_spnbox = QtWidgets.QSpinBox(self.groupBox_2)
        self.month_spnbox.setGeometry(QtCore.QRect(150, 40, 51, 31))
        self.month_spnbox.setMinimum(1)
        self.month_spnbox.setMaximum(12)
        self.month_spnbox.setProperty("value", 5)
        self.month_spnbox.setObjectName("month_spnbox")
        self.day_spnbox = QtWidgets.QSpinBox(self.groupBox_2)
        self.day_spnbox.setGeometry(QtCore.QRect(240, 40, 51, 31))
        self.day_spnbox.setMinimum(1)
        self.day_spnbox.setMaximum(31)
        self.day_spnbox.setProperty("value", 15)
        self.day_spnbox.setObjectName("day_spnbox")
        self.groupBox_5 = QtWidgets.QGroupBox(addEditAppointment_form)
        self.groupBox_5.setGeometry(QtCore.QRect(40, 230, 331, 91))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.minute_spnbox = QtWidgets.QSpinBox(self.groupBox_5)
        self.minute_spnbox.setGeometry(QtCore.QRect(160, 40, 51, 31))
        self.minute_spnbox.setMinimum(0)
        self.minute_spnbox.setMaximum(59)
        self.minute_spnbox.setProperty("value", 30)
        self.minute_spnbox.setObjectName("minute_spnbox")
        self.label_47 = QtWidgets.QLabel(self.groupBox_5)
        self.label_47.setGeometry(QtCore.QRect(200, 40, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        self.label_47.setFont(font)
        self.label_47.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_47.setObjectName("label_47")
        self.hour_spnbox = QtWidgets.QSpinBox(self.groupBox_5)
        self.hour_spnbox.setGeometry(QtCore.QRect(50, 40, 51, 31))
        self.hour_spnbox.setMinimum(0)
        self.hour_spnbox.setMaximum(24)
        self.hour_spnbox.setProperty("value", 15)
        self.hour_spnbox.setObjectName("hour_spnbox")
        self.label_48 = QtWidgets.QLabel(self.groupBox_5)
        self.label_48.setGeometry(QtCore.QRect(90, 40, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        self.label_48.setFont(font)
        self.label_48.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_48.setObjectName("label_48")
        self.description_txtbox = QtWidgets.QTextEdit(addEditAppointment_form)
        self.description_txtbox.setGeometry(QtCore.QRect(40, 330, 331, 101))
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
        self.service_cmbox = QtWidgets.QComboBox(addEditAppointment_form)
        self.service_cmbox.setEnabled(True)
        self.service_cmbox.setGeometry(QtCore.QRect(40, 100, 331, 31))
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
        self.label_14 = QtWidgets.QLabel(addEditAppointment_form)
        self.label_14.setGeometry(QtCore.QRect(360, 110, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(addEditAppointment_form)
        self.label_15.setGeometry(QtCore.QRect(360, 70, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.status_cmbox = QtWidgets.QComboBox(addEditAppointment_form)
        self.status_cmbox.setEnabled(True)
        self.status_cmbox.setGeometry(QtCore.QRect(40, 60, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(11)
        self.status_cmbox.setFont(font)
        self.status_cmbox.setAcceptDrops(False)
        self.status_cmbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.status_cmbox.setStyleSheet("")
        self.status_cmbox.setEditable(False)
        self.status_cmbox.setMaxVisibleItems(3)
        self.status_cmbox.setDuplicatesEnabled(False)
        self.status_cmbox.setObjectName("status_cmbox")
        self.status_cmbox.addItem("")
        self.status_cmbox.addItem("")
        self.label_16 = QtWidgets.QLabel(addEditAppointment_form)
        self.label_16.setGeometry(QtCore.QRect(370, 335, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")

        self.retranslateUi(addEditAppointment_form)
        QtCore.QMetaObject.connectSlotsByName(addEditAppointment_form)

    def retranslateUi(self, addEditAppointment_form):
        _translate = QtCore.QCoreApplication.translate
        addEditAppointment_form.setWindowTitle(_translate("addEditAppointment_form", "نوبت"))
        self.cancel_btn.setText(_translate("addEditAppointment_form", "لغو"))
        self.save_btn.setText(_translate("addEditAppointment_form", "ثبت"))
        self.label_13.setText(_translate("addEditAppointment_form", "نام پزشک: "))
        self.groupBox_2.setTitle(_translate("addEditAppointment_form", "تاریخ"))
        self.label_38.setText(_translate("addEditAppointment_form", "روز:"))
        self.label_39.setText(_translate("addEditAppointment_form", "ماه:"))
        self.label_40.setText(_translate("addEditAppointment_form", "سال:"))
        self.groupBox_5.setTitle(_translate("addEditAppointment_form", "زمان"))
        self.label_47.setText(_translate("addEditAppointment_form", "دقیقه:"))
        self.label_48.setText(_translate("addEditAppointment_form", "ساعت:"))
        self.description_txtbox.setHtml(_translate("addEditAppointment_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Vazirmatn\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_14.setText(_translate("addEditAppointment_form", "سرویس:"))
        self.label_15.setText(_translate("addEditAppointment_form", "وضعیت:"))
        self.status_cmbox.setCurrentText(_translate("addEditAppointment_form", "فعال"))
        self.status_cmbox.setItemText(0, _translate("addEditAppointment_form", "فعال"))
        self.status_cmbox.setItemText(1, _translate("addEditAppointment_form", "غیرفعال"))
        self.label_16.setText(_translate("addEditAppointment_form", "توضیحات:"))