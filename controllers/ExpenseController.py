# controllers/add_patient_controller.py
from PyQt5.QtWidgets import QDialog
# from ui import Ui_MainWindow,Ui_addEditDeleteExpense_form
from ui import get_ui_class
from PyQt5.QtCore import pyqtSignal
from models import Expenses
from PyQt5.QtWidgets import QListWidgetItem
from utility import Dates,Numbers,Validators,Messages,BaseController,LoadSpinBox
import jdatetime

class ExpenseTabController(BaseController):
    def __init__(self, ui):
        self.ui = ui
        self.active_workers = []
        self.load_current_month_expense_list()
        self.load_current_date_into_date_spnboxes()
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.searchExpenseByName_btn.clicked.connect(self.search_by_name)
        self.ui.searchExpenseByDate_btn.clicked.connect(self.search_by_date)
        self.ui.addExpense_btn.clicked.connect(self.open_add_expense)
        self.ui.expense_lst.itemDoubleClicked.connect(self.open_edit_delete_expense)
        self.ui.refreshExpenseList_btn.clicked.connect(self.handle_expense_refresh)

    def handle_expense_refresh(self):
        self.ui.expenseName_txtbox.setText("")
        self.load_current_month_expense_list()
        self.load_current_date_into_date_spnboxes()

    def open_add_expense(self):
        self.add_expense_controller = AddEditDeleteExpenses()
        self.add_expense_controller.refresh_expense_list.connect(self.load_current_month_expense_list)
        self.add_expense_controller.show()

    def open_edit_delete_expense(self,item):
        expense_id = item.data(1)
        self.edit_delete_expense_controller = AddEditDeleteExpenses(expense_id)
        self.edit_delete_expense_controller.refresh_expense_list.connect(self.load_current_month_expense_list)
        self.edit_delete_expense_controller.show()

    def search_by_name(self):
        name = self.ui.expenseName_txtbox.text()
        self._start_worker(Expenses.search_by_name, [name], self.display_expense_list)

    def search_by_date(self):
        from_year, from_month, from_day = self.ui.fromYear_spnbox.value(), self.ui.fromMonth_spnbox.value(), self.ui.fromDay_spnbox.value()
        to_year, to_month, to_day = self.ui.toYear_spnbox.value(), self.ui.toMonth_spnbox.value(), self.ui.toDay_spnbox.value()

        from_date = jdatetime.date(from_year,from_month,from_day).togregorian().strftime("%Y-%m-%d")
        to_date = jdatetime.date(to_year,to_month,to_day).togregorian().strftime("%Y-%m-%d")

        self._start_worker(
            Expenses.get_by_date, [from_date, to_date], self.display_expense_list
        )

    def load_current_month_expense_list(self):
        first_day_month,last_day_month = Dates.get_jalali_current_month_interval_based_on_greg()
        self._start_worker(
            Expenses.get_by_date,
            [first_day_month, last_day_month],
            self.display_expense_list,
        )

    def display_expense_list(self,expenses):
        self.ui.expense_lst.clear()
        for expense in expenses:
            price = Numbers.int_to_persian_with_separators(expense["price"])
            jalali_date = Dates.convert_to_jalali_format(expense["jalali_date"])
            item_txt = f"{expense["name"]} | {price} تومان | {jalali_date}"
            item = QListWidgetItem(item_txt)
            item.setData(1, expense['id'])
            self.ui.expense_lst.addItem(item)

    def load_current_date_into_date_spnboxes(self):
        date_spnbox_list = [
            {
                "year": "toYear_spnbox",
                "month": "toMonth_spnbox",
                "day": "toDay_spnbox",
            },
            {
                "year": "fromYear_spnbox",
                "month": "fromMonth_spnbox",
                "day": "fromDay_spnbox",
            },
        ]

        for date_spnbox in date_spnbox_list:
            LoadSpinBox.set_current_date_into_date_spin_boxes(self.ui,date_spnbox)

