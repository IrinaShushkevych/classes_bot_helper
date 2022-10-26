from operator import truediv


class Field:
    def __init__(self, value=None):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def is_contain(self, key):
        if key in self._value:
            return True
        return False