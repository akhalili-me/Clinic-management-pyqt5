from ui import Ui_MainWindow
from models import DatabaseManager,Services,Reports
from utility import Dates,Numbers,TimeIntervals,ChartManager

class ReportsTabController:
    HIGH_SELL_LABEL_COUNT = 4

    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        self.chart_manager = ChartManager(ui)
        self._connect_buttons()
        self._load_services()

    def _connect_buttons(self):
        buttons = {
            'generalReport_btn': self.switch_to_general_report,
            'serviceReport_btn': self.switch_to_service_report,
            'refreshServiceReport_btn': self.refresh_service_report
        }
        for button, function in buttons.items():
            getattr(self.ui, button).clicked.connect(function)

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

    def refresh_service_report(self):
        service_id = self.ui.reportService_cmbox.currentData()
        start_date, end_date = self._get_selected_date_interval()

        with DatabaseManager() as db:
            report_data = Reports.get_service_count_income(db, service_id, start_date, end_date)
            high_sold_service_data = Reports.get_most_sold_service_dates(db, service_id, start_date, end_date)
        
        if report_data["services_count"] == 0:
            self._no_report_found()
            return

        self._update_report_labels(report_data, high_sold_service_data)
        self._update_chart()

    def _update_chart(self):
        selected_time = self.ui.serviceReportTime_cmbox.currentText()
        service_id = self.ui.reportService_cmbox.currentData()

        if selected_time == TimeIntervals.CURRENT_MONTH.value:
            self.chart_manager.current_month_bar_chart(service_id)

    def _update_report_labels(self, report_data, high_sold_service_data):
        total_income = Numbers.int_to_persian_with_separators(report_data["total_income"])
        self.ui.serviceIncome_lbl.setText(f"{total_income} تومان")
        self.ui.serviceCount_lbl.setText(Numbers.english_to_persian_numbers(report_data["services_count"]))

        self._clear_service_high_sell_labels()
        for i, data in enumerate(high_sold_service_data[:self.HIGH_SELL_LABEL_COUNT]):
            sold_count = Numbers.english_to_persian_numbers(data["sold_count"])
            jalali_date = Dates.convert_to_jalali_format(data["jalali_date"])
            label = getattr(self.ui, f"n{i}DayServiceHighSell_lbl")
            label.setText(f"{sold_count} سرویس در روز {jalali_date}")

    def _clear_service_high_sell_labels(self):
        for i in range(self.HIGH_SELL_LABEL_COUNT):
            label = getattr(self.ui, f"n{i}DayServiceHighSell_lbl")
            label.setText("-")

    def _get_selected_date_interval(self):
        selected_time = self.ui.serviceReportTime_cmbox.currentText()
        time_intervals = {
            TimeIntervals.LAST_SIX_MONTHS.value: Dates.get_jalali_last_six_month_interval_based_on_greg,
            TimeIntervals.LAST_THREE_MONTHS.value: Dates.get_jalali_last_three_month_interval_based_on_greg,
            TimeIntervals.CURRENT_MONTH.value: Dates.get_jalali_current_month_interval_based_on_greg,
            TimeIntervals.LAST_YEAR.value: Dates.get_jalali_last_year_interval_based_on_greg,
            TimeIntervals.CURRENT_YEAR.value: Dates.get_jalali_current_year_interval_based_on_greg
        }
        return time_intervals[selected_time]()

    def _no_report_found(self):
        self.ui.serviceCount_lbl.setText("بدون اطلاعات")
        self.ui.serviceIncome_lbl.setText("بدون اطلاعات")
        self._clear_service_high_sell_labels()
        self.chart_manager.clear_chart_view()
