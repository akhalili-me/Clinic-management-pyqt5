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
    @staticmethod
    def limit_text_edit(text_edit):
        max_length = 150  # Limit to 100 characters
        if len(text_edit.toPlainText()) > max_length:
            text_edit.textCursor().deletePreviousChar()



        