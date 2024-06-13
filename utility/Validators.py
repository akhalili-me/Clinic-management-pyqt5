from utility import Messages

class Validators:
    @staticmethod
    def validate_empty_txt_boxes(txtboxes):
        for txtbox in txtboxes:
            name = txtbox["name"]
            text = txtbox["text"]
            if len(text.strip()) == 0:
                Messages.show_error_msg(f"{name} نباید خالی باشد.")
                return False
        return True
        