import sys
from pathlib import Path

def get_base_path():
    """ Get the base path where the executable or script is running. """
    if getattr(sys, 'frozen', False):
        # Running in a bundled environment, return the executable's directory
        return Path(sys.executable).parent
    else:
        # Running in a development environment, return the script's directory
        return Path(__file__).resolve().parent.parent

def get_media_path():
    """ Get the path to the media directory, creating it if it doesn't exist. """
    media_path = get_base_path() / 'media'
    media_path.mkdir(exist_ok=True)  # Creates the media directory if it doesn't exist
    return media_path

def get_resource_path():
    """ Get the absolute path to the resource, works for both development and packaged applications. """
    try:
        # PyInstaller stores temp files in _MEIPASS when bundled
        base_path = Path(sys._MEIPASS)
    except AttributeError:
        # In development, use the file's parent directory
        base_path = Path(__file__).resolve().parent.parent

    return base_path / 'resources'

RESOURCES_DIR = get_resource_path()
BASE_PATH = get_base_path()
MEDIA_DIR = get_media_path()

from .Messages import *
from .Config import *
from .CustomWidgets import *
from .Numbers import *
from .Dates import *
from .SMS import *
from .Charts import *
from .Images import *
from .LoadingValues import *
from .Validators import *
from .Database import *
from .PDF import *
from .PatientFile import *

from models import DatabaseWorker

import shutil
import os
import logging
from enum import Enum

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

def copy_file_to_directory(file_path, directory, new_file_name):
    try:
        if not os.path.isfile(file_path):
            raise ValueError(f"The specified file does not exist: {file_path}")

        if not os.path.isdir(directory):
            raise ValueError(f"The specified directory does not exist: {directory}")

        new_file_path = os.path.join(directory, new_file_name)
        shutil.copy(file_path, new_file_path)
    except Exception as e:
        logging.error(f"Error occcured: {str(e)}")

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

    def log_error(self, error_message):
        logging.error(f"Error occurred: {error_message}")

    def _start_worker(
        self,
        operation,
        args=[],
        result_callback=None,
        success_callback=None,
        show_error=True,
    ):
        worker = DatabaseWorker(operation, *args)
        if result_callback:
            worker.result_signal.connect(result_callback)
        if success_callback:
            worker.success_signal.connect(success_callback)

        if show_error:
            worker.error_signal.connect(self.handle_error)
        else:
            worker.error_signal.connect(self.log_error)

        self.active_workers.append(worker)
        worker.finished.connect(lambda: self.active_workers.remove(worker))
        worker.start()


def create_patient_directory_if_not_exist(patient_file_number):
    patient_directory = Path.joinpath(MEDIA_DIR,patient_file_number)
    try:
        os.makedirs(patient_directory, exist_ok=True)
    except OSError as e:
        error_msg = f"Error making patient directory: {e.strerror}"
        logging.error(error_msg)
        raise e

def delete_patient_directory(patient_file_number):
    patient_dir = Path.joinpath(MEDIA_DIR,patient_file_number)
    try:
        shutil.rmtree(patient_dir)
    except OSError as e:
        error_msg = f"Error removing patient directory: {e.strerror}"
        logging.error(error_msg)
        raise e

def get_patient_signature_image_path(patient_id):
    return f"{MEDIA_DIR}/{patient_id}/signature.png"
