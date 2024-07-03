from models import DatabaseManager
from utility import Dates
import jdatetime
from PyQt5.QtChart import (
    QChart,
    QValueAxis,
    QBarCategoryAxis,
    QBarSeries,
    QBarSet,
    QBarCategoryAxis,
    QValueAxis,
)
from PyQt5.QtGui import QPainter,QFont
from PyQt5.QtCore import Qt

class ChartManager:
    def __init__(self, ui):
        self.ui = ui

    def year_bar_chart(self, service_id, year):
        bar_chart = QChart()
        bar_chart.setTitle("نمودار میله‌ای نمایش سالانه درآمد سرویس")
        bar_chart.setAnimationOptions(QChart.SeriesAnimations)

        series = QBarSeries()
        year_intervals = Dates.get_year_monthly_intervals(year)

        report_data = {}

        for month, date in year_intervals.items():
            report_data[month] = self._month_service_count_income(
                service_id, date["start_date"], date["end_date"]
            )

        barset_income = QBarSet("درآمد سرویس")
        
        for month, data in report_data.items():
            total_income = float(data["total_income"]) if data["total_income"] else 0.0
            barset_income.append(total_income)
            
        series.append(barset_income)
        bar_chart.addSeries(series)

        axis_x = QBarCategoryAxis()
        axis_x.append([month for month in report_data.keys()])
        bar_chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        bar_chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        self._apply_fonts_to_chart(bar_chart, axis_x, axis_y)
        self.ui.report_chart.setChart(bar_chart)
        self.ui.report_chart.setRenderHint(QPainter.Antialiasing)


    def _month_service_count_income(self,service_id,start_date,end_date):
        from models import Reports
        with DatabaseManager() as db:
            return Reports.get_monthly_service_income(db, service_id,start_date,end_date)

    def current_month_bar_chart(self, service_id):
        bar_chart = QChart()
        bar_chart.setTitle("نمودار میله‌ای نمایش درآمد سرویس")
        bar_chart.setAnimationOptions(QChart.SeriesAnimations)

        series = QBarSeries()
        report_data = self._get_current_month_service_income_by_days(service_id)

        income_dict = {data['jalali_date']: data['income'] for data in report_data}
        self._fill_missing_days_with_zero(income_dict)

        days_sorted = sorted(income_dict.keys())

        barset_service = QBarSet('درآمد سرویس')
        for day in days_sorted:
            barset_service.append(income_dict[day])
        series.append(barset_service)
        bar_chart.addSeries(series)

        axis_x = self._create_category_axis(days_sorted)
        bar_chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        bar_chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        self._apply_fonts_to_chart(bar_chart, axis_x, axis_y)
        self.ui.report_chart.setChart(bar_chart)
        self.ui.report_chart.setRenderHint(QPainter.Antialiasing)

    def _get_current_month_service_income_by_days(self, service_id):
        from models import Reports
        with DatabaseManager() as db:
            return Reports.get_current_month_service_income_by_days(db, service_id)

    def _fill_missing_days_with_zero(self, income_dict):
        today_date = jdatetime.date.today()
        year_month_str = today_date.strftime("%Y-%m")
        current_month_last_day_date = Dates.get_last_day_of_month_date(today_date)
        days_in_month = list(range(1, current_month_last_day_date.day + 1))

        for day in days_in_month:
            jalali_date = f"{year_month_str}-{day:02}"
            if jalali_date not in income_dict:
                income_dict[jalali_date] = 0

    def _create_category_axis(self, days_sorted):
        axis_x = QBarCategoryAxis()
        axis_x.append([day[-2:] for day in days_sorted])
        return axis_x

    def _apply_fonts_to_chart(self, chart, axis_x, axis_y):
        font = QFont()
        font.setFamily("Vazirmatn ExtraBold")
        font.setPointSize(10)
        chart.setTitleFont(font)
        axis_x.setLabelsFont(font)
        axis_y.setLabelsFont(font)
        chart.legend().setFont(font)

    def clear_chart_view(self):
        chart = self.ui.report_chart.chart()
        chart.removeAllSeries()
        for axis in chart.axes():
            chart.removeAxis(axis)
        chart.setTitle("")
        chart.legend().hide()
