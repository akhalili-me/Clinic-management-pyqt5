from .Numbers import *
from .Dates import *
from .SMS import *
from .Charts import *
from .Images import *
from .LoadingValues import *
from .Messages import *
from .Validators import *
from .Database import *


import shutil
import os
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
        print(f"File '{file_path}' successfully copied to '{new_file_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

