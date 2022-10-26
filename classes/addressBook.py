from collections import UserDict
from genericpath import isfile
import pickle
import os
from unittest import result
from classes.record import Record


class AddressBook(UserDict):
    def __init__(self, filename='phonebook.txt'):
        super().__init__()
        self.start_index = 0
        self.count_index = 2
        self.filename = filename
        self._load_from_file()

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_index > len(self.data) - 1:
            self.start_index = 0
            raise StopIteration
        end_index = self.start_index + self.count_index
        enum = list(enumerate(self.data))[self.start_index:end_index]
        self.start_index = end_index
        result = {}
        for i, el in enum:
            result[el] = self.data[el]
        return result

    def _save_to_file(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.data, f)

    def _load_from_file(self):
        if os.path.isfile(self.filename):
            with open(self.filename, 'rb') as f:
                self.data = pickle.load(f)

    def find(self, keys):
        result = {}
        for key, value in self.data.items():
            if value.name.is_contain(keys):
                result[key] = value
            else:
                for phone in value.phones:
                    if phone.is_contain(keys):
                        result[key] = value
                        break
        return result

    def set_iter_count(self, counts=1):
        self.count_index = counts

    def show_phone(self, name):
        name = name.capitalize()
        try:
            if self.data[name]:
                lists = []
                for phone in self.data[name].phones:
                    lists.append(phone.value)
                return ', '.join(lists)
        except KeyError:
            raise ValueError(f'Can not find record {name}')
        
    def add_record(self, name, phone=None, birthday=None):
        record = Record(name.capitalize(), phone, birthday)
        self.data.__setitem__(record.name.value, record)
        self._save_to_file()

    def remove_record(self, name):
        name = name.capitalize()
        try:
            self.data.__delitem__(name)
            self._save_to_file()
        except KeyError:
            raise ValueError(f'Can not find record {name}')

    def add_phone(self, name, phone):
        name = name.capitalize()
        try:
            self.data[name].add(phone)
            self._save_to_file()
        except KeyError:
            raise ValueError(f'Can not find record {name}')

    def add_birthday(self, name, birthday):
        name = name.capitalize()
        try:
            self.data[name]['birthday'] = birthday
            self._save_to_file()
        except KeyError:
            raise ValueError(f'Can not find record {name}')
  
    def change_name(self, name, new_name):
        name = name.capitalize()
        new_name = new_name.capitalize()
        try:
            record = self.data[name]
        except KeyError:
            raise ValueError(f'Can not find record {name}')
        record['name'] = new_name
        self.data.__delitem__(name)
        self.data.__setitem__(record.name.value, record)
        self._save_to_file()

    def change_phone(self, name, phone_old, new_phone):
        name = name.capitalize()
        try:
            self.data[name].change(phone_old, new_phone)
            self._save_to_file()
        except KeyError:
            raise ValueError(f'Can not find record {name}')

    def change_birthday(self, name, birthday):
        name = name.capitalize()
        try:
            self.data[name]['birthday'] = birthday
            self._save_to_file()
        except KeyError:
            raise ValueError(f'Can not find record {name}')

    def remove_phone(self, name, phone=None):
        name = name.capitalize()
        if phone: 
            try:
                for rec_phone in self.data[name].phones:
                    if rec_phone.value.lower() == phone.lower():
                        self.data[name].phones.remove(rec_phone)
                        self._save_to_file()
                        return
            except KeyError:
                raise ValueError(f'Can not find record {name}')

    def print_addressbook(self, data=None):
        if not data:
            data = self.data
        counts = 0
        for name in data:
            if len(data[name].phones) > counts:
                counts = len(data[name].phones)
            data[name].days_to_birthday()
        if counts > 0:
            print('-'*(22 + (counts*21) + 21))
            s = '|{:^20}|{:^' + str(counts*20 + counts - 1) + '}|{:^20}|'
            print(s.format('Name', 'Phone', 'Days to birthday'))
            print('-'*(22 + (counts*21) + 21))
            for record in data:
                lists = [record]
                s = '|{:^20}|'
                for phone in data[record].phones:
                    s += '{:^20}|'
                    lists.append(phone.value)
                if counts - len(data[record].phones) > 0:
                    if counts - len(data[record].phones) == 1:
                        s += '{:^' + str(20*(counts - len(data[record].phones))) + '}|'
                    else:
                        s += '{:^' + str(20*(counts - len(data[record].phones)) + 1*(counts-2)) + '}|'
                    for _ in range(counts - len(data[record].phones), counts + 1):
                        lists.append('')
                if data[record].birthday.value:
                    lists.append(data[record].days_to_birthday())
                else:
                    lists.append('')
                s += '{:^20}|'
                print(s.format(*lists))
            print('-'*(22 + (counts*21) + 21))
        else:
            print('No records')
            
