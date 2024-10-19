# controllers/add_patient_controller.py
from PyQt5.QtWidgets import QDialog
from ui import Ui_addEditDeleteService_form,Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSignal
from models import Services,DatabaseWorker,DatabaseManager
from PyQt5.QtWidgets import QListWidgetItem
from utility import Numbers,Messages,BaseController

class ServicesTabController(BaseController):
    def __init__(self, ui:Ui_MainWindow):
        self.ui = ui
        self.current_worker = None
        self.load_services_list()
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.addServices_btn.clicked.connect(self.open_add_service)
        self.ui.services_lst.itemDoubleClicked.connect(self.open_edit_delete_service)

    def open_edit_delete_service(self, item):
        service_id = item.data(1)
        with DatabaseManager() as db:
            try:
                service = Services.get_by_id(db,service_id)
            except Exception as e:
                Messages.show_error_msg(str(e))
                return
        self.open_delete_edit_service_controller = AddEditDeleteServiceController(service)
        self.open_delete_edit_service_controller.refresh_services_list.connect(self.load_services_list)
        self.open_delete_edit_service_controller.show()

    def open_add_service(self):
        self.add_service_controller = AddEditDeleteServiceController()
        self.add_service_controller.refresh_services_list.connect(self.load_services_list)
        self.add_service_controller.show()

    def load_services_list(self):
        self.current_worker = DatabaseWorker(Services.get_all)
        self.current_worker.result_signal.connect(self.display_services_data)
        self.current_worker.error_signal.connect(self.handle_error)
        self.current_worker.start()

    def display_services_data(self,all_services):
        self.ui.services_lst.clear()
        for service in all_services:
            persian_price = Numbers.int_to_persian_with_separators(service["price"])
            item_txt = f"{service['name']} | قیمت: {persian_price} تومان"
            item = QListWidgetItem(item_txt)
            item.setData(1, service['id'])
            self.ui.services_lst.addItem(item)
    

class AddEditDeleteServiceController(BaseController,QDialog):
    refresh_services_list = pyqtSignal()

    def __init__(self,service=None):
        super(AddEditDeleteServiceController, self).__init__()
        self.ui = Ui_addEditDeleteService_form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.current_worker = None
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

        if self.service:
            service_data['id'] = self.service["id"]
            self.update_service(service_data)
        else:
            self.add_service(service_data)
            

    def add_service(self, service):
        print(service)
        self.current_worker = DatabaseWorker(Services.add_service, service)
        self.current_worker.success_signal.connect(lambda: self.operation_successful("سرویس با موفقیت اضافه شد."))
        self.current_worker.error_signal.connect(self.handle_error)
        self.current_worker.start()

    def update_service(self, service):
        self.current_worker = DatabaseWorker(Services.update_service,service)
        self.current_worker.success_signal.connect(lambda: self.operation_successful("سرویس با موفقیت ویرایش شد."))
        self.current_worker.error_signal.connect(self.handle_error)
        self.current_worker.start()

    def operation_successful(self,success_msg):
        QMessageBox.information(self, "موفقیت", success_msg)
        self.refresh_services_list.emit()
        self.close()

    def delete_service(self):
        msg_box, yes_button = Messages.show_confirm_delete_msg()
        if msg_box.clickedButton() == yes_button:
            self.current_worker = DatabaseWorker(Services.delete_service,self.service["id"])
            self.current_worker.success_signal.connect(lambda: self.operation_successful("سرویس با موفقیت حذف شد."))
            self.current_worker.error_signal.connect(self.handle_error)
            self.current_worker.start()
        else:
            msg_box.close()
