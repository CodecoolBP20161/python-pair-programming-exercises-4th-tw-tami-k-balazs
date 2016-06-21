class Person():
    _name = None
    _phone_number = None

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number


    def is_phone_number_matching(self, input_phone_number):
        return self.phone_number == input_phone_number

    def get_name(self):
        return self.name

    @staticmethod
    def normalize_phone_number(phone_number):
        phone_number.replace((" ","-"), "")
