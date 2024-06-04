# controllers/add_patient_controller.py
from PyQt5.QtWidgets import QDialog
from ui import Ui_addEditDeleteDoctor_form,Ui_MainWindow,Ui_addEditDeleteExpense_form
from models.db import DatabaseManager
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSignal
from models import Expenses
from PyQt5.QtWidgets import QListWidgetItem
from utility import Dates,Numbers,LoadingValues

class ExpenseTabController:
    def __init__(self, ui:Ui_MainWindow):
        self.ui = ui
        self.load_current_month_expense_list()
        self.load_current_date_into_date_spnboxes()
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.searchExpenseByName_btn.clicked.connect(self.search_by_name)
        self.ui.searchExpenseByDate_btn.clicked.connect(self.search_by_date)

    def search_by_name(self):
        name = self.ui.expenseName_txtbox.text()
        with DatabaseManager() as db:
            searched_expenses = Expenses.search_by_name(db,name)
        self._load_expense_data_expense_list(searched_expenses)
    
    def search_by_date(self):
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
            price = Numbers.int_to_persian_with_separators(expense["price"])
            jalali_date = Dates.convert_to_jalali_format(expense["jalali_date"])
            item_txt = f"{expense["name"]} | {price} تومان | {expense} | {jalali_date}"
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
    refresh_doctors_list = pyqtSignal()

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

        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.save_btn.clicked.connect(self.save_expense)
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.delete_btn.clicked.connect(self.delete_expense)

    def validate_form(self):
        pass

    def load_expense_data_into_txtboxes(self):
        self.ui.firstName_txtbox.setText(self.doctor["firstName"])
        self.ui.lastName_txtbox.setText(self.doctor["lastName"])
        self.ui.specialization_txtbox.setText(self.doctor["specialization"])

    def save_expense(self):
        doctor_data = {
            'firstName': self.ui.firstName_txtbox.text().strip(),
            'lastName': self.ui.lastName_txtbox.text().strip(),
            "specialization": self.ui.specialization_txtbox.text().strip(),
        }

        with DatabaseManager() as db:
            if self.doctor:
                doctor_data['id'] = self.doctor["id"]
                Doctors.update_doctor(db, doctor_data)
                success_message = "پزشک با موفقیت ویرایش شد."
            else:
                Doctors.add_doctor(db, doctor_data)
                success_message = "پزشک با موفقیت اضافه شد."

            QMessageBox.information(self, "موفقیت", success_message)
            self.refresh_doctors_list.emit()
            self.close()


    def delete_expense(self):
        msg_box, yes_button = Messages.show_confirm_delete_msg()
        if msg_box.clickedButton() == yes_button:
            with DatabaseManager() as db:
                Doctors.delete_doctor(db,self.doctor["id"])
                Messages.show_success_msg("پزشک با موفقیت حذف شد.")
                self.close()
                self.refresh_doctors_list.emit()
        else:
            msg_box.close()