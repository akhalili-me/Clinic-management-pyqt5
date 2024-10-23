from .Numbers import *
from .Dates import *
from .SMS import *
from .Charts import *
from .Images import *
from .LoadingValues import *
from .Messages import *
from .Validators import *
from .Database import *
from models import DatabaseWorker

import shutil
import os
import logging
from enum import Enum

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA = BASE_DIR / "media"

class SpecialDays(Enum):
    TODAY = "امروز"
    TOOMMORROW = "فردا"
    TWO_DAYS_LATER = "دو روز بعد"
    THREE_DAYS_LATER = "سه روز بعد"
    FOUR_DAYS_LATER = "چهار روز بعد"

class TimeIntervals(Enum):
    CURRENT_MONTH = "ماه جاری"
    LAST_YEAR = "سال گذشته"
    CURRENT_YEAR = "سال جاری"

def restart_app():
    from PyQt5.QtCore import QProcess
    from PyQt5.QtWidgets import QApplication

    QMessageBox.information(None,"راه‌اندازی مجدد", "برنامه با پایگاه داده جدید راه‌اندازی می‌شود.")
    QApplication.quit()
    QProcess.startDetached(sys.executable, sys.argv)



def configure_logs():
    logging.basicConfig(
        filename="app.log",
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True,
        encoding='utf-8'
    )

class BaseController:

    def handle_error(self, error_message):
        Messages.show_error_msg(error_message)
        logging.error(f"Error occurred: {error_message}")

    def _start_worker(self, operation, args=[], result_callback=None, success_callback=None):
        worker = DatabaseWorker(operation, *args)
        if result_callback:
            worker.result_signal.connect(result_callback)
        if success_callback:
            worker.success_signal.connect(success_callback)
        worker.error_signal.connect(self.handle_error)
        self.active_workers.append(worker)
        worker.finished.connect(lambda: self.active_workers.remove(worker))
        worker.start()

def create_patient_directory_if_not_exist(patient_file_number):
    patient_directory = Path.joinpath(MEDIA,patient_file_number)
    try:
        os.makedirs(patient_directory, exist_ok=True)
    except OSError as e:
        error_msg = f"Error making patient directory: {e.strerror}"
        logging.error(error_msg)
        raise e
    
def delete_patient_directory(patient_file_number):
    patient_dir = Path.joinpath(MEDIA,patient_file_number)
    try:
        shutil.rmtree(patient_dir)
    except OSError as e:
        error_msg = f"Error removing patient directory: {e.strerror}"
        logging.error(error_msg)
        raise e

