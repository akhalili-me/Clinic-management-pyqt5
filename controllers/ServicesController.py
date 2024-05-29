# controllers/add_patient_controller.py
from PyQt5.QtWidgets import QDialog
from ui.add_service import Ui_addService_form
from models.db import DatabaseManager
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSignal
from models.Services import Services
from models.Services import Services
from PyQt5.QtWidgets import QListWidgetItem
from utility import Numbers

class ServicesTabController:
    def __init__(self, ui):
        self.ui = ui
        self.load_services_list()
        self.ui.addServices_btn.clicked.connect(self.open_add_service)

    def open_add_service(self):
        from controllers.ServicesController import AddServiceController
        self.add_service_controller = AddServiceController()
        self.add_service_controller.refresh_services_list.connect(self.load_services_list)
        self.add_service_controller.show()

    def load_services_list(self):
        self.ui.services_lst.clear()
        with DatabaseManager() as db:
            all_services = Services.get_all(db)
            for service in all_services:
                persian_price = Numbers.int_to_persian_with_separators(service["price"])
                item_txt = f"{service['name']} | قیمت: {persian_price} تومان"
                item = QListWidgetItem(item_txt)
                item.setData(1, service['id'])
                self.ui.services_lst.addItem(item)


class AddServiceController(QDialog):
    refresh_services_list = pyqtSignal()

    def __init__(self):
        super(AddServiceController, self).__init__()
        self.ui = Ui_addService_form()
        self.ui.setupUi(self)

        self.setModal(True)

        # Connecting the buttons 
        self.ui.save_btn.clicked.connect(self.save_patient)
        self.ui.cancel_btn.clicked.connect(self.close)

    def save_patient(self):
        service = {
            'name': self.ui.serviceName_txtbox.text(),
            'price': self.ui.servicePrice_spnbox.value(),
        }

        with DatabaseManager() as db:
            Services.add_service(db,service)
            QMessageBox.information(self, "موفقیت", "سرویس با موفقیت اضافه شد.")
            self.refresh_services_list.emit()
            self.close()
