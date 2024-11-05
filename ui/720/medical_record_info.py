# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medical_record_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from .resources_rc import *

class Ui_iMedicalRecord(object):
    def setupUi(self, medicalRecordInfo_form):
        medicalRecordInfo_form.setObjectName("medicalRecordInfo_form")
        medicalRecordInfo_form.resize(544, 465)
        medicalRecordInfo_form.setMinimumSize(QtCore.QSize(544, 465))
        medicalRecordInfo_form.setMaximumSize(QtCore.QSize(544, 465))
        self.tabWidget = QtWidgets.QTabWidget(medicalRecordInfo_form)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 551, 471))
        self.tabWidget.setMinimumSize(QtCore.QSize(551, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(551, 16777215))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.patientFullName_lbl = QtWidgets.QLabel(self.tab)
        self.patientFullName_lbl.setGeometry(QtCore.QRect(20, 20, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.patientFullName_lbl.setFont(font)
        self.patientFullName_lbl.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(232, 232, 232);\n"
"background-color: rgb(233, 236, 239);\n"
"border-radius: 10px;\n"
"border-color: rgb(206, 206, 206); ")
        self.patientFullName_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.patientFullName_lbl.setObjectName("patientFullName_lbl")
        self.patientFullName_lbl_2 = QtWidgets.QLabel(self.tab)
        self.patientFullName_lbl_2.setGeometry(QtCore.QRect(430, 20, 101, 41))
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
        self.date_lbl = QtWidgets.QLabel(self.tab)
        self.date_lbl.setGeometry(QtCore.QRect(20, 70, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.date_lbl.setFont(font)
        self.date_lbl.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(232, 232, 232);\n"
"background-color: rgb(233, 236, 239);\n"
"border-radius: 10px;\n"
"border-color: rgb(206, 206, 206); ")
        self.date_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.date_lbl.setObjectName("date_lbl")
        self.doctorName_lbl = QtWidgets.QLabel(self.tab)
        self.doctorName_lbl.setGeometry(QtCore.QRect(20, 120, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.doctorName_lbl.setFont(font)
        self.doctorName_lbl.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(232, 232, 232);\n"
"background-color: rgb(233, 236, 239);\n"
"border-radius: 10px;\n"
"border-color: rgb(206, 206, 206); ")
        self.doctorName_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.doctorName_lbl.setObjectName("doctorName_lbl")
        self.serviceName_lbl = QtWidgets.QLabel(self.tab)
        self.serviceName_lbl.setGeometry(QtCore.QRect(20, 170, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.serviceName_lbl.setFont(font)
        self.serviceName_lbl.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(232, 232, 232);\n"
"background-color: rgb(233, 236, 239);\n"
"border-radius: 10px;\n"
"border-color: rgb(206, 206, 206); ")
        self.serviceName_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.serviceName_lbl.setObjectName("serviceName_lbl")
        self.price_lbl = QtWidgets.QLabel(self.tab)
        self.price_lbl.setGeometry(QtCore.QRect(20, 220, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.price_lbl.setFont(font)
        self.price_lbl.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(232, 232, 232);\n"
"background-color: rgb(233, 236, 239);\n"
"border-radius: 10px;\n"
"border-color: rgb(206, 206, 206); ")
        self.price_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.price_lbl.setObjectName("price_lbl")
        self.description_lbl = QtWidgets.QTextEdit(self.tab)
        self.description_lbl.setGeometry(QtCore.QRect(20, 270, 401, 91))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(10)
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
        self.patientFullName_lbl_3 = QtWidgets.QLabel(self.tab)
        self.patientFullName_lbl_3.setGeometry(QtCore.QRect(430, 70, 101, 41))
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
        self.patientFullName_lbl_4 = QtWidgets.QLabel(self.tab)
        self.patientFullName_lbl_4.setGeometry(QtCore.QRect(430, 120, 101, 41))
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
        self.patientFullName_lbl_5 = QtWidgets.QLabel(self.tab)
        self.patientFullName_lbl_5.setGeometry(QtCore.QRect(430, 170, 101, 41))
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
        self.patientFullName_lbl_6 = QtWidgets.QLabel(self.tab)
        self.patientFullName_lbl_6.setGeometry(QtCore.QRect(430, 220, 101, 41))
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
        self.patientFullName_lbl_7 = QtWidgets.QLabel(self.tab)
        self.patientFullName_lbl_7.setGeometry(QtCore.QRect(430, 270, 101, 91))
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
        self.editMedicalRecord_btn = QtWidgets.QPushButton(self.tab)
        self.editMedicalRecord_btn.setGeometry(QtCore.QRect(340, 380, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.editMedicalRecord_btn.setFont(font)
        self.editMedicalRecord_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.editMedicalRecord_btn.setStyleSheet("QPushButton {\n"
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
        self.editMedicalRecord_btn.setObjectName("editMedicalRecord_btn")
        self.deleteMedicalRecord_btn = QtWidgets.QPushButton(self.tab)
        self.deleteMedicalRecord_btn.setGeometry(QtCore.QRect(450, 380, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.deleteMedicalRecord_btn.setFont(font)
        self.deleteMedicalRecord_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.deleteMedicalRecord_btn.setStyleSheet("QPushButton{\n"
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
        self.deleteMedicalRecord_btn.setObjectName("deleteMedicalRecord_btn")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.image_lbl = QtWidgets.QLabel(self.tab_2)
        self.image_lbl.setGeometry(QtCore.QRect(30, 20, 481, 301))
        self.image_lbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.image_lbl.setText("")
        self.image_lbl.setPixmap(QtGui.QPixmap("../../../../Downloads/blank-profile-picture-973460_1920.png"))
        self.image_lbl.setScaledContents(False)
        self.image_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.image_lbl.setWordWrap(False)
        self.image_lbl.setObjectName("image_lbl")
        self.patientFullName_lbl_8 = QtWidgets.QLabel(self.tab_2)
        self.patientFullName_lbl_8.setGeometry(QtCore.QRect(430, 340, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(10)
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
        self.imageName_lbl = QtWidgets.QLabel(self.tab_2)
        self.imageName_lbl.setGeometry(QtCore.QRect(200, 340, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Medium")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.imageName_lbl.setFont(font)
        self.imageName_lbl.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(232, 232, 232);\n"
"background-color: rgb(233, 236, 239);\n"
"border-radius: 10px;\n"
"border-color: rgb(206, 206, 206); ")
        self.imageName_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.imageName_lbl.setObjectName("imageName_lbl")
        self.deleteImage_btn = QtWidgets.QPushButton(self.tab_2)
        self.deleteImage_btn.setEnabled(True)
        self.deleteImage_btn.setGeometry(QtCore.QRect(360, 390, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.deleteImage_btn.setFont(font)
        self.deleteImage_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.deleteImage_btn.setStyleSheet("QPushButton{\n"
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
"QPushButton:disabled {\n"
"    background-color: #d6d6d6; /* Gray background */\n"
"    color: #a1a1a1; /* Light gray text */\n"
"    border: none;\n"
"}\n"
"")
        self.deleteImage_btn.setObjectName("deleteImage_btn")
        self.nextImage_btn = QtWidgets.QPushButton(self.tab_2)
        self.nextImage_btn.setEnabled(True)
        self.nextImage_btn.setGeometry(QtCore.QRect(270, 390, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.nextImage_btn.setFont(font)
        self.nextImage_btn.setStyleSheet("QPushButton {\n"
"    background-color: #17a2b8;\n"
"    color: white; /* White text */\n"
"    border: none;\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(20, 141, 159);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(15, 110, 125);\n"
"    background-color: #004085; \n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #d6d6d6; /* Gray background */\n"
"    color: #a1a1a1; /* Light gray text */\n"
"    border: none;\n"
"}")
        self.nextImage_btn.setObjectName("nextImage_btn")
        self.addImage_btn = QtWidgets.QPushButton(self.tab_2)
        self.addImage_btn.setGeometry(QtCore.QRect(180, 390, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.addImage_btn.setFont(font)
        self.addImage_btn.setStyleSheet("QPushButton {\n"
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
        self.addImage_btn.setObjectName("addImage_btn")
        self.patientFullName_lbl_9 = QtWidgets.QLabel(self.tab_2)
        self.patientFullName_lbl_9.setGeometry(QtCore.QRect(90, 340, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.patientFullName_lbl_9.setFont(font)
        self.patientFullName_lbl_9.setStyleSheet("border: 1px solid;\n"
"border-radius: 10px;\n"
"border-color: rgb(232, 232, 232);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(42, 98, 167);\n"
"\n"
"")
        self.patientFullName_lbl_9.setAlignment(QtCore.Qt.AlignCenter)
        self.patientFullName_lbl_9.setObjectName("patientFullName_lbl_9")
        self.imageCount_lbl = QtWidgets.QLabel(self.tab_2)
        self.imageCount_lbl.setGeometry(QtCore.QRect(30, 340, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.imageCount_lbl.setFont(font)
        self.imageCount_lbl.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(232, 232, 232);\n"
"background-color: rgb(233, 236, 239);\n"
"border-radius: 10px;\n"
"border-color: rgb(206, 206, 206); ")
        self.imageCount_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.imageCount_lbl.setObjectName("imageCount_lbl")
        self.viewImage_btn = QtWidgets.QPushButton(self.tab_2)
        self.viewImage_btn.setGeometry(QtCore.QRect(130, 390, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.viewImage_btn.setFont(font)
        self.viewImage_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.viewImage_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(204, 204, 204);\n"
"    \n"
"    background-color: rgb(230, 230, 230);\n"
"    border: none;\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(199, 199, 199);\n"
"\n"
"   \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(143, 143, 143);\n"
"}\n"
"  \n"
"\n"
"")
        self.viewImage_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/image (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewImage_btn.setIcon(icon)
        self.viewImage_btn.setIconSize(QtCore.QSize(30, 35))
        self.viewImage_btn.setObjectName("viewImage_btn")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(medicalRecordInfo_form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(medicalRecordInfo_form)

    def retranslateUi(self, medicalRecordInfo_form):
        _translate = QtCore.QCoreApplication.translate
        medicalRecordInfo_form.setWindowTitle(_translate("medicalRecordInfo_form", "اطلاعات خدمات بیمار"))
        self.patientFullName_lbl.setText(_translate("medicalRecordInfo_form", "-"))
        self.patientFullName_lbl_2.setText(_translate("medicalRecordInfo_form", "نام بیمار"))
        self.date_lbl.setText(_translate("medicalRecordInfo_form", "-"))
        self.doctorName_lbl.setText(_translate("medicalRecordInfo_form", "-"))
        self.serviceName_lbl.setText(_translate("medicalRecordInfo_form", "-"))
        self.price_lbl.setText(_translate("medicalRecordInfo_form", "-"))
        self.description_lbl.setHtml(_translate("medicalRecordInfo_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Vazirmatn\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Vazirmatn,sans-serif\'; font-size:12pt;\">-</span></p></body></html>"))
        self.patientFullName_lbl_3.setText(_translate("medicalRecordInfo_form", "تاریخ"))
        self.patientFullName_lbl_4.setText(_translate("medicalRecordInfo_form", "دکتر"))
        self.patientFullName_lbl_5.setText(_translate("medicalRecordInfo_form", "سرویس"))
        self.patientFullName_lbl_6.setText(_translate("medicalRecordInfo_form", "مبلغ"))
        self.patientFullName_lbl_7.setText(_translate("medicalRecordInfo_form", "توضیحات"))
        self.editMedicalRecord_btn.setText(_translate("medicalRecordInfo_form", "ویرایش "))
        self.deleteMedicalRecord_btn.setText(_translate("medicalRecordInfo_form", "حذف "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("medicalRecordInfo_form", "اطلاعات خدمات"))
        self.patientFullName_lbl_8.setText(_translate("medicalRecordInfo_form", "نام تصویر"))
        self.imageName_lbl.setText(_translate("medicalRecordInfo_form", "-"))
        self.deleteImage_btn.setText(_translate("medicalRecordInfo_form", "حذف "))
        self.nextImage_btn.setText(_translate("medicalRecordInfo_form", "تصویر بعد"))
        self.addImage_btn.setText(_translate("medicalRecordInfo_form", "افزودن تصویر"))
        self.patientFullName_lbl_9.setText(_translate("medicalRecordInfo_form", "تعداد کل تصاویر"))
        self.imageCount_lbl.setText(_translate("medicalRecordInfo_form", "-"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("medicalRecordInfo_form", "تصاویر خدمات"))

        _translate = QtCore.QCoreApplication.translate
        medicalRecordInfo_form.setWindowTitle(_translate("medicalRecordInfo_form", "اطلاعات خدمات بیمار"))
        self.patientFullName_lbl.setText(_translate("medicalRecordInfo_form", "-"))
        self.patientFullName_lbl_2.setText(_translate("medicalRecordInfo_form", "نام بیمار"))
        self.date_lbl.setText(_translate("medicalRecordInfo_form", "-"))
        self.doctorName_lbl.setText(_translate("medicalRecordInfo_form", "-"))
        self.serviceName_lbl.setText(_translate("medicalRecordInfo_form", "-"))
        self.price_lbl.setText(_translate("medicalRecordInfo_form", "-"))
        self.description_lbl.setHtml(_translate("medicalRecordInfo_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Vazirmatn\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Vazirmatn,sans-serif\'; font-size:12pt;\">-</span></p></body></html>"))
        self.patientFullName_lbl_3.setText(_translate("medicalRecordInfo_form", "تاریخ"))
        self.patientFullName_lbl_4.setText(_translate("medicalRecordInfo_form", "دکتر"))
        self.patientFullName_lbl_5.setText(_translate("medicalRecordInfo_form", "سرویس"))
        self.patientFullName_lbl_6.setText(_translate("medicalRecordInfo_form", "مبلغ"))
        self.patientFullName_lbl_7.setText(_translate("medicalRecordInfo_form", "توضیحات"))
        self.editMedicalRecord_btn.setText(_translate("medicalRecordInfo_form", "ویرایش "))
        self.deleteMedicalRecord_btn.setText(_translate("medicalRecordInfo_form", "حذف "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("medicalRecordInfo_form", "اطلاعات خدمات"))
        self.patientFullName_lbl_8.setText(_translate("medicalRecordInfo_form", "نام تصویر"))
        self.imageName_lbl.setText(_translate("medicalRecordInfo_form", "-"))
        self.deleteImage_btn.setText(_translate("medicalRecordInfo_form", "حذف "))
        self.nextImage_btn.setText(_translate("medicalRecordInfo_form", "تصویر بعد"))
        self.addImage_btn.setText(_translate("medicalRecordInfo_form", "افزودن تصویر"))
        self.patientFullName_lbl_9.setText(_translate("medicalRecordInfo_form", "تعداد کل تصاویر"))
        self.imageCount_lbl.setText(_translate("medicalRecordInfo_form", "-"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("medicalRecordInfo_form", "تصاویر خدمات"))