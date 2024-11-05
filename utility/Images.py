from utility import MEDIA_DIR
import os
import uuid
import shutil
import logging

class Images:

    @staticmethod
    def save_image_to_patient_directory(current_image_path,patient_file_number):
        unique_filename = str(uuid.uuid4()) + os.path.splitext(current_image_path)[1]
        new_image_path = os.path.join(patient_file_number , unique_filename)
        shutil.copy(current_image_path, MEDIA_DIR / new_image_path)
        return new_image_path

    @staticmethod
    def delete_image(image_path):
        try:
            if os.path.exists(image_path):
                os.remove(image_path)
        except Exception as e:
            logging.error(str(e))
            raise e
    
    @staticmethod
    def get_default_image_path():
        return MEDIA_DIR / "default.png"
    
    @staticmethod
    def get_media_directory():
        return MEDIA_DIR
