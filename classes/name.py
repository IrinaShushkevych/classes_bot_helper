from classes.field import Field

class Name(Field):
    def check(self, value):
        if not value:
            raise ValueError('Enter user name')
        return True
