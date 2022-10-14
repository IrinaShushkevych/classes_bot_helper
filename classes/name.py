from classes.field import Field

class Name(Field):

    @Field.value.setter
    def value(self, value):
        if not value:
            raise ValueError('Enter user name')
        self._value = value