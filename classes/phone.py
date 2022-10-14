import re
from classes.field import Field

class Phone(Field):
    @Field.value.setter
    def value(self, value=None):
        if value:
            result = re.match(r"^\d{3}\-\d{3}\-\d{2}\-\d{2}|\d{3}\-\d{3}\-\d{1}\-\d{3}$", value)
            if not result:
                raise ValueError('Invalid phone number.Must be 066-123-45-67 or 066-123-4-567')
        self._value = value

