import jdatetime
from datetime import timedelta
from utility import Numbers
class Dates:
    @staticmethod
    def convert_to_jalali_format(date_str: str) -> str:
        year, month, day = map(int, date_str.split('-'))
        date_obj = jdatetime.date(year, month, day)

        weekday_number = date_obj.weekday()
        weekday_persian = Dates.get_persian_weekday(weekday_number)

        persian_date = date_obj.strftime("%Y/%m/%d")
        persian_date_formatted = Numbers.english_to_persian_numbers(persian_date)

        return f"{weekday_persian} {persian_date_formatted}"

    @staticmethod
    def get_future_date(days_ahead) -> str:
        tomorrow = jdatetime.date.today() + timedelta(days=days_ahead)
        return tomorrow.strftime("%Y-%m-%d")

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
            6: 'شهرویر',
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