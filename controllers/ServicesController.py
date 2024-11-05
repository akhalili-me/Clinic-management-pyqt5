# controllers/add_patient_controller.py
from PyQt5.QtWidgets import QDialog
from ui import get_ui_class
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSignal
from models import Services
from PyQt5.QtWidgets import QListWidgetItem
from utility import Numbers, Messages, BaseController
from models import DatabaseWorker

class ServicesTabController(BaseController):
    def __init__(self, ui, dispatcher):
        self.ui = ui
        self.active_workers = []
        self.dispatcher = dispatcher
        self.load_services_list()
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.addServices_btn.clicked.connect(self.open_add_service)
        self.ui.services_lst.itemDoubleClicked.connect(self.open_edit_delete_service)
        self.ui.searchServices_btn.clicked.connect(self.search_services)
        self.ui.refreshServiceList_btn.clicked.connect(self.refresh_service_list)

    def refresh_service_list(self):
        self.ui.serviceName_txtbox.setText("")
        self.load_services_list()

    def search_services(self):
        searched_name = self.ui.serviceName_txtbox.text().strip()
        self._start_worker(
            Services.search_service_by_name, [searched_name], self.display_services_data
        )

    def open_edit_delete_service(self, item):
        service_id = item.data(1)
        self.open_delete_edit_service_controller = AddEditDeleteServiceController(
            service_id, self.dispatcher
        )
        self.open_delete_edit_service_controller.refresh_services_list.connect(
            self.load_services_list
        )
        self.open_delete_edit_service_controller.show()

    def open_add_service(self):
        self.add_service_controller = AddEditDeleteServiceController(
            dispatcher=self.dispatcher
        )
        self.add_service_controller.refresh_services_list.connect(
            self.load_services_list
        )
        self.add_service_controller.show()

    def load_services_list(self):
        self._start_worker(Services.get_all, result_callback=self.display_services_data)

    def display_services_data(self, all_services):
        self.ui.services_lst.clear()
        for service in all_services:
            persian_price = Numbers.int_to_persian_with_separators(service["price"])
            item_txt = f"{service['name']} | قیمت: {persian_price} تومان"
            item = QListWidgetItem(item_txt)
            item.setData(1, service["id"])
            self.ui.services_lst.addItem(item)


class AddEditDeleteServiceController(BaseController, QDialog):
    refresh_services_list = pyqtSignal()

    def __init__(self, service_id=None, dispatcher=None):
        super(AddEditDeleteServiceController, self).__init__()
        self.ui = get_ui_class("aedService")()
        self.ui.setupUi(self)
        self._setup_validators()
        self.active_workers = []
        self.dispatcher = dispatcher
        self.setModal(True)
        self.service_id = service_id
        if service_id:
            self.load_service_data()
        else:
            self.ui.deleteService_btn.hide()
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.save_btn.clicked.connect(self.save_service)
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.deleteService_btn.clicked.connect(self.delete_service)

    def _setup_validators(self):
        self.ui.serviceName_txtbox.setMaxLength(50)

    def load_service_data(self):
        self._start_worker(Services.get_by_id,[self.service_id],self.display_service_data)

    def display_service_data(self,service):
        self.ui.serviceName_txtbox.setText(service["name"])
        self.ui.servicePrice_spnbox.setValue(service["price"])

    def save_service(self):
        service_data = {
            "name": self.ui.serviceName_txtbox.text(),
            "price": self.ui.servicePrice_spnbox.value(),
        }

        if self.service_id:
            service_data["id"] = self.service_id
            self.update_service(service_data)
        else:
            self.add_service(service_data)

    def add_service(self, service):
        self._start_worker(
            Services.add_service,
            [service],
            success_callback=lambda: self.operation_successful(
                "سرویس با موفقیت اضافه شد."
            ),
        )

    def update_service(self, service):
        self._start_worker(
            Services.update_service,
            [service],
            success_callback=lambda: self.operation_successful(
                "سرویس با موفقیت ویرایش شد.", True
            ),
        )

    def operation_successful(self, success_msg, update_delete=False):
        QMessageBox.information(self, "موفقیت", success_msg)
        if update_delete:
            self.dispatcher.refresh_appointments_list.emit()
        self.dispatcher.reload_report_services.emit()
        self.refresh_services_list.emit()
        self.close()

    def delete_service(self):
        msg_box, yes_button = Messages.show_confirm_delete_msg()
        if msg_box.clickedButton() == yes_button:
            self._start_worker(
                Services.delete_service,
                [self.service["id"]],
                success_callback=lambda: self.operation_successful(
                    "سرویس با موفقیت حذف شد.", True
                ),
            )
        else:
            msg_box.close()
