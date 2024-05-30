# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_edit_medical_records.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addEditMedicalRecords_form(object):
    def setupUi(self, addEditMedicalRecords_form):
        addEditMedicalRecords_form.setObjectName("addEditMedicalRecords_form")
        addEditMedicalRecords_form.resize(496, 218)
        self.services_cmbox = QtWidgets.QComboBox(addEditMedicalRecords_form)
        self.services_cmbox.setGeometry(QtCore.QRect(20, 150, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(13)
        self.services_cmbox.setFont(font)
        self.services_cmbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.services_cmbox.setObjectName("services_cmbox")
        self.services_cmbox.addItem("")
        self.doctor_cmbox = QtWidgets.QComboBox(addEditMedicalRecords_form)
        self.doctor_cmbox.setGeometry(QtCore.QRect(20, 110, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(13)
        self.doctor_cmbox.setFont(font)
        self.doctor_cmbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.doctor_cmbox.setObjectName("doctor_cmbox")
        self.doctor_cmbox.addItem("")
        self.groupBox = QtWidgets.QGroupBox(addEditMedicalRecords_form)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 371, 81))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn Black")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.day_spnbox = QtWidgets.QSpinBox(self.groupBox)
        self.day_spnbox.setGeometry(QtCore.QRect(270, 30, 51, 31))
        self.day_spnbox.setMinimum(1)
        self.day_spnbox.setMaximum(31)
        self.day_spnbox.setObjectName("day_spnbox")
        self.label_38 = QtWidgets.QLabel(self.groupBox)
        self.label_38.setGeometry(QtCore.QRect(310, 30, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        self.label_38.setFont(font)
        self.label_38.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_38.setObjectName("label_38")
        self.month_spnbox = QtWidgets.QSpinBox(self.groupBox)
        self.month_spnbox.setGeometry(QtCore.QRect(160, 30, 51, 31))
        self.month_spnbox.setMinimum(1)
        self.month_spnbox.setMaximum(12)
        self.month_spnbox.setObjectName("month_spnbox")
        self.month_lbl = QtWidgets.QLabel(self.groupBox)
        self.month_lbl.setGeometry(QtCore.QRect(199, 30, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        self.month_lbl.setFont(font)
        self.month_lbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.month_lbl.setObjectName("month_lbl")
        self.year_spnbox = QtWidgets.QSpinBox(self.groupBox)
        self.year_spnbox.setGeometry(QtCore.QRect(10, 30, 91, 31))
        self.year_spnbox.setMinimum(1400)
        self.year_spnbox.setMaximum(1500)
        self.year_spnbox.setObjectName("year_spnbox")
        self.label_40 = QtWidgets.QLabel(self.groupBox)
        self.label_40.setGeometry(QtCore.QRect(90, 30, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        self.label_40.setFont(font)
        self.label_40.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(addEditMedicalRecords_form)
        self.label_41.setGeometry(QtCore.QRect(390, 110, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        self.label_41.setFont(font)
        self.label_41.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(addEditMedicalRecords_form)
        self.label_42.setGeometry(QtCore.QRect(390, 150, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(12)
        self.label_42.setFont(font)
        self.label_42.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_42.setObjectName("label_42")

        self.retranslateUi(addEditMedicalRecords_form)
        QtCore.QMetaObject.connectSlotsByName(addEditMedicalRecords_form)

    def retranslateUi(self, addEditMedicalRecords_form):
        _translate = QtCore.QCoreApplication.translate
        addEditMedicalRecords_form.setWindowTitle(_translate("addEditMedicalRecords_form", "اضافه کردن خدمات"))
        self.services_cmbox.setItemText(0, _translate("addEditMedicalRecords_form", "بوتاکس صورت"))
        self.doctor_cmbox.setItemText(0, _translate("addEditMedicalRecords_form", "رضا نجفی"))
        self.groupBox.setTitle(_translate("addEditMedicalRecords_form", "تاریخ"))
        self.label_38.setText(_translate("addEditMedicalRecords_form", "روز:"))
        self.month_lbl.setText(_translate("addEditMedicalRecords_form", "ماه:"))
        self.label_40.setText(_translate("addEditMedicalRecords_form", "سال:"))
        self.label_41.setText(_translate("addEditMedicalRecords_form", "دکتر:"))
        self.label_42.setText(_translate("addEditMedicalRecords_form", "سرویس:"))
