from models import DatabaseManager,Doctors,Services
import jdatetime
from PyQt5.QtCore import Qt

class LoadingValues:
    @staticmethod
    def load_doctors_services_combo_boxes(ui):
        with DatabaseManager() as db:
            ui.doctor_cmbox.clear()
            doctors =  Doctors.get_all(db)
            for doctor in doctors:
                full_name = f"{doctor["firstName"]} {doctor["lastName"]}"
                ui.doctor_cmbox.addItem(f"دکتر {full_name}", doctor["id"])

            ui.service_cmbox.clear()
            services = Services.get_all(db)
            for service in services:
                ui.service_cmbox.addItem(service["name"],service["id"])
                ui.service_cmbox.setItemData(ui.service_cmbox.count() - 1, service["price"], Qt.UserRole + 1)
        
    @staticmethod
    def load_current_date_spin_box_values(ui, date_spnbox_names=None):
        if not date_spnbox_names:
            date_spnbox_names = {
                "year": "year_spnbox",
                "month": "month_spnbox",
                "day": "day_spnbox"
            }

        current_date = jdatetime.date.today()
        getattr(ui,date_spnbox_names["year"]).setValue(current_date.year)
        getattr(ui,date_spnbox_names["month"]).setValue(current_date.month)
        getattr(ui,date_spnbox_names["day"]).setValue(current_date.day)

    @staticmethod
    def load_date_into_date_spinbox(ui,date: str):
        year, month, day = map(int, date.split('-'))
        ui.year_spnbox.setValue(year)
        ui.month_spnbox.setValue(month)
        ui.day_spnbox.setValue(day)

    @staticmethod
    def load_time_into_time_spnbox(ui,time: str):
        hour, minute = map(int, time.split(':'))
        ui.hour_spnbox.setValue(hour)
        ui.minute_spnbox.setValue(minute)