from classes.field import Field

class Name(Field):
    def __init__(self, value):
        if self.check(value):
            self.value = value

    def check(self, value):
        if not value:
            raise ValueError('Enter user name')
        return True
        
    def change(self, value):
        self.value = value