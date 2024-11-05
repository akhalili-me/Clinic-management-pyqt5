# from kavenegar import *
from utility import Dates,Numbers,ConfigUtils,Messages
from PyQt5.QtCore import QThread, pyqtSignal
from kavenegar import *


def get_sms_api_key():
    api_key = ConfigUtils.get_value("sms_api_key")
    if not api_key:
        Messages.show_warning_msg("کلید سرویس پیامکی یافت نشد.")
        return        
    return api_key

class SMS:
    def send_appointment_reminder_sms(api, input_sms_params):
        proccessed_prams = SMS._prepare_sms_params(input_sms_params)

        params = {
            'receptor': proccessed_prams["phone_number"],
            'template': 'appointment',
            'token': proccessed_prams["appointment_datetime"],
            'token2': proccessed_prams["service_name"],
            'token3': proccessed_prams["patient_name"]
        }
        return api.verify_lookup(params)
    
    def _prepare_sms_params(appointment):
        appointment_datetime = (
            f"{Dates.convert_to_jalali_format(appointment['jalali_date']).strip().replace(' ', '-')}"
            f"--ساعت-{Numbers.english_to_persian_numbers(appointment['time'])}".replace(
                " ", "-"
            )
        )
        return {
            "patient_name": appointment["patient_name"].strip().replace(" ", "-"),
            "phone_number": appointment["phone_number"],
            "appointment_datetime": appointment_datetime,
            "service_name": appointment["service_name"].strip().replace(" ", "-"),
        }

class SMSWorker(QThread):
    error_signal = pyqtSignal(str)
    success_signal = pyqtSignal()

    def __init__(self, input_sms_params):
        super().__init__()
        self.api = KavenegarAPI(get_sms_api_key())
        self.input_sms_params = input_sms_params

    def run(self):
        try:
            SMS.send_appointment_reminder_sms(self.api, self.input_sms_params)
            self.success_signal.emit()
        except Exception:
            error_msg = f"""
            ارسال پیامک موفقیت‌آمیز نبود. 
            """
            self.error_signal.emit(error_msg)

class GroupSMSWorker(QThread):
    summary_signal = pyqtSignal(int, int)  
    update_sms_field_signal = pyqtSignal(dict)

    def __init__(self, appointments):
        super().__init__()
        self.api = KavenegarAPI(get_sms_api_key())
        self.appointments = appointments
        self.success_count = 0
        self.failure_count = 0

    def run(self):
        for appointment in self.appointments:
            try:
                SMS.send_appointment_reminder_sms(self.api, appointment)
                self.success_count += 1
                self.update_sms_field_signal.emit({"id": appointment["id"], "sms": appointment["sms"] + 1})
            except Exception:
                self.failure_count += 1

        self.summary_signal.emit(self.success_count, self.failure_count)
