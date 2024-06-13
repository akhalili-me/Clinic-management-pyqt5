# controllers/add_patient_controller.py
from PyQt5.QtWidgets import QDialog
from ui import Ui_MainWindow,Ui_addEditDeleteExpense_form
from models.db import DatabaseManager
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSignal
from models import Expenses
from PyQt5.QtWidgets import QListWidgetItem
from utility import Dates,Numbers,LoadingValues,Validators,Messages
import jdatetime

class ExpenseTabController:
    def __init__(self, ui:Ui_MainWindow):
        self.ui = ui
        self.load_current_month_expense_list()
        self.load_current_date_into_date_spnboxes()
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.searchExpenseByName_btn.clicked.connect(self.search_by_name)
        self.ui.searchExpenseByDate_btn.clicked.connect(self.search_by_date)
        self.ui.addExpense_btn.clicked.connect(self.open_add_expense)
        self.ui.expense_lst.itemDoubleClicked.connect(self.open_edit_delete_expense)

    def open_add_expense(self):
        self.add_expense_controller = AddEditDeleteExpenses()
        self.add_expense_controller.refresh_expense_list.connect(self.load_current_month_expense_list)
        self.add_expense_controller.show()

    def open_edit_delete_expense(self,item):
        expense_id = item.data(1)
        with DatabaseManager() as db:
            expense = Expenses.get_by_id(db,expense_id)
        self.edit_delete_expense_controller = AddEditDeleteExpenses(expense)
        self.edit_delete_expense_controller.refresh_expense_list.connect(self.load_current_month_expense_list)
        self.edit_delete_expense_controller.show()

    def search_by_name(self):
        name = self.ui.expenseName_txtbox.text()
        with DatabaseManager() as db:
            searched_expenses = Expenses.search_by_name(db,name)
        self._load_expense_data_expense_list(searched_expenses)
    
    def search_by_date(self):
        # to do
        from_date = ""
        to_date = ""
        with DatabaseManager() as db:
            searched_expenses = Expenses.get_by_date(db,from_date,to_date)
        self._load_expense_data_expense_list(searched_expenses)

    def load_current_month_expense_list(self):
        current_month_expenses = self._fetch_current_month_expenses()
        self._load_expense_data_expense_list(current_month_expenses)
        
    def _load_expense_data_expense_list(self,expenses):
        self.ui.expense_lst.clear()
        
        for expense in expenses:
            description = expense["description"] or "بدون توضیحات"
            price = Numbers.int_to_persian_with_separators(expense["price"])
            jalali_date = Dates.convert_to_jalali_format(expense["jalali_date"])
            item_txt = f"{expense["name"]} | {price} تومان | {jalali_date} | {description}"
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
            LoadingValues.load_current_date_spin_box_values(self.ui,date_spnbox)

    def _fetch_current_month_expenses(self):
        first_day_month,last_day_month = Dates.get_jalali_current_month_interval_based_on_greg()
        with DatabaseManager() as db:
            return Expenses.get_by_date(db, first_day_month, last_day_month)

class AddEditDeleteExpenses(QDialog):
    refresh_expense_list = pyqtSignal()

    def __init__(self, expense=None):
        super(AddEditDeleteExpenses, self).__init__()
        self.ui = Ui_addEditDeleteExpense_form()
        self.ui.setupUi(self)
        self.setModal(True)

        #Check if it's a edit window
        self.expense = expense
        if expense:
            self.load_expense_data_into_txtboxes()
            self.ui.title_lbl.setText("ویرایش هزینه")
        else:
            self.ui.delete_btn.hide()

        LoadingValues.load_current_date_spin_box_values(self.ui)
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.save_btn.clicked.connect(self.validate_form)
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.delete_btn.clicked.connect(self.delete_expense)

    def validate_form(self):
        name_text = self.ui.name_txtbox.text()
        txtboxes = [
            {"text": name_text, "name": "نام هزینه"},
        ]

        if Validators.validate_empty_txt_boxes(txtboxes):
            self.save_expense()

    def load_expense_data_into_txtboxes(self):
        self.ui.name_txtbox.setText(self.expense["name"])
        self.ui.price_txtbox.setValue(self.expense["price"])
        LoadingValues.load_date_into_date_spinbox(self.ui,self.expense["jalali_date"])
        self.ui.description_txtbox.setPlainText(self.expense["description"])

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

        with DatabaseManager() as db:
            if self.expense:
                expense_data['id'] = self.expense["id"]
                Expenses.update_expense(db, expense_data)
                success_message = "هزینه با موفقیت ویرایش شد."
            else:
                Expenses.add_expense(db, expense_data)
                success_message = "هزینه با موفقیت اضافه شد."

            QMessageBox.information(self, "موفقیت", success_message)
            self.refresh_expense_list.emit()
            self.close()


    def delete_expense(self):
        msg_box, yes_button = Messages.show_confirm_delete_msg()
        if msg_box.clickedButton() == yes_button:
            with DatabaseManager() as db:
                Expenses.delete_expense(db,self.expense["id"])
                Messages.show_success_msg("هزینه با موفقیت حذف شد.")
                self.close()
                self.refresh_expense_list.emit()
        else:
            msg_box.close()

    def _get_jalali_date(self):
        year = self.ui.year_spnbox.value()
        month = self.ui.month_spnbox.value()
        day = self.ui.day_spnbox.value()
        return jdatetime.date(year, month, day).strftime("%Y-%m-%d")

    def _get_gregorian_date(self, jalali_date_str):
        year, month, day = map(int, jalali_date_str.split("-"))
        return (
            jdatetime.datetime(year, month, day)
            .togregorian()
            .strftime("%Y-%m-%d %H:%M")
        )
