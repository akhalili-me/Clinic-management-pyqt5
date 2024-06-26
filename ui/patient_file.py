# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patient_file.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_patientFile_form(object):
    def setupUi(self, patientFile_form):
        patientFile_form.setObjectName("patientFile_form")
        patientFile_form.resize(1636, 719)
        patientFile_form.setMinimumSize(QtCore.QSize(1636, 719))
        patientFile_form.setMaximumSize(QtCore.QSize(1636, 719))
        self.addNewMedicalRecord_btn = QtWidgets.QPushButton(patientFile_form)
        self.addNewMedicalRecord_btn.setGeometry(QtCore.QRect(1120, 660, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn,sans-serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.addNewMedicalRecord_btn.setFont(font)
        self.addNewMedicalRecord_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.addNewMedicalRecord_btn.setStyleSheet("QPushButton {\n"
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
        self.addNewMedicalRecord_btn.setObjectName("addNewMedicalRecord_btn")
        self.userMedicalRecords_lst = QtWidgets.QListWidget(patientFile_form)
        self.userMedicalRecords_lst.setGeometry(QtCore.QRect(10, 50, 461, 661))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn,sans-serif")
        font.setPointSize(12)
        self.userMedicalRecords_lst.setFont(font)
        self.userMedicalRecords_lst.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.userMedicalRecords_lst.setStyleSheet("/* Basic ListWidget styling */\n"
"QListWidget {\n"
"    background-color: #f8f9fa; /* Light grey background */\n"
"    border: 1px solid #dee2e6; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 5px; /* Padding inside the list */\n"
"    font-family: \'Vazirmatn\', sans-serif; /* Font family */\n"
"    outline: 0; /* Remove focus indicator */\n"
"}\n"
"\n"
"/* Item styling */\n"
"QListWidget::item {\n"
"    padding: 10px 5px; /* Padding for each item */\n"
"    margin: 5px 0; /* Margin between items */\n"
"    background-color: #ffffff; /* White background for items */\n"
"    border-radius: 5px; /* Rounded corners for items */\n"
"    color: #343a40; /* Dark grey text color */\n"
"    outline: 0; /* Remove focus indicator */\n"
"}\n"
"\n"
"/* Hover effect for items */\n"
"QListWidget::item:hover {\n"
"    background-color: #e9ecef; /* Light grey background on hover */\n"
"}\n"
"\n"
"/* Selected item styling */\n"
"QListWidget::item:selected {\n"
"    background-color: #0050a5;\n"
"    color: white;\n"
"}\n"
"\n"
"/* Scroll bar styling */\n"
"QScrollBar:vertical {\n"
"    background: #f8f9fa; /* Light grey background for the scroll bar */\n"
"    width: 12px; /* Width of the vertical scroll bar */\n"
"    margin: 22px 0 22px 0; /* Margin to fit the top and bottom arrows */\n"
"    border: 1px solid #dee2e6; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #ced4da; /* Medium grey handle */\n"
"    min-height: 20px; /* Minimum height of the handle */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: #ced4da; /* Medium grey for arrows */\n"
"    height: 20px;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top;\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.userMedicalRecords_lst.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.userMedicalRecords_lst.setObjectName("userMedicalRecords_lst")
        item = QtWidgets.QListWidgetItem()
        self.userMedicalRecords_lst.addItem(item)
        self.label_39 = QtWidgets.QLabel(patientFile_form)
        self.label_39.setGeometry(QtCore.QRect(1240, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(16)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.line = QtWidgets.QFrame(patientFile_form)
        self.line.setGeometry(QtCore.QRect(997, 110, 621, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.firstName_lbl = QtWidgets.QLabel(patientFile_form)
        self.firstName_lbl.setGeometry(QtCore.QRect(1000, 60, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(14)
        self.firstName_lbl.setFont(font)
        self.firstName_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.firstName_lbl.setObjectName("firstName_lbl")
        self.label_35 = QtWidgets.QLabel(patientFile_form)
        self.label_35.setGeometry(QtCore.QRect(1510, 60, 101, 62))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(17)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.line_2 = QtWidgets.QFrame(patientFile_form)
        self.line_2.setGeometry(QtCore.QRect(1000, 190, 611, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lastName_lbl = QtWidgets.QLabel(patientFile_form)
        self.lastName_lbl.setGeometry(QtCore.QRect(1006, 130, 491, 62))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(14)
        self.lastName_lbl.setFont(font)
        self.lastName_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lastName_lbl.setObjectName("lastName_lbl")
        self.label_38 = QtWidgets.QLabel(patientFile_form)
        self.label_38.setGeometry(QtCore.QRect(1510, 130, 101, 62))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(13)
        self.label_38.setFont(font)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.gender_lbl = QtWidgets.QLabel(patientFile_form)
        self.gender_lbl.setGeometry(QtCore.QRect(995, 210, 501, 62))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(14)
        self.gender_lbl.setFont(font)
        self.gender_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.gender_lbl.setObjectName("gender_lbl")
        self.label_41 = QtWidgets.QLabel(patientFile_form)
        self.label_41.setGeometry(QtCore.QRect(1510, 210, 101, 62))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(16)
        self.label_41.setFont(font)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.age_lbl = QtWidgets.QLabel(patientFile_form)
        self.age_lbl.setGeometry(QtCore.QRect(1005, 290, 491, 61))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(14)
        self.age_lbl.setFont(font)
        self.age_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.age_lbl.setObjectName("age_lbl")
        self.label_43 = QtWidgets.QLabel(patientFile_form)
        self.label_43.setGeometry(QtCore.QRect(1510, 290, 101, 62))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(17)
        self.label_43.setFont(font)
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.identityCode_lbl = QtWidgets.QLabel(patientFile_form)
        self.identityCode_lbl.setGeometry(QtCore.QRect(1005, 371, 491, 51))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(14)
        self.identityCode_lbl.setFont(font)
        self.identityCode_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.identityCode_lbl.setObjectName("identityCode_lbl")
        self.label_45 = QtWidgets.QLabel(patientFile_form)
        self.label_45.setGeometry(QtCore.QRect(1510, 360, 101, 62))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(16)
        self.label_45.setFont(font)
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.phoneNumber_lbl = QtWidgets.QLabel(patientFile_form)
        self.phoneNumber_lbl.setGeometry(QtCore.QRect(1005, 441, 481, 51))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(14)
        self.phoneNumber_lbl.setFont(font)
        self.phoneNumber_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.phoneNumber_lbl.setObjectName("phoneNumber_lbl")
        self.label_47 = QtWidgets.QLabel(patientFile_form)
        self.label_47.setGeometry(QtCore.QRect(1510, 430, 101, 62))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(13)
        self.label_47.setFont(font)
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.extraInfo_lbl = QtWidgets.QLabel(patientFile_form)
        self.extraInfo_lbl.setGeometry(QtCore.QRect(1001, 511, 491, 51))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        self.extraInfo_lbl.setFont(font)
        self.extraInfo_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.extraInfo_lbl.setObjectName("extraInfo_lbl")
        self.a = QtWidgets.QLabel(patientFile_form)
        self.a.setGeometry(QtCore.QRect(1510, 510, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(11)
        self.a.setFont(font)
        self.a.setAlignment(QtCore.Qt.AlignCenter)
        self.a.setObjectName("a")
        self.line_3 = QtWidgets.QFrame(patientFile_form)
        self.line_3.setGeometry(QtCore.QRect(1000, 270, 611, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(patientFile_form)
        self.line_4.setGeometry(QtCore.QRect(1000, 350, 611, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(patientFile_form)
        self.line_5.setGeometry(QtCore.QRect(1000, 420, 611, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(patientFile_form)
        self.line_6.setGeometry(QtCore.QRect(1000, 490, 611, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(patientFile_form)
        self.line_7.setGeometry(QtCore.QRect(1490, 80, 20, 561))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.address_lbl = QtWidgets.QLabel(patientFile_form)
        self.address_lbl.setGeometry(QtCore.QRect(1001, 581, 491, 51))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        self.address_lbl.setFont(font)
        self.address_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.address_lbl.setObjectName("address_lbl")
        self.a_2 = QtWidgets.QLabel(patientFile_form)
        self.a_2.setGeometry(QtCore.QRect(1510, 580, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(16)
        self.a_2.setFont(font)
        self.a_2.setAlignment(QtCore.Qt.AlignCenter)
        self.a_2.setObjectName("a_2")
        self.line_8 = QtWidgets.QFrame(patientFile_form)
        self.line_8.setGeometry(QtCore.QRect(1000, 560, 611, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.editPatient_btn = QtWidgets.QPushButton(patientFile_form)
        self.editPatient_btn.setGeometry(QtCore.QRect(1340, 660, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn,sans-serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.editPatient_btn.setFont(font)
        self.editPatient_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.editPatient_btn.setStyleSheet("QPushButton {\n"
"    background-color: #ffc107; /* Bootstrap warning yellow */\n"
"    color: #212529; /* Dark text */\n"
"    border: none;\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-weight: bold; /* Bold text */\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-family: \'Vazirmatn\', sans-serif; /* Font family */\n"
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
        self.editPatient_btn.setObjectName("editPatient_btn")
        self.label_40 = QtWidgets.QLabel(patientFile_form)
        self.label_40.setGeometry(QtCore.QRect(110, 10, 211, 31))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(16)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.deletePatient_btn = QtWidgets.QPushButton(patientFile_form)
        self.deletePatient_btn.setGeometry(QtCore.QRect(1530, 660, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn,sans-serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.deletePatient_btn.setFont(font)
        self.deletePatient_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.deletePatient_btn.setStyleSheet("QPushButton{\n"
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
        self.deletePatient_btn.setObjectName("deletePatient_btn")
        self.addAppointment_btn = QtWidgets.QPushButton(patientFile_form)
        self.addAppointment_btn.setGeometry(QtCore.QRect(1000, 660, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn,sans-serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.addAppointment_btn.setFont(font)
        self.addAppointment_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.addAppointment_btn.setStyleSheet("QPushButton {\n"
"    background-color: #17a2b8; /* Bootstrap info blue */\n"
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
"    background-color: #138496; /* Darker blue on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #117a8b; /* Even darker blue on press */\n"
"}\n"
"")
        self.addAppointment_btn.setObjectName("addAppointment_btn")
        self.label_42 = QtWidgets.QLabel(patientFile_form)
        self.label_42.setGeometry(QtCore.QRect(580, 10, 211, 31))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(16)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.userAppointments_lst = QtWidgets.QListWidget(patientFile_form)
        self.userAppointments_lst.setGeometry(QtCore.QRect(490, 50, 501, 661))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn,sans-serif")
        font.setPointSize(12)
        self.userAppointments_lst.setFont(font)
        self.userAppointments_lst.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.userAppointments_lst.setStyleSheet("/* Basic ListWidget styling */\n"
"QListWidget {\n"
"    background-color: #f8f9fa; /* Light grey background */\n"
"    border: 1px solid #dee2e6; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 5px; /* Padding inside the list */\n"
"    font-family: \'Vazirmatn\', sans-serif; /* Font family */\n"
"    outline: 0; /* Remove focus indicator */\n"
"}\n"
"\n"
"/* Item styling */\n"
"QListWidget::item {\n"
"    padding: 10px 5px; /* Padding for each item */\n"
"    margin: 5px 0; /* Margin between items */\n"
"    background-color: #ffffff; /* White background for items */\n"
"    border-radius: 5px; /* Rounded corners for items */\n"
"    color: #343a40; /* Dark grey text color */\n"
"    outline: 0; /* Remove focus indicator */\n"
"}\n"
"\n"
"/* Hover effect for items */\n"
"QListWidget::item:hover {\n"
"    background-color: #e9ecef; /* Light grey background on hover */\n"
"}\n"
"\n"
"/* Selected item styling */\n"
"QListWidget::item:selected {\n"
"    background-color: #0050a5;\n"
"    color: white;\n"
"}\n"
"\n"
"/* Scroll bar styling */\n"
"QScrollBar:vertical {\n"
"    background: #f8f9fa; /* Light grey background for the scroll bar */\n"
"    width: 12px; /* Width of the vertical scroll bar */\n"
"    margin: 22px 0 22px 0; /* Margin to fit the top and bottom arrows */\n"
"    border: 1px solid #dee2e6; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #ced4da; /* Medium grey handle */\n"
"    min-height: 20px; /* Minimum height of the handle */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: #ced4da; /* Medium grey for arrows */\n"
"    height: 20px;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top;\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.userAppointments_lst.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.userAppointments_lst.setObjectName("userAppointments_lst")
        item = QtWidgets.QListWidgetItem()
        self.userAppointments_lst.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.userAppointments_lst.addItem(item)
        self.line_9 = QtWidgets.QFrame(patientFile_form)
        self.line_9.setGeometry(QtCore.QRect(470, 50, 20, 661))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")

        self.retranslateUi(patientFile_form)
        QtCore.QMetaObject.connectSlotsByName(patientFile_form)

    def retranslateUi(self, patientFile_form):
        _translate = QtCore.QCoreApplication.translate
        patientFile_form.setWindowTitle(_translate("patientFile_form", "پرونده بیمار"))
        self.addNewMedicalRecord_btn.setText(_translate("patientFile_form", "افزودن خدمات جدید به پرونده"))
        __sortingEnabled = self.userMedicalRecords_lst.isSortingEnabled()
        self.userMedicalRecords_lst.setSortingEnabled(False)
        item = self.userMedicalRecords_lst.item(0)
        item.setText(_translate("patientFile_form", "بوتاکس -دکتر احمدی- تاریخ: ۴/۲۳/۱۳۴۵ "))
        self.userMedicalRecords_lst.setSortingEnabled(__sortingEnabled)
        self.label_39.setText(_translate("patientFile_form", "اطلاعات بیمار"))
        self.firstName_lbl.setText(_translate("patientFile_form", "امیررضا "))
        self.label_35.setText(_translate("patientFile_form", "نام:"))
        self.lastName_lbl.setText(_translate("patientFile_form", "خلیلی"))
        self.label_38.setText(_translate("patientFile_form", "نام خانوادگی:"))
        self.gender_lbl.setText(_translate("patientFile_form", "مرد"))
        self.label_41.setText(_translate("patientFile_form", "جنسیت:"))
        self.age_lbl.setText(_translate("patientFile_form", "۲۳"))
        self.label_43.setText(_translate("patientFile_form", "سن: "))
        self.identityCode_lbl.setText(_translate("patientFile_form", "۱۸۳۰۶۸۲۰۰۸"))
        self.label_45.setText(_translate("patientFile_form", "کد ملی:"))
        self.phoneNumber_lbl.setText(_translate("patientFile_form", "۰۹۰۱۲۷۲۳۵۸۹۹"))
        self.label_47.setText(_translate("patientFile_form", "شماره تلفن:"))
        self.extraInfo_lbl.setText(_translate("patientFile_form", "مبتلا به تنگی نفس"))
        self.a.setText(_translate("patientFile_form", "اطلاعات اضافه:"))
        self.address_lbl.setText(_translate("patientFile_form", "اهواز باغملک خیابان ۳ رشت"))
        self.a_2.setText(_translate("patientFile_form", "آدرس:"))
        self.editPatient_btn.setText(_translate("patientFile_form", "ویرایش اطلاعات بیمار"))
        self.label_40.setText(_translate("patientFile_form", "خدمات ارائه شده به بیمار"))
        self.deletePatient_btn.setText(_translate("patientFile_form", "حذف "))
        self.addAppointment_btn.setText(_translate("patientFile_form", "افزودن نوبت"))
        self.label_42.setText(_translate("patientFile_form", "نوبت‌های بیمار"))
        __sortingEnabled = self.userAppointments_lst.isSortingEnabled()
        self.userAppointments_lst.setSortingEnabled(False)
        item = self.userAppointments_lst.item(0)
        item.setText(_translate("patientFile_form", "بوتاکس -دکتر احمدی- تاریخ: ۴/۲۳/۱۳۴۵ "))
        item = self.userAppointments_lst.item(1)
        item.setText(_translate("patientFile_form", "sdf"))
        self.userAppointments_lst.setSortingEnabled(__sortingEnabled)
