from models import DatabaseManager, Doctors, Services
import jdatetime
from PyQt5.QtCore import Qt


class LoadComboBox:

    def __init__(self, ui, worker=None):
        self.ui = ui
        self._start_worker = worker

    def load_doctors_combo_box(self):
        self._start_worker(Doctors.get_all, [], self.populate_doctors_combo_box)

    def populate_doctors_combo_box(self, doctors):
        for doctor in doctors:
            full_name = f"{doctor["firstName"]} {doctor["lastName"]}"
            self.ui.doctor_cmbox.addItem(f"دکتر {full_name}", doctor["id"])

    def load_services_combo_box(self):
        self._start_worker(Services.get_all, [], self.populate_services_combo_box)

    def populate_services_combo_box(self, services):
        for service in services:
            self.ui.service_cmbox.addItem(service["name"], service["id"])
            self.ui.service_cmbox.setItemData(
                self.ui.service_cmbox.count() - 1, service["price"], Qt.UserRole + 1
            )

    def load_doctors_services_combo_boxes(self):
        self.load_doctors_combo_box()
        self.load_services_combo_box()

class LoadSpinBox:

    @staticmethod
    def set_current_date_into_date_spin_boxes(ui, date_spnbox_names=None):
        if not date_spnbox_names:
            date_spnbox_names = {
                "year": "year_spnbox",
                "month": "month_spnbox",
                "day": "day_spnbox",
            }

        current_date = jdatetime.date.today()
        getattr(ui, date_spnbox_names["year"]).setValue(current_date.year)
        getattr(ui, date_spnbox_names["month"]).setValue(current_date.month)
        getattr(ui, date_spnbox_names["day"]).setValue(current_date.day)

    @staticmethod
    def load_date_into_date_spinboxes(ui, date: str):
        year, month, day = map(int, date.split("-"))
        ui.year_spnbox.setValue(year)
        ui.month_spnbox.setValue(month)
        ui.day_spnbox.setValue(day)

    @staticmethod
    def load_time_into_time_spinboxes(ui, time: str):
        hour, minute = map(int, time.split(":"))
        ui.hour_spnbox.setValue(hour)
        ui.minute_spnbox.setValue(minute)