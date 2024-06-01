# controllers/add_patient_controller.py
from PyQt5.QtWidgets import QDialog
from ui import Ui_addEditDeleteService_form,Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSignal
from models import Services,DatabaseManager
from PyQt5.QtWidgets import QListWidgetItem
from utility import Numbers,Messages

class ServicesTabController:
    def __init__(self, ui:Ui_MainWindow):
        self.ui = ui
        self.load_services_list()
        self._connect_buttons()


    def _connect_buttons(self):
        self.ui.addServices_btn.clicked.connect(self.open_add_service)
        self.ui.services_lst.itemDoubleClicked.connect(self.open_edit_delete_service)
        

    def open_edit_delete_service(self, item):
        service_id = item.data(1)
        with DatabaseManager() as db:
            service = Services.get_by_id(db,service_id)
        self.open_delete_edit_service_controller = AddEditDeleteServiceController(service)
        self.open_delete_edit_service_controller.refresh_services_list.connect(self.load_services_list)
        self.open_delete_edit_service_controller.show()

    def open_add_service(self):
        self.add_service_controller = AddEditDeleteServiceController()
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


class AddEditDeleteServiceController(QDialog):
    refresh_services_list = pyqtSignal()

    def __init__(self,service=None):
        super(AddEditDeleteServiceController, self).__init__()
        self.ui = Ui_addEditDeleteService_form()
        self.ui.setupUi(self)
        self.setModal(True)

        self.service = service
        if service:
            self.ui.title_lbl.setText("ویرایش سرویس")
            self.load_service_data_into_txtboxes()
        else:
            self.ui.deleteService_btn.hide()

        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.save_btn.clicked.connect(self.save_service)
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.deleteService_btn.clicked.connect(self.delete_service)

    def load_service_data_into_txtboxes(self):
        self.ui.serviceName_txtbox.setText(self.service["name"])
        self.ui.servicePrice_spnbox.setValue(self.service["price"])

    def save_service(self):
        service_data = {
            'name': self.ui.serviceName_txtbox.text(),
            'price': self.ui.servicePrice_spnbox.value(),
        }

        with DatabaseManager() as db:
            if self.service:
                service_data['id'] = self.service["id"]
                Services.update_service(db, service_data)
                success_message = "سرویس با موفقیت ویرایش شد."
            else:
                Services.add_service(db,service_data)
                success_message = "سرویس با موفقیت اضافه شد."

            QMessageBox.information(self, "موفقیت", success_message)
            self.refresh_services_list.emit()
            self.close()

    def delete_service(self):
        msg_box, yes_button = Messages.show_confirm_delete_msg()
        if msg_box.clickedButton() == yes_button:
            with DatabaseManager() as db:
                Services.delete_service(db,self.service["id"])
                Messages.show_success_msg("سرویس با موفقیت حذف شد.")
                self.close()
                self.refresh_services_list.emit()
        else:
            msg_box.close()