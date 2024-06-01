from PyQt5.QtWidgets import QDialog
from ui import Ui_MainWindow,Ui_addEditAppointment_form
from models.db import DatabaseManager
from PyQt5.QtWidgets import QMessageBox
from models import Doctors,Services,Appointments,Patients
from PyQt5.QtCore import pyqtSignal
from utility import LoadingValues,Dates,Numbers
from PyQt5.QtWidgets import QListWidgetItem
import jdatetime
from utility import Dates

class AppointmentsTabController:
    def __init__(self, ui:Ui_MainWindow):
        self.ui = ui

        LoadingValues.load_date_spin_box_values(self.ui)
        self.load_today_appointments_list()
        
        # Connecting buttons
        self.ui.AppointmentSearchByDate_btn.clicked.connect(self.search_appointments_by_date)
        self.ui.todayAppointmentSearch_btn.clicked.connect(self.load_today_appointments_list)
        self.ui.tomorrowAppointmentSearch_btn.clicked.connect(self.load_tommorow_appointments_list)
        self.ui.twoDayAppointmentSearch_btn.clicked.connect(self.load_two_day_ahead_appointments)
        self.ui.threeDayAppointmentSearch_btn.clicked.connect(self.load_three_day_ahead_appointments)
        self.ui.fourDayAppointmentSearch_btn.clicked.connect(self.load_four_day_ahead_appointments)

    def load_tommorow_appointments_list(self):
        self._load_future_date_appointments(days_ahead=1)

    def load_two_day_ahead_appointments(self):
        self._load_future_date_appointments(days_ahead=2)

    def load_three_day_ahead_appointments(self):
        self._load_future_date_appointments(days_ahead=3)

    def load_four_day_ahead_appointments(self):
        self._load_future_date_appointments(days_ahead=4)

    def _load_future_date_appointments(self,days_ahead):
        date = Dates.get_future_date(days_ahead)

        with DatabaseManager() as db:
            appointments = Appointments.get_by_date(db,date)
            self._load_data_into_appointment_list(db,appointments)

    def search_appointments_by_date(self):
        year = self.ui.year_spnbox.value()
        month = self.ui.month_spnbox.value()
        day = self.ui.day_spnbox.value()
        date_str = jdatetime.date(year,month,day).strftime("%Y-%m-%d")

        with DatabaseManager() as db:
            appointments = Appointments.get_by_date(db,date_str)
            self._load_data_into_appointment_list(db,appointments)

    def load_today_appointments_list(self):
        self.ui.appointments_lst.clear()
        LoadingValues.load_date_spin_box_values(self.ui)
        today_date = jdatetime.date.today().strftime("%Y-%m-%d")

        with DatabaseManager() as db:
            today_appointments = Appointments.get_by_date(db,today_date)
            self._load_data_into_appointment_list(db,today_appointments)

    def _load_data_into_appointment_list(self,db,appointments):
        self.ui.appointments_lst.clear()
        for appointment in appointments:
            service = Services.get_by_id(db,appointment["service"])
            doctor = Doctors.get_by_id(db, appointment["doctor"])
            patient = Patients.get_by_id(db,appointment["patient"])
            patient_full_name = f"{patient["firstName"]} {patient["lastName"]}"
            date = Dates.convert_to_jalali_format(appointment["jalali_date"])
            time = Numbers.english_to_persian_numbers(appointment["time"])
            description = appointment['description'] or "بدون توضیحات"
            item_txt = f"{patient_full_name} | {service['name']} | دکتر {doctor['lastName']} | {appointment['status']} | {date} | {time} | {description}"
            item = QListWidgetItem(item_txt)
            item.setData(1,appointment["id"])
            self.ui.appointments_lst.addItem(item)


class AddEditAppointmentController(QDialog):
    refresh_appointment_list = pyqtSignal()

    def __init__(self,patient_id):
        super(AddEditAppointmentController, self).__init__()
        self.ui = Ui_addEditAppointment_form()
        self.ui.setupUi(self)
        self.setModal(True)

        self.patient_id = patient_id
        
        LoadingValues.load_doctors_services_combo_boxes(self.ui)
        LoadingValues.load_date_spin_box_values(self.ui)

        self.ui.save_btn.clicked.connect(self.save_appointment)
        self.ui.cancel_btn.clicked.connect(self.close)

    def save_appointment(self):
        year = self.ui.year_spnbox.value()
        month = self.ui.month_spnbox.value()
        day = self.ui.day_spnbox.value()
        jalali_date_str = jdatetime.date(year,month,day).strftime("%Y-%m-%d")

        hour = self.ui.hour_spnbox.value()
        minute = self.ui.minute_spnbox.value()
        time_str = f"{hour}:{minute}"

        greg_datetime = jdatetime.datetime(year,month,day,hour,minute).togregorian().strftime('%Y-%m-%d %H:%M')

        appointment = {
            'status': self.ui.status_cmbox.currentText().strip(),
            'jalali_date': jalali_date_str.strip(),
            'greg_datetime': greg_datetime.strip(),
            "time": time_str.strip(),
            "doctor": self.ui.doctor_cmbox.currentData(),
            "service": self.ui.service_cmbox.currentData(),
            "description": self.ui.description_txtbox.toPlainText().strip(),
            "patient": self.patient_id,
        }

        with DatabaseManager() as db:
            Appointments.add_appointment(db,appointment)
            QMessageBox.information(self, "موفقیت", "نوبت با موفقیت اضافه شد.")
            self.refresh_appointment_list.emit()
            self.close()
