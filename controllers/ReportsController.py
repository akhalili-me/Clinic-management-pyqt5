# from ui import Ui_MainWindow
from models import Services, Reports
from utility import (
    Dates,
    Numbers,
    ChartManager,
    Messages,
    BaseController,
)
import jdatetime

class ReportsTabController(BaseController):
    HIGH_SELL_LABEL_COUNT = 4

    def __init__(self, ui,dispatcher):
        self.ui = ui
        self.active_workers = []
        dispatcher.reload_report_services.connect(self.load_services)
        self.chart_manager = ChartManager(ui)
        self._connect_buttons()
        self.load_services()
        self._set_current_date_into_reports_intervals()
        self._no_general_report_found()
        self._no_service_report_found()

    def _set_current_date_into_reports_intervals(self):
        today_date = jdatetime.date.today()
        self.ui.generalReportYear_spnbox.setValue(today_date.year)
        self.ui.generalReportToMonth_spnbox.setValue(today_date.month)
        self.ui.generalReportFromMonth_spnbox.setValue(today_date.month)

        self.ui.serviceReportYear_spnbox.setValue(today_date.year)
        self.ui.serviceReportToMonth_spnbox.setValue(today_date.month)
        self.ui.serviceReportFromMonth_spnbox.setValue(today_date.month)

    def _connect_buttons(self):
        button_connections = {
            "generalReport_btn": self.switch_to_general_report,
            "serviceReport_btn": self.switch_to_service_report,
            "refreshServiceReport_btn": lambda: self.validate_form("service"),
            "refreshGeneralReport_btn": lambda: self.validate_form("general"),
        }
        for button_name, function in button_connections.items():
            getattr(self.ui, button_name).clicked.connect(function)

    def switch_to_report(self, index):
        self.ui.report_stackedWidget.setCurrentIndex(index)

    def switch_to_general_report(self):
        self.switch_to_report(0)

    def switch_to_service_report(self):
        self.switch_to_report(1)

    def load_services(self):
        self._start_worker(Services.get_all, [], self.display_services)

    def display_services(self, services):
        self.ui.reportService_cmbox.clear()
        for service in services:
            self.ui.reportService_cmbox.addItem(service["name"], service["id"])

    def validate_form(self,report_type):
        selected_from_month = getattr(self.ui, f"{report_type}ReportFromMonth_spnbox").value()
        selected_to_month = getattr(self.ui, f"{report_type}ReportToMonth_spnbox").value()

        if selected_from_month > selected_to_month:
            Messages.show_warning_msg("شروع ماه ‌نمی‌تواند از پایان ماه کمتر باشد.")
            return

        getattr(self,f"load_{report_type}_report")()

    def load_general_report(self):
        intervals = self._get_selected_date_interval("general")
        self._start_worker(Reports.get_general_report, intervals["date_intervals"], self.display_general_report_labels)

        worker_fn = Reports.get_multi_month_general_financial_summary if intervals["monthly_intervals"] else Reports.get_single_month_financial_summary_by_days
        args = [intervals["monthly_intervals"]] if intervals["monthly_intervals"] else intervals["date_intervals"]
        result_fn = self.display_multi_month_general_report_chart if intervals["monthly_intervals"] else self.display_single_month_general_bar_chart
        self._start_worker(worker_fn, args, result_fn)

    def display_multi_month_general_report_chart(self, report_data):
        self.chart_manager.general_multi_month_bar_chart(report_data)

    def display_single_month_general_bar_chart(self,report_data):
        self.chart_manager.general_single_month_bar_chart(report_data)

    def display_general_report_labels(self, data):
        financial_summary, service_expense_summary = data
        if (
            financial_summary["total_income"] == 0
            and financial_summary["total_expense"] == 0
        ):
            self._no_general_report_found()
            return

        highest_services, highest_expenses = self._separate_services_from_expenses(
            service_expense_summary
        )
        self._update_general_report_labels(
            financial_summary, highest_services, highest_expenses
        )

    def _separate_services_from_expenses(self, data):
        services = [item for item in data if item["type"] == "service"]
        expenses = [item for item in data if item["type"] != "service"]
        return services, expenses

    def _update_general_report_labels(
        self, general_report_data, highest_services, highest_expenses
    ):
        profit = general_report_data.get("profit", 0)
        profit_type = "ضرر" if profit < 0 else "سود"

        total_income = Numbers.int_to_persian_with_separators(
            general_report_data.get("total_income", 0)
        )
        total_expense = Numbers.int_to_persian_with_separators(
            general_report_data.get("total_expense", 0)
        )
        profit = Numbers.int_to_persian_with_separators(profit)

        self.ui.profitType_lbl.setText(profit_type)
        self.ui.generalIncome_lbl.setText(f"{total_income} تومان")
        self.ui.generalExpense_lbl.setText(f"{total_expense} تومان")
        self.ui.generalProfit_lbl.setText(f"{profit} تومان")

        self._clear_highest_labels("ServiceHighSold")
        self._clear_highest_labels("HighestExpense")
        self._set_highest_labels("ServiceHighSold", highest_services, "name")
        self._set_highest_labels("HighestExpense", highest_expenses, "name")

    def load_service_report(self):
        intervals = self._get_selected_date_interval("service")
        service_id = self.ui.reportService_cmbox.currentData()
        self._start_worker(Reports.get_service_report, [service_id, *intervals["date_intervals"]], self.display_service_report_labels)

        worker_fn = Reports.get_multi_month_service_financial_summary if intervals["monthly_intervals"] else Reports.get_single_month_service_financial_summary
        args = [service_id, intervals["monthly_intervals"]] if intervals["monthly_intervals"] else [service_id, *intervals["date_intervals"]]
        result_fn = self.display_multi_month_service_report_chart if intervals["monthly_intervals"] else self.display_single_month_service_report_chart
        self._start_worker(worker_fn, args, result_fn)

    def display_multi_month_service_report_chart(self,report_data):
        self.chart_manager.service_multi_month_bar_chart(report_data)

    def display_single_month_service_report_chart(self,report_data):
        self.chart_manager.service_single_month_bar_chart(report_data)

    def display_service_report_labels(self, data):
        service_financials, high_sold_service_days = data

        if service_financials["services_count"] == 0:
            self._no_service_report_found()
            return

        self._update_service_report_labels(service_financials, high_sold_service_days)

    def _update_service_report_labels(self, report_data, high_sold_service_data):
        total_income = Numbers.int_to_persian_with_separators(
            report_data["total_income"]
        )
        self.ui.serviceIncome_lbl.setText(f"{total_income} تومان")
        self.ui.serviceCount_lbl.setText(
            Numbers.english_to_persian_numbers(report_data["services_count"])
        )

        self._clear_highest_labels("DayServiceHighSell")
        for i, data in enumerate(high_sold_service_data[: self.HIGH_SELL_LABEL_COUNT]):
            sold_count = Numbers.english_to_persian_numbers(data["sold_count"])
            jalali_date = Dates.convert_to_jalali_format(data["jalali_date"])
            label = getattr(self.ui, f"n{i}DayServiceHighSell_lbl")
            label.setText(f"{sold_count} سرویس در روز {jalali_date}")

    def _get_selected_date_interval(self, report_type):
        result = {}
        selected_year = getattr(self.ui, f"{report_type}ReportYear_spnbox").value()
        selected_from_month = getattr(self.ui, f"{report_type}ReportFromMonth_spnbox").value()
        selected_to_month = getattr(self.ui, f"{report_type}ReportToMonth_spnbox").value()
        start_date, end_date = Dates.get_date_interval(selected_year, selected_from_month, selected_to_month)
        result["date_intervals"] = start_date, end_date
        result["monthly_intervals"] = None
        if selected_from_month != selected_to_month:
            result["monthly_intervals"] = Dates.get_multi_month_intervals(selected_year, selected_from_month, selected_to_month)
        return result

    def _no_service_report_found(self):
        self.ui.serviceCount_lbl.setText("بدون اطلاعات")
        self.ui.serviceIncome_lbl.setText("بدون اطلاعات")
        self._clear_highest_labels("DayServiceHighSell")
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
        self._clear_highest_labels("ServiceHighSold")
        self._clear_highest_labels("HighestExpense")
        self.chart_manager.clear_chart_view()
