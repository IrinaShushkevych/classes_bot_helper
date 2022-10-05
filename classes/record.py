from classes.name import Name
from classes.phone import Phone

class Record:
    def __init__(self, name, *args):
        self.name = Name(name)
        self.phones = []
        if args:
            for phone in args:
                self.phones.append(Phone(phone))

    def add(self, *args):
        if args:
            for phone in args:
                self.phones.append(Phone(phone))

    def remove(self, value):
        for phone in self.phones:
            if phone.value == value:
                self.phone.remove(phone)

    def change(self, value, new_value):
        for i in range(0, len(self.phones)):
            if self.phones[i].value == value:
               self.phones[i].change(new_value)

    def rename(self, name):
        self.name.change(name)
        return self