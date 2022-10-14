from datetime import datetime
from classes.field import Field

class Birthday(Field):
    @Field.value.setter
    def value(self, value=None):
        if value and type(value) == str:
            value = value.replace('.', '-')
            try:
                value = datetime.strptime(value, '%d-%m-%Y').date()
            except:
                raise ValueError('Invalid date format. Must be dd-mm-yyyy or dd.mm.yyyy')
        elif value != None:
            raise ValueError('Invalid date format. Must be string dd-mm-yyyy or dd.mm.yyyy')
        self._value = value

    def __repr__(self):
        return datetime.strftime(self.value, '%d-%m-%Y')