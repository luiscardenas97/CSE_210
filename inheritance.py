class Phone:
    def __init__(self):
        self._phone_number = 0
        self._text_messages = []
    
    def place_call(self, number_to_call):
        pass
    
    def place_text(self, number_to_text, message_to_send):
        pass

    def save_text(self, message_to_save):
        pass

    def get_texts(self,text_message):
        self._text_messages = text_message

    def get_number(self, phone_number):
        self._phone_number = phone_number
        


class CameraPhone(Phone):
    def __init__(self) -> None:
        super().__init__()
        self._pictures = []

    def take_picture(self, picture_name):
        self._pictures.append(picture_name)
