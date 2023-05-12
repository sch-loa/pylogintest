class InvalidUsername(Exception):
    def __init__(self):
        super().__init__('The given username does not exist.')

class InvalidPassword(Exception):
    def __init__(self):
        super().__init__('The given password is not correct.')
