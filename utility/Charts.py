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

    def general_year_bar_chart(self,year):
        bar_chart = QChart()
        bar_chart.setTitle("نمودار میله‌ای نمایش سالانه درآمد، هزینه و سود")
        bar_chart.setAnimationOptions(QChart.SeriesAnimations)

        series = QBarSeries()
        year_intervals = Dates.get_year_monthly_intervals(year)

        report_data = {}

        for month, date in year_intervals.items():
            report_data[month] = self._get_monthly_financial_summary(
                date["start_date"], date["end_date"]
            )
        
        barset_income = QBarSet("درآمد")
        barset_expense = QBarSet("هزینه")
        barset_profit = QBarSet("سود")

        for month, data in report_data.items():
            total_income = float(data["total_income"]) if data["total_income"] else 0.0
            barset_income.append(total_income)

            total_expense = float(data["total_expense"]) if data["total_expense"] else 0.0
            barset_expense.append(total_expense)

            profit = float(data["profit"]) if data["profit"] else 0.0
            barset_profit.append(profit)
            

        series.append(barset_income)
        series.append(barset_expense)
        series.append(barset_profit)
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

    def general_current_month_bar_chart(self):
        bar_chart = QChart()
        bar_chart.setTitle("نمودار میله‌ای نمایش درآمد، هزینه و سود")
        bar_chart.setAnimationOptions(QChart.SeriesAnimations)

        report_data = self._get_current_month_financial_summery_by_days()
        
        financial_dict = {
            data['jalali_date']: {
                'total_income': data['total_income'],
                'total_expense': data['total_expense'],
                'profit': data['profit']
            } for data in report_data
        }
        self._fill_missing_days_with_zero(financial_dict, ['total_income', 'total_expense', 'profit'])

        days_sorted = sorted(financial_dict.keys())

        barset_income = QBarSet('درآمد کل')
        barset_expense = QBarSet('هزینه کل')
        barset_profit = QBarSet('سود کل')

        for day in days_sorted:
            barset_income.append(financial_dict[day]['total_income'])
            barset_expense.append(financial_dict[day]['total_expense'])
            barset_profit.append(financial_dict[day]['profit'])

        series = QBarSeries()
        series.append(barset_income)
        series.append(barset_expense)
        series.append(barset_profit)
        bar_chart.addSeries(series)

        axis_x = self._create_category_axis(days_sorted)
        bar_chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        max_value = max(max(barset_income), max(barset_expense), max(barset_profit))
        min_value = min(min(barset_income), min(barset_expense), min(barset_profit))

        axis_y = QValueAxis()
        axis_y.setRange(min_value, max_value)
        bar_chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        self._apply_fonts_to_chart(bar_chart, axis_x, axis_y)
        self.ui.report_chart.setChart(bar_chart)
        self.ui.report_chart.setRenderHint(QPainter.Antialiasing)

    def _get_current_month_financial_summery_by_days(self):
        from models import Reports
        start_date,end_date = Dates.get_jalali_current_month_interval_based_on_greg()
        with DatabaseManager() as db:
            return Reports.get_financial_summary_by_days(db, start_date, end_date)

    def service_year_bar_chart(self, service_id, year):
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

    def service_current_month_bar_chart(self, service_id):
        bar_chart = QChart()
        bar_chart.setTitle("نمودار میله‌ای نمایش درآمد سرویس")
        bar_chart.setAnimationOptions(QChart.SeriesAnimations)

        series = QBarSeries()
        report_data = self._get_current_month_service_income_by_days(service_id)

        income_dict = {data['jalali_date']: data['income'] for data in report_data}
        self._fill_missing_days_with_zero(income_dict, 'income')

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

    def _create_daily_chart(self, title, days_sorted, data_dict, keys, labels):
        bar_chart = QChart()
        bar_chart.setTitle(title)
        bar_chart.setAnimationOptions(QChart.SeriesAnimations)

        series_dict = {label: QBarSeries() for label in labels}
        barset_dict = {label: QBarSet(label) for label in labels}

        for day in days_sorted:
            for key, label in zip(keys, labels):
                value = data_dict[day] if not isinstance(data_dict[day], dict) else data_dict[day].get(key, 0)
                barset_dict[label].append(value)

        for label in labels:
            series_dict[label].append(barset_dict[label])
            bar_chart.addSeries(series_dict[label])

        axis_x = self._create_category_axis(days_sorted)
        bar_chart.addAxis(axis_x, Qt.AlignBottom)
        for series in series_dict.values():
            series.attachAxis(axis_x)

        max_value = max(max(barset) for barset in barset_dict.values())
        axis_y = QValueAxis()
        axis_y.setMax(max_value)
        bar_chart.addAxis(axis_y, Qt.AlignLeft)
        for series in series_dict.values():
            series.attachAxis(axis_y)

        self._apply_fonts_to_chart(bar_chart, axis_x, axis_y)
        self.ui.report_chart.setChart(bar_chart)
        self.ui.report_chart.setRenderHint(QPainter.Antialiasing)
        
    def _month_service_count_income(self,service_id,start_date,end_date):
        from models import Reports
        with DatabaseManager() as db:
            return Reports.get_monthly_service_income(db, service_id,start_date,end_date)

    def _get_monthly_financial_summary(self,start_date,end_date):
        from models import Reports
        with DatabaseManager() as db:
            return Reports.get_financial_summary(db,start_date,end_date)

    def _get_current_month_service_income_by_days(self, service_id):
        from models import Reports
        with DatabaseManager() as db:
            return Reports.get_current_month_service_income_by_days(db, service_id)

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
    
    def _fill_missing_days_with_zero(self, data_dict, keys):
        today_date = jdatetime.date.today()
        year_month_str = today_date.strftime("%Y-%m")
        current_month_last_day_date = Dates.get_last_day_of_month_date(today_date)
        days_in_month = range(1, current_month_last_day_date.day + 1)

        for day in days_in_month:
            jalali_date = f"{year_month_str}-{day:02}"
            if jalali_date not in data_dict:
                if isinstance(keys, list):
                    data_dict[jalali_date] = {key: 0 for key in keys}
                else:
                    data_dict[jalali_date] = 0