class AddEditDeleteExpenses(BaseController,QDialog):
    refresh_expense_list = pyqtSignal()

    def __init__(self, expense_id=None):
        super(AddEditDeleteExpenses, self).__init__()
        self.ui = get_ui_class("aedExpense")()
        self.ui.setupUi(self)
        self.setModal(True)
        self._setup_validators()
        self.active_workers = []
        self.expense_id= expense_id
        if expense_id:
            self.load_expense_data_into_txtboxes()
        else:
            self.ui.delete_btn.hide()

        LoadSpinBox.set_current_date_into_date_spin_boxes(self.ui)
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.save_btn.clicked.connect(self.validate_form)
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.delete_btn.clicked.connect(self.open_delete_expense)

    def _setup_validators(self):
        self.ui.name_txtbox.setMaxLength(50)
        self.ui.description_txtbox.textChanged.connect(
            lambda: Validators.limit_text_edit(self.ui.description_txtbox)
        )
    def validate_form(self):
        try:
            self._get_jalali_date()
        except Exception as e:
            warning_message = f"""
            تاریخ انتخاب شده وجود ندارد. 
            {str(e)}
            """
            Messages.show_warning_msg(warning_message)
            return

        name_text = self.ui.name_txtbox.text()
        txtboxes = [
            {"text": name_text, "name": "نام هزینه"},
        ]

        if Validators.validate_empty_txt_boxes(txtboxes):
            self.save_expense()

        

    def load_expense_data_into_txtboxes(self):
        self._start_worker(
            Expenses.get_by_id, [self.expense_id], self.display_expense_data
        )

    def display_expense_data(self,expense):
        self.ui.name_txtbox.setText(expense["name"])
        self.ui.price_txtbox.setValue(expense["price"])
        LoadSpinBox.load_date_into_date_spinboxes(self.ui,expense["jalali_date"])
        self.ui.description_txtbox.setPlainText(expense["description"])

    def save_expense(self):
        jalali_date_str = self._get_jalali_date().strip()
        greg_date = self._get_gregorian_date(jalali_date_str).strip()

        expense_data = {
            'name': self.ui.name_txtbox.text().strip(),
            'price': self.ui.price_txtbox.value(),
            'description': self.ui.description_txtbox.toPlainText().strip(),
            'jalali_date': jalali_date_str,
            'greg_date': greg_date
        }

        if self.expense_id:
            expense_data['id'] = self.expense_id
            self.update_expense(expense_data)
        else:
            self.add_expense(expense_data)

    def add_expense(self,expense):
        self._start_worker(
            Expenses.add_expense,
            [expense],
            success_callback=lambda: self.operation_successful(
                "هزینه با موفقیت اضافه شد."
            ),
        )

    def update_expense(self,expense):
        self._start_worker(
            Expenses.update_expense,
            [expense],
            success_callback=lambda: self.operation_successful(
                "هزینه با موفقیت ویرایش شد."
            ),
        )

    def open_delete_expense(self):
        msg_box, yes_button = Messages.show_confirm_delete_msg()
        if msg_box.clickedButton() != yes_button:
            msg_box.close()
            return

        self._start_worker(
            Expenses.delete_expense,
            [self.expense_id],
            success_callback=lambda: self.operation_successful(
                "هزینه با موفقیت حذف شد."
            ),
        )

    def operation_successful(self,success_msg):
        Messages.show_success_msg(success_msg)
        self.refresh_expense_list.emit()
        self.close()

    def _get_jalali_date(self):
        year = self.ui.year_spnbox.value()
        month = self.ui.month_spnbox.value()
        day = self.ui.day_spnbox.value()
        return jdatetime.date(year, month, day).strftime("%Y-%m-%d")

    def _get_gregorian_date(self, jalali_date_str):
        year, month, day = map(int, jalali_date_str.split("-"))
        return (
            jdatetime.date(year, month, day)
            .togregorian()
            .strftime("%Y-%m-%d")
        )
