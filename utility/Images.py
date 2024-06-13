from pathlib import Path
import os
import uuid
import shutil

BASE_DIR = Path(__file__).resolve().parent.parent
IMAGES_DIR = BASE_DIR / "resources" / "images"

class Images:
    @staticmethod
    def create_image_directory_if_not_exist(patient_name):
        directory = Path.joinpath(IMAGES_DIR,patient_name)
        os.makedirs(directory, exist_ok=True)
        return directory

    @staticmethod
    def save_image_to_new_directory(current_image_path,image_directory):
            unique_filename = str(uuid.uuid4()) + os.path.splitext(current_image_path)[1]
            new_image_path = os.path.join(image_directory, unique_filename)
            shutil.copy(current_image_path, new_image_path)
            return new_image_path
   
    def delete_image(image_path):
        try:
            if os.path.exists(image_path):
                os.remove(image_path)
            else:
                raise
        except Exception:
            raise
    
    @staticmethod
    def get_default_image_path():
        return IMAGES_DIR / "default.png"