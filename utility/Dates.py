import jdatetime
from datetime import timedelta
from utility import Numbers
from utility import Dates,Numbers
from PyQt5.QtCore import QThread, pyqtSignal
import requests

class Dates:

    @staticmethod
    def get_today_date_greg():
        tomorrow = jdatetime.date.today().togregorian()
        return tomorrow.strftime("%Y-%m-%d")

    @staticmethod
    def get_future_date_greg(days_ahead) -> str:
        future = jdatetime.date.today() + timedelta(days=days_ahead)
        return future.togregorian().strftime("%Y-%m-%d")
    
    @staticmethod
    def convert_to_jalali_format(jalali_date_str: str) -> str:
        year, month, day = map(int, jalali_date_str.split('-'))
        date_obj = jdatetime.date(year, month, day)

        weekday_number = date_obj.weekday()
        weekday_persian = Dates.get_persian_weekday(weekday_number)

        persian_date = date_obj.strftime("%Y/%m/%d")
        persian_date_formatted = Numbers.english_to_persian_numbers(persian_date)

        return f"{weekday_persian} {persian_date_formatted}"

    @staticmethod
    def get_future_date(days_ahead) -> str:
        future = jdatetime.date.today() + timedelta(days=days_ahead)
        return future.strftime("%Y-%m-%d")

    @staticmethod
    def get_persian_weekday(weekday_number: int) -> str:
        weekday_persian_mapping = {
            0: 'شنبه',
            1: 'یک‌شنبه',
            2: 'دوشنبه',
            3: 'سه‌شنبه',
            4: 'چهارشنبه',
            5: 'پنج‌شنبه',
            6: 'جمعه'
        }
        return weekday_persian_mapping[weekday_number]

    @staticmethod
    def get_jalali_current_month_interval_based_on_greg():
        today = jdatetime.date.today()
        last_day_of_month = Dates.get_last_day_of_month_date(today).togregorian()
        first_day_of_month = jdatetime.date(today.year, today.month, 1).togregorian()
        return first_day_of_month, last_day_of_month

    def get_single_month_intervals(year,month):
        start_day_of_month = jdatetime.date(year, month, 1)
        last_day_of_month = Dates.get_last_day_of_month_date(start_day_of_month).togregorian()

        return start_day_of_month, last_day_of_month

    @staticmethod
    def get_last_day_of_month_date(date):
        if date.month < 7:
            last_day = 31
        elif date.month < 12:
            last_day = 30
        else:
            last_day = 30 if date.isleap() else 29
        return date.replace(day=last_day)

    @staticmethod
    def get_persian_month_fa(month_number: int):
        month_persian_mapping = {
            1: 'فروردین',
            2: 'اردیبشهت',
            3: 'خرداد',
            4: 'تیر',
            5: 'مرداد',
            6: 'شهریور',
            7: 'مهر',
            8: 'آبان',
            9: 'آذر',
            10: 'دی',
            11: 'بهمن',
            12: 'اسفند'
        }
        return month_persian_mapping[month_number]

    @staticmethod
    def get_year_monthly_intervals(year):
        interval = {}
        for month in range(1, 13):
            start_month_interval = jdatetime.date(year, month, 1)
            end_month_interval = Dates.get_last_day_of_month_date(start_month_interval)
            month_fa = Dates.get_persian_month_fa(month)
            interval[month_fa] = {
                "start_date": start_month_interval.togregorian(),
                "end_date": end_month_interval.togregorian()
            }
        return interval

    @staticmethod
    def get_year_interval(year):
        first_day_year = jdatetime.date(year, 1, 1).togregorian()
        last_day_year = Dates.get_last_day_of_month_date(jdatetime.date(year, 12, 1)).togregorian()
        return first_day_year,last_day_year

    @staticmethod 
    def get_date_interval(year,fromMonth, toMonth):
        first_day = jdatetime.date(year, fromMonth, 1).togregorian()
        last_day = Dates.get_last_day_of_month_date(jdatetime.date(year, toMonth, 1)).togregorian()
        return first_day, last_day
    
    @staticmethod
    def get_multi_month_intervals(year, from_month, to_month):
        interval = {}
        for month in range(from_month, to_month + 1):
            start_month_interval = jdatetime.date(year, month, 1)
            end_month_interval = Dates.get_last_day_of_month_date(start_month_interval)
            month_fa = Dates.get_persian_month_fa(month)
            interval[month_fa] = {
                "start_date": start_month_interval.togregorian(),
                "end_date": end_month_interval.togregorian()
            }
        return interval


class FetchTodayDateEventWorker(QThread):
    error_signal = pyqtSignal(str)
    result_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.today_date = jdatetime.date.today()

    def run(self):
        error_msg = f"""
        واکشی مناسبت‌ها موفقیت آمیز نبود. 
        """
        try:
            url = f"https://holidayapi.ir/jalali/{self.today_date.year}/{self.today_date.month}/{self.today_date.day}"
            res = requests.get(url)
            if res.status_code == 200:
                self.result_signal.emit(res.json())
            else:
                self.error_signal.emit(error_msg)
        except Exception:

            self.error_signal.emit(error_msg)
