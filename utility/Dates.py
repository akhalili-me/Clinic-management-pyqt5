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
    def get_jalali_last_six_month_interval_based_on_greg():
        today = jdatetime.date.today()
        start_date = (today - jdatetime.timedelta(days=6*30)).replace(day=1)  # Approximation and set to the first day
        end_date = (today.replace(day=1) - jdatetime.timedelta(days=1)).togregorian()  # End of the previous month

        start_date = jdatetime.date(start_date.year, start_date.month, 1).togregorian()
        
        return start_date, end_date

    @staticmethod
    def get_jalali_last_three_month_interval_based_on_greg():
        today = jdatetime.date.today()
        start_date = (today - jdatetime.timedelta(days=3*30)).replace(day=1)  # Approximation and set to the first day
        end_date = (today.replace(day=1) - jdatetime.timedelta(days=1)).togregorian()  # End of the previous month

        start_date = jdatetime.date(start_date.year, start_date.month, 1).togregorian()
        
        return start_date, end_date

    @staticmethod
    def get_jalali_last_year_interval_based_on_greg():
        today = jdatetime.date.today() 
        last_year_date_obj = jdatetime.date(today.year - 1, 1, 1)

        start_date = last_year_date_obj.togregorian()
        end_date = jdatetime.date(today.year - 1, 12, 30 if last_year_date_obj.isleap() else 29).togregorian()
        
        return start_date, end_date
    
    @staticmethod
    def get_jalali_current_year_interval_based_on_greg():
        today = jdatetime.date.today()
        start_date = jdatetime.date(today.year, 1, 1).togregorian()
        
        # Determine the last day of the Jalali year
        end_date = jdatetime.date(today.year, 12, 30 if jdatetime.date.isleap(today) else 29).togregorian()
        
        return start_date, end_date

    def get_last_day_of_month_date(date):
        if date.month < 7:
            last_day = 31
        elif date.month < 12:
            last_day = 30
        else:
            last_day = 30 if date.isleap() else 29
        return date.replace(day=last_day)