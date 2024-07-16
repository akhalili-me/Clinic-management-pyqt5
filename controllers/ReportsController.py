from ui import Ui_MainWindow
from models import DatabaseManager,Services,Reports
from utility import Dates,Numbers,TimeIntervals,ChartManager
import jdatetime

class ReportsTabController:
    HIGH_SELL_LABEL_COUNT = 4

    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        self.chart_manager = ChartManager(ui)
        self._connect_buttons()
        self._load_services()
        self._no_general_report_found()
        self._no_service_report_found()

    def _connect_buttons(self):
        button_connections = {
            'generalReport_btn': self.switch_to_general_report,
            'serviceReport_btn': self.switch_to_service_report,
            'refreshServiceReport_btn': self.refresh_service_report,
            'refreshGeneralReport_btn': self.refresh_general_report
        }
        for button_name, function in button_connections.items():
            getattr(self.ui, button_name).clicked.connect(function)

    def switch_to_report(self, index):
        self.ui.report_stackedWidget.setCurrentIndex(index)

    def switch_to_general_report(self):
        self.switch_to_report(0)

    def switch_to_service_report(self):
        self.switch_to_report(1)

    def _load_services(self):
        with DatabaseManager() as db:
            services = Services.get_all(db)
            self.ui.reportService_cmbox.clear()
            for service in services:
                self.ui.reportService_cmbox.addItem(service["name"], service["id"])

    def refresh_general_report(self):
        start_date, end_date = self._get_selected_date_interval(self.ui.generalTime_cmbox.currentText())
        general_report_data, service_usage_expense_data = self._fetch_general_report_data(start_date, end_date)
        
        if general_report_data["total_income"] == 0 and general_report_data["total_expense"] == 0:
            self._no_general_report_found()
            return
        
        highest_services, highest_expenses = self._separate_services_from_expenses(service_usage_expense_data)
        self._update_general_report_labels(general_report_data, highest_services, highest_expenses)
        self._update_general_report_chart(self.ui.generalTime_cmbox.currentText())

    def _fetch_general_report_data(self, start_date, end_date):
        with DatabaseManager() as db:
            general_report_data = Reports.get_financial_summary(db, start_date, end_date)
            service_usage_expense_data = Reports.get_service_usage_and_expenses_summary(db, start_date, end_date)
        return general_report_data, service_usage_expense_data

    def _separate_services_from_expenses(self, data):
        services = [item for item in data if item["type"] == 'service']
        expenses = [item for item in data if item["type"] != 'service']
        return services, expenses

    def _update_general_report_labels(self, general_report_data, highest_services, highest_expenses):
        profit = general_report_data.get("profit", 0)
        profit_type = "ضرر" if profit < 0 else "سود"
        
        total_income = Numbers.int_to_persian_with_separators(general_report_data.get("total_income", 0))
        total_expense = Numbers.int_to_persian_with_separators(general_report_data.get("total_expense", 0))
        profit = Numbers.int_to_persian_with_separators(profit)

        self.ui.profitType_lbl.setText(profit_type)
        self.ui.generalIncome_lbl.setText(f"{total_income} تومان")
        self.ui.generalExpense_lbl.setText(f"{total_expense} تومان")
        self.ui.generalProfit_lbl.setText(f"{profit} تومان")

        self._clear_highest_labels('ServiceHighSold')
        self._clear_highest_labels('HighestExpense')
        self._set_highest_labels('ServiceHighSold', highest_services, 'name')
        self._set_highest_labels('HighestExpense', highest_expenses, 'name')

    def _update_general_report_chart(self, selected_time):
        current_year = jdatetime.date.today().year
        if selected_time == TimeIntervals.CURRENT_MONTH.value:
            self.chart_manager.general_current_month_bar_chart()
        elif selected_time in [TimeIntervals.CURRENT_YEAR.value, TimeIntervals.LAST_YEAR.value]:
            year = current_year if selected_time == TimeIntervals.CURRENT_YEAR.value else current_year - 1
            self.chart_manager.general_year_bar_chart(year)

    def refresh_service_report(self):
        service_id = self.ui.reportService_cmbox.currentData()
        start_date, end_date = self._get_selected_date_interval(self.ui.serviceReportTime_cmbox.currentText())
        service_report_data, high_sold_service_data = self._fetch_service_report_data(service_id, start_date, end_date)

        if service_report_data["services_count"] == 0:
            self._no_service_report_found()
            return

        self._update_service_report_labels(service_report_data, high_sold_service_data)
        self._update_service_chart(service_id, self.ui.serviceReportTime_cmbox.currentText())

    def _fetch_service_report_data(self, service_id, start_date, end_date):
        with DatabaseManager() as db:
            service_report_data = Reports.get_service_count_income(db, service_id, start_date, end_date)
            high_sold_service_data = Reports.get_most_sold_service_dates(db, service_id, start_date, end_date)
        return service_report_data, high_sold_service_data

    def _update_service_chart(self, service_id, selected_time):
        current_year = jdatetime.date.today().year
        if selected_time == TimeIntervals.CURRENT_MONTH.value:
            self.chart_manager.service_current_month_bar_chart(service_id)
        elif selected_time in [TimeIntervals.CURRENT_YEAR.value, TimeIntervals.LAST_YEAR.value]:
            year = current_year if selected_time == TimeIntervals.CURRENT_YEAR.value else current_year - 1
            self.chart_manager.service_year_bar_chart(service_id, year)

    def _update_service_report_labels(self, report_data, high_sold_service_data):
        total_income = Numbers.int_to_persian_with_separators(report_data["total_income"])
        self.ui.serviceIncome_lbl.setText(f"{total_income} تومان")
        self.ui.serviceCount_lbl.setText(Numbers.english_to_persian_numbers(report_data["services_count"]))

        self._clear_highest_labels('DayServiceHighSell')
        for i, data in enumerate(high_sold_service_data[:self.HIGH_SELL_LABEL_COUNT]):
            sold_count = Numbers.english_to_persian_numbers(data["sold_count"])
            jalali_date = Dates.convert_to_jalali_format(data["jalali_date"])
            label = getattr(self.ui, f"n{i}DayServiceHighSell_lbl")
            label.setText(f"{sold_count} سرویس در روز {jalali_date}")

    def _get_selected_date_interval(self, selected_time):
        current_year = jdatetime.date.today().year
        time_interval_functions = {
            TimeIntervals.CURRENT_MONTH.value: Dates.get_jalali_current_month_interval_based_on_greg,
            TimeIntervals.CURRENT_YEAR.value: lambda: Dates.get_year_interval(current_year),
            TimeIntervals.LAST_YEAR.value: lambda: Dates.get_year_interval(current_year - 1)
        }
        return time_interval_functions[selected_time]()

    def _no_service_report_found(self):
        self.ui.serviceCount_lbl.setText("بدون اطلاعات")
        self.ui.serviceIncome_lbl.setText("بدون اطلاعات")
        self._clear_highest_labels('DayServiceHighSell')
        self.chart_manager.clear_chart_view()

    def _clear_highest_labels(self, label_type):
        for i in range(4):
            label = getattr(self.ui, f"n{i}{label_type}_lbl", None)
            label.setText("-")

    def _set_highest_labels(self, label_prefix, items, item_key):
        for i, item in enumerate(items):
            label = getattr(self.ui, f"n{i}{label_prefix}_lbl")
            label.setText(item[item_key])

    def _no_general_report_found(self):
        self.ui.generalIncome_lbl.setText("بدون اطلاعات")
        self.ui.generalExpense_lbl.setText("بدون اطلاعات")
        self.ui.generalProfit_lbl.setText("بدون اطلاعات")
        self._clear_highest_labels('ServiceHighSold')
        self._clear_highest_labels('HighestExpense')
        self.chart_manager.clear_chart_view()