from PyQt5.QtWidgets import QDesktopWidget

ui_mapping = {
    "patientFile": "patient_file",
    "main": "main_window",
    "aAppointmentPatientSearch": "add_appointment_with_patient_search",
    "aeAppointment": "add_edit_appointment",
    "iAppointment": "appointment_info",
    "aedExpense": "add_edit_delete_expense",
    "aedDoctor": "add_edit_delete_doctors",
    "aedService": "add_edit_delete_service",
    "aeImage": "add_edit_images",
    "aePatient": "add_edit_patient",
    "aeMedicalRecord": "add_edit_medical_records",
    "iMedicalRecord": "medical_record_info",
    "aSmsApi": "add_sms_api_key",
}

def get_ui_class(ui_name):
    # Detect screen resolution
    screen = QDesktopWidget().screenGeometry()
    width, height = screen.width(), screen.height()

    # Choose the folder based on resolution
    if width >= 1920 and height >= 1080:
        ui_folder = "ui.720"  # use dot notation for module path
    else:
        ui_folder = "ui.720"

    # Get the Python filename from ui_mapping
    ui_file_name = ui_mapping.get(ui_name)
    if not ui_file_name:
        raise ValueError(f"No UI file mapped for '{ui_name}'")

    # Construct the full module path (e.g., "ui.1080.patient_file")
    module_path = f"{ui_folder}.{ui_file_name}"

    # Import the module and retrieve the UI class
    try:
        ui_module = __import__(module_path, fromlist=[f"Ui_{ui_name}"])
        ui_class = getattr(ui_module, f"Ui_{ui_name}")
    except (ImportError, AttributeError) as e:
        raise ImportError(f"Could not load UI class for '{ui_name}' from '{module_path}': {e}")

    return ui_class
