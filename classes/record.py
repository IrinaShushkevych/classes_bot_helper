from classes.name import Name
from classes.phone import Phone

class Record:
    def __init__(self, name, phone=None):
        self.name = Name(name)
        self.phones = []
        if phone:
            self.phones.append(Phone(phone))

    def add(self, phone):
        if phone:
            self.phones.append(Phone(phone))

    def remove(self, value):
        for phone in self.phones:
            if phone.value == value:
                self.phone.remove(phone)

    def change(self, value, new_value):
        enums = list(enumerate(self.phones))
        for i, el in enums:
            if el.value.lower() == value.lower():
               self.phones[i].change(new_value)

    def rename(self, name):
        self.name.change(name)
        return self