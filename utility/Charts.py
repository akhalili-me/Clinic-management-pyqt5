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

    def _create_bar_chart(self, title, series_data, x_axis_labels, label_format="date"):
        bar_chart = QChart()
        bar_chart.setTitle(title)
        bar_chart.setAnimationOptions(QChart.SeriesAnimations)

        series = QBarSeries()
        for label, data in series_data.items():
            barset = QBarSet(label)
            barset.append(data)
            series.append(barset)

        bar_chart.addSeries(series)

        axis_x = QBarCategoryAxis()
        if label_format == "day_only":
            axis_x.append([day[-2:] for day in x_axis_labels])  # Extracting just the day part for single month
        else:
            axis_x.append(x_axis_labels)  # Full date format for multi-month
        bar_chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        bar_chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        self._apply_fonts_to_chart(bar_chart, axis_x, axis_y)
        self.ui.report_chart.setChart(bar_chart)
        self.ui.report_chart.setRenderHint(QPainter.Antialiasing)

    def general_single_month_bar_chart(self, report_data):
        financial_dict = {
            data['jalali_date']: {
                'total_income': data['total_income'],
                'total_expense': data['total_expense'],
                'profit': data['profit']
            } for data in report_data
        }
        self._fill_missing_days_with_zero(financial_dict, ["total_income", "total_expense", "profit"], "general")
        days_sorted = sorted(financial_dict.keys())

        series_data = {
            'درآمد کل': [financial_dict[day]['total_income'] for day in days_sorted],
            'هزینه کل': [financial_dict[day]['total_expense'] for day in days_sorted],
            'ضرر/سود': [financial_dict[day]['profit'] for day in days_sorted],
        }
        self._create_bar_chart("نمودار میله‌ای نمایش درآمد، هزینه و سود", series_data, days_sorted, label_format="day_only")

    def general_multi_month_bar_chart(self, report_data):
        series_data = {
            'درآمد': [],
            'هزینه': [],
            'سود': []
        }
        for month, data in report_data.items():
            series_data['درآمد'].append(float(data["total_income"]) if data["total_income"] else 0.0)
            series_data['هزینه'].append(float(data["total_expense"]) if data["total_expense"] else 0.0)
            series_data['سود'].append(float(data["profit"]) if data["profit"] else 0.0)

        self._create_bar_chart("نمودار میله‌ای نمایش سالانه درآمد، هزینه و سود", series_data, list(report_data.keys()))

    def service_multi_month_bar_chart(self, report_data):
        series_data = {
            'درآمد سرویس': []
        }
        for month, data in report_data.items():
            series_data['درآمد سرویس'].append(float(data["total_income"]) if data["total_income"] else 0.0)

        self._create_bar_chart("نمودار میله‌ای نمایش سالانه درآمد سرویس", series_data, list(report_data.keys()))

    def service_single_month_bar_chart(self, report_data):
        income_dict = {data['jalali_date']: data['income'] for data in report_data}
        self._fill_missing_days_with_zero(income_dict, "income", "service")

        days_sorted = sorted(income_dict.keys())
        series_data = {
            'درآمد سرویس': [income_dict[day] for day in days_sorted]
        }
        self._create_bar_chart("نمودار میله‌ای نمایش درآمد سرویس", series_data, days_sorted, label_format="day_only")

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

    def _fill_missing_days_with_zero(self, data_dict, keys, report_type):
        selected_year = getattr(self.ui, f"{report_type}ReportYear_spnbox").value()
        selected_from_month = getattr(self.ui, f"{report_type}ReportFromMonth_spnbox").value()
        date = jdatetime.date(selected_year, selected_from_month, 1)
        year_month_str = date.strftime("%Y-%m")
        current_month_last_day_date = Dates.get_last_day_of_month_date(date)
        days_in_month = range(1, current_month_last_day_date.day + 1)

        for day in days_in_month:
            jalali_date = f"{year_month_str}-{day:02}"
            if jalali_date not in data_dict:
                data_dict[jalali_date] = {key: 0 for key in keys} if isinstance(keys, list) else 0

