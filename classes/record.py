from datetime import datetime, date
from classes.name import Name
from classes.phone import Phone
from classes.birthday import Birthday

class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = Name(name)
        self.birthday = Birthday(birthday)
        self.phones = []
        if phone:
            self.phones.append(Phone(phone))

    def __setitem__(self, index, value):
        if index == 'birthday':
            if not self.birthday:
                self.birthday = Birthday(value)
            else:
                self.birthday.value = value
        elif index == 'name':
            self.name.value = value
        else: 
            raise KeyError(f'Wrong key {index}')

    def __getitem__(self, index):
        if index == 'birthday':
            return self.birthday.value 
        elif index == 'name':
            return self.name.value 
        else: 
            raise KeyError(f'Wrong key {index}')
            
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

    def days_to_birthday(self):
        if not self.birthday.value:
            return ""
        now = date.today()
        birth = date(now.year, self.birthday.value.month, self.birthday.value.day)
        if birth < now:
            birth = date(now.year + 1, self.birthday.value.month, self.birthday.value.day)
        return (birth - now).days

    def is_contain(self, keys):
        if self.name.is_contain(keys):
                return True
        for phone in self.phones:
            if phone.is_contain(keys):
                return True

    def __repr__(self):
        string = f'Record : ( {self.name.value} ['
        for el in self.phones:
            string += f'{el.value}, '
        string = string[:len(string)-2]
        string += f'] {self.birthday.value})'
        return string