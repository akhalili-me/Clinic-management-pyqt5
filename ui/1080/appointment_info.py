# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appointment_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_iAppointment(object):
    def setupUi(self, appointmentInfo_form):
        appointmentInfo_form.setObjectName("appointmentInfo_form")
        appointmentInfo_form.resize(649, 503)
        appointmentInfo_form.setMinimumSize(QtCore.QSize(649, 503))
        appointmentInfo_form.setMaximumSize(QtCore.QSize(649, 503))
        self.sendReminderSMS_btn = QtWidgets.QPushButton(appointmentInfo_form)
        self.sendReminderSMS_btn.setGeometry(QtCore.QRect(20, 450, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.sendReminderSMS_btn.setFont(font)
        self.sendReminderSMS_btn.setStyleSheet("QPushButton {\n"
"    background-color: #0050a5; /* Bootstrap primary blue */\n"
"    color: white; /* White text */\n"
"    border: none;\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
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
        self.sendReminderSMS_btn.setObjectName("sendReminderSMS_btn")
        self.addAppointmentToMedicalRecords_btn = QtWidgets.QPushButton(appointmentInfo_form)
        self.addAppointmentToMedicalRecords_btn.setGeometry(QtCore.QRect(210, 450, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.addAppointmentToMedicalRecords_btn.setFont(font)
        self.addAppointmentToMedicalRecords_btn.setStyleSheet("QPushButton {\n"
"    background-color: #17a2b8; /* Bootstrap primary blue */\n"
"    color: white; /* White text */\n"
"    border: none;\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
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
        self.addAppointmentToMedicalRecords_btn.setObjectName("addAppointmentToMedicalRecords_btn")
        self.editAppointment_btn = QtWidgets.QPushButton(appointmentInfo_form)
        self.editAppointment_btn.setGeometry(QtCore.QRect(440, 450, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.editAppointment_btn.setFont(font)
        self.editAppointment_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.editAppointment_btn.setStyleSheet("QPushButton {\n"
"    background-color: #ffc107; /* Bootstrap warning yellow */\n"
"    color: #212529; /* Dark text */\n"
"    border: none;\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e0a800; /* Darker yellow on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #c69500; /* Even darker yellow on press */\n"
"}\n"
"")
        self.editAppointment_btn.setObjectName("editAppointment_btn")
        self.deleteAppointment_btn = QtWidgets.QPushButton(appointmentInfo_form)
        self.deleteAppointment_btn.setGeometry(QtCore.QRect(550, 450, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.deleteAppointment_btn.setFont(font)
        self.deleteAppointment_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.deleteAppointment_btn.setStyleSheet("QPushButton{\n"
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
        self.deleteAppointment_btn.setObjectName("deleteAppointment_btn")
        self.smsCount_lbl = QtWidgets.QLabel(appointmentInfo_form)
        self.smsCount_lbl.setGeometry(QtCore.QRect(20, 390, 611, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Medium")
        font.setPointSize(12)
        self.smsCount_lbl.setFont(font)
        self.smsCount_lbl.setStyleSheet("border: 1px solid;\n"
"background-color: rgb(233, 236, 239);\n"
"border-radius: 5px;\n"
"border-color: rgb(206, 206, 206); ")
        self.smsCount_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.smsCount_lbl.setObjectName("smsCount_lbl")
        self.patientFullName_lbl = QtWidgets.QLabel(appointmentInfo_form)
        self.patientFullName_lbl.setGeometry(QtCore.QRect(20, 20, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Medium")
        font.setPointSize(12)
        self.patientFullName_lbl.setFont(font)
        self.patientFullName_lbl.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(232, 232, 232);\n"
"background-color: rgb(233, 236, 239);\n"
"border-radius: 10px;\n"
"border-color: rgb(206, 206, 206); ")
        self.patientFullName_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.patientFullName_lbl.setObjectName("patientFullName_lbl")
        self.phoneNumber_lbl = QtWidgets.QLabel(appointmentInfo_form)
        self.phoneNumber_lbl.setGeometry(QtCore.QRect(20, 70, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Medium")
        font.setPointSize(12)
        self.phoneNumber_lbl.setFont(font)
        self.phoneNumber_lbl.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(232, 232, 232);\n"
"background-color: rgb(233, 236, 239);\n"
"border-radius: 10px;\n"
"border-color: rgb(206, 206, 206); ")
        self.phoneNumber_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.phoneNumber_lbl.setObjectName("phoneNumber_lbl")
        self.patientFullName_lbl_2 = QtWidgets.QLabel(appointmentInfo_form)
        self.patientFullName_lbl_2.setGeometry(QtCore.QRect(530, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.patientFullName_lbl_2.setFont(font)
        self.patientFullName_lbl_2.setStyleSheet("border: 1px solid;\n"
"border-radius: 10px;\n"
"border-color: rgb(232, 232, 232);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(42, 98, 167);\n"
"\n"
"")
        self.patientFullName_lbl_2.setAlignment(QtCore.Qt.AlignCenter)
        self.patientFullName_lbl_2.setObjectName("patientFullName_lbl_2")
        self.datetime_lbl = QtWidgets.QLabel(appointmentInfo_form)
        self.datetime_lbl.setGeometry(QtCore.QRect(20, 120, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Medium")
        font.setPointSize(12)
        self.datetime_lbl.setFont(font)
        self.datetime_lbl.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(232, 232, 232);\n"
"background-color: rgb(233, 236, 239);\n"
"border-radius: 10px;\n"
"border-color: rgb(206, 206, 206); ")
        self.datetime_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.datetime_lbl.setObjectName("datetime_lbl")
        self.doctorName_lbl = QtWidgets.QLabel(appointmentInfo_form)
        self.doctorName_lbl.setGeometry(QtCore.QRect(20, 170, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Medium")
        font.setPointSize(12)
        self.doctorName_lbl.setFont(font)
        self.doctorName_lbl.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(232, 232, 232);\n"
"background-color: rgb(233, 236, 239);\n"
"border-radius: 10px;\n"
"border-color: rgb(206, 206, 206); ")
        self.doctorName_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.doctorName_lbl.setObjectName("doctorName_lbl")
        self.serviceName_lbl = QtWidgets.QLabel(appointmentInfo_form)
        self.serviceName_lbl.setGeometry(QtCore.QRect(20, 220, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Medium")
        font.setPointSize(12)
        self.serviceName_lbl.setFont(font)
        self.serviceName_lbl.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(232, 232, 232);\n"
"background-color: rgb(233, 236, 239);\n"
"border-radius: 10px;\n"
"border-color: rgb(206, 206, 206); ")
        self.serviceName_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.serviceName_lbl.setObjectName("serviceName_lbl")
        self.status_lbl = QtWidgets.QLabel(appointmentInfo_form)
        self.status_lbl.setGeometry(QtCore.QRect(20, 270, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Medium")
        font.setPointSize(12)
        self.status_lbl.setFont(font)
        self.status_lbl.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(232, 232, 232);\n"
"background-color: rgb(233, 236, 239);\n"
"border-radius: 10px;\n"
"border-color: rgb(206, 206, 206); ")
        self.status_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.status_lbl.setObjectName("status_lbl")
        self.patientFullName_lbl_3 = QtWidgets.QLabel(appointmentInfo_form)
        self.patientFullName_lbl_3.setGeometry(QtCore.QRect(530, 70, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.patientFullName_lbl_3.setFont(font)
        self.patientFullName_lbl_3.setStyleSheet("border: 1px solid;\n"
"border-radius: 10px;\n"
"border-color: rgb(232, 232, 232);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(42, 98, 167);\n"
"\n"
"")
        self.patientFullName_lbl_3.setAlignment(QtCore.Qt.AlignCenter)
        self.patientFullName_lbl_3.setObjectName("patientFullName_lbl_3")
        self.patientFullName_lbl_4 = QtWidgets.QLabel(appointmentInfo_form)
        self.patientFullName_lbl_4.setGeometry(QtCore.QRect(530, 120, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.patientFullName_lbl_4.setFont(font)
        self.patientFullName_lbl_4.setStyleSheet("border: 1px solid;\n"
"border-radius: 10px;\n"
"border-color: rgb(232, 232, 232);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(42, 98, 167);\n"
"\n"
"")
        self.patientFullName_lbl_4.setAlignment(QtCore.Qt.AlignCenter)
        self.patientFullName_lbl_4.setObjectName("patientFullName_lbl_4")
        self.patientFullName_lbl_5 = QtWidgets.QLabel(appointmentInfo_form)
        self.patientFullName_lbl_5.setGeometry(QtCore.QRect(530, 170, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.patientFullName_lbl_5.setFont(font)
        self.patientFullName_lbl_5.setStyleSheet("border: 1px solid;\n"
"border-radius: 10px;\n"
"border-color: rgb(232, 232, 232);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(42, 98, 167);\n"
"\n"
"")
        self.patientFullName_lbl_5.setAlignment(QtCore.Qt.AlignCenter)
        self.patientFullName_lbl_5.setObjectName("patientFullName_lbl_5")
        self.patientFullName_lbl_6 = QtWidgets.QLabel(appointmentInfo_form)
        self.patientFullName_lbl_6.setGeometry(QtCore.QRect(530, 220, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.patientFullName_lbl_6.setFont(font)
        self.patientFullName_lbl_6.setStyleSheet("border: 1px solid;\n"
"border-radius: 10px;\n"
"border-color: rgb(232, 232, 232);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(42, 98, 167);\n"
"\n"
"")
        self.patientFullName_lbl_6.setAlignment(QtCore.Qt.AlignCenter)
        self.patientFullName_lbl_6.setObjectName("patientFullName_lbl_6")
        self.patientFullName_lbl_7 = QtWidgets.QLabel(appointmentInfo_form)
        self.patientFullName_lbl_7.setGeometry(QtCore.QRect(530, 270, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.patientFullName_lbl_7.setFont(font)
        self.patientFullName_lbl_7.setStyleSheet("border: 1px solid;\n"
"border-radius: 10px;\n"
"border-color: rgb(232, 232, 232);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(42, 98, 167);\n"
"\n"
"")
        self.patientFullName_lbl_7.setAlignment(QtCore.Qt.AlignCenter)
        self.patientFullName_lbl_7.setObjectName("patientFullName_lbl_7")
        self.patientFullName_lbl_8 = QtWidgets.QLabel(appointmentInfo_form)
        self.patientFullName_lbl_8.setGeometry(QtCore.QRect(530, 320, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.patientFullName_lbl_8.setFont(font)
        self.patientFullName_lbl_8.setStyleSheet("border: 1px solid;\n"
"border-radius: 10px;\n"
"border-color: rgb(232, 232, 232);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(42, 98, 167);\n"
"\n"
"")
        self.patientFullName_lbl_8.setAlignment(QtCore.Qt.AlignCenter)
        self.patientFullName_lbl_8.setObjectName("patientFullName_lbl_8")
        self.description_lbl = QtWidgets.QTextEdit(appointmentInfo_form)
        self.description_lbl.setGeometry(QtCore.QRect(20, 320, 501, 61))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.description_lbl.setFont(font)
        self.description_lbl.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.description_lbl.setStyleSheet("/* Basic LineEdit styling */\n"
"QTextEdit {\n"
"    background-color: rgb(233, 236, 239);\n"
"       border: 1px solid;\n"
"    border-color: rgb(206, 206, 206); \n"
"    border-radius: 5px; /* Rounded corners */\n"
"    color: #343a40; /* Dark grey text color */\n"
"    outline: none; /* Remove default outline */\n"
"}\n"
"\n"
"/* Disabled state */\n"
"QTextEdit:disabled {\n"
"    background-color: #e9ecef; /* Light grey background when disabled */\n"
"    color: #6c757d; /* Grey text color when disabled */\n"
"}\n"
"\n"
"")
        self.description_lbl.setReadOnly(True)
        self.description_lbl.setObjectName("description_lbl")

        self.retranslateUi(appointmentInfo_form)
        QtCore.QMetaObject.connectSlotsByName(appointmentInfo_form)

    def retranslateUi(self, appointmentInfo_form):
        _translate = QtCore.QCoreApplication.translate
        appointmentInfo_form.setWindowTitle(_translate("appointmentInfo_form", "اطلاعات نوبت"))
        self.sendReminderSMS_btn.setText(_translate("appointmentInfo_form", "ارسال پیامک یادآوری به بیمار"))
        self.addAppointmentToMedicalRecords_btn.setText(_translate("appointmentInfo_form", "اضافه کردن نوبت به خدمات پرونده"))
        self.editAppointment_btn.setText(_translate("appointmentInfo_form", "ویرایش نوبت"))
        self.deleteAppointment_btn.setText(_translate("appointmentInfo_form", "حذف "))
        self.smsCount_lbl.setText(_translate("appointmentInfo_form", "-"))
        self.patientFullName_lbl.setText(_translate("appointmentInfo_form", "-"))
        self.phoneNumber_lbl.setText(_translate("appointmentInfo_form", "-"))
        self.patientFullName_lbl_2.setText(_translate("appointmentInfo_form", "نام بیمار"))
        self.datetime_lbl.setText(_translate("appointmentInfo_form", "-"))
        self.doctorName_lbl.setText(_translate("appointmentInfo_form", "-"))
        self.serviceName_lbl.setText(_translate("appointmentInfo_form", "-"))
        self.status_lbl.setText(_translate("appointmentInfo_form", "-"))
        self.patientFullName_lbl_3.setText(_translate("appointmentInfo_form", "شماره تلفن"))
        self.patientFullName_lbl_4.setText(_translate("appointmentInfo_form", "تاریخ و زمان"))
        self.patientFullName_lbl_5.setText(_translate("appointmentInfo_form", "دکتر"))
        self.patientFullName_lbl_6.setText(_translate("appointmentInfo_form", "سرویس"))
        self.patientFullName_lbl_7.setText(_translate("appointmentInfo_form", "وضعیت"))
        self.patientFullName_lbl_8.setText(_translate("appointmentInfo_form", "توضیحات"))
        self.description_lbl.setHtml(_translate("appointmentInfo_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Vazirmatn\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Vazirmatn,sans-serif\'; font-size:16px;\">-</span></p></body></html>"))


