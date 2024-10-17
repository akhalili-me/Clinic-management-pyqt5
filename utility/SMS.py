# from kavenegar import *
from utility import Dates

class SMS:
    @staticmethod
    def send_appointment_reminder_sms(appointment):
        # api = KavenegarAPI('Your API Key')
        persian_format_date = Dates.convert_to_jalali_format(appointment["jalali_date"])
        message = f"""
        سلام زیبای جوی عزیز
        شما برای تاریخ {persian_format_date} یک نوبت {appointment["service_name"]} رزرو شده دارید.
        منتظر حضور شما در کلینیک زیبایی رویتا هستیم.  
        """
    
        params = {
            'sender': '1000xxxx',
            'receptor' : '0919xxxxxx',
            'message' : message
        }   

        # response = api.sms_send(params)
        return 
        