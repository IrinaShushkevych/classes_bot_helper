from collections import UserDict
from classes.record import Record


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.start_index = 0
        self.count_index = 2

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

    def remove_record(self, name):
        name = name.capitalize()
        try:
            self.data.__delitem__(name)
        except KeyError:
            raise ValueError(f'Can not find record {name}')

    def add_phone(self, name, phone):
        name = name.capitalize()
        try:
            self.data[name].add(phone)
        except KeyError:
            raise ValueError(f'Can not find record {name}')

    def add_birthday(self, name, birthday):
        name = name.capitalize()
        try:
            self.data[name]['birthday'] = birthday
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

    def change_phone(self, name, phone_old, new_phone):
        name = name.capitalize()
        try:
            self.data[name].change(phone_old, new_phone)
        except KeyError:
            raise ValueError(f'Can not find record {name}')

    def change_birthday(self, name, birthday):
        name = name.capitalize()
        try:
            self.data[name]['birthday'] = birthday
        except KeyError:
            raise ValueError(f'Can not find record {name}')

    def remove_phone(self, name, phone=None):
        name = name.capitalize()
        if phone: 
            try:
                for rec_phone in self.data[name].phones:
                    if rec_phone.value.lower() == phone.lower():
                        self.data[name].phones.remove(rec_phone)
                        return
            except KeyError:
                raise ValueError(f'Can not find record {name}')

    def print_addressbook(self):
        counts = 0
        for name in self.data:
            if len(self.data[name].phones) > counts:
                counts = len(self.data[name].phones)
            self.data[name].days_to_birthday()
        if counts > 0:
            print('-'*(22 + (counts*21) + 21))
            s = '|{:^20}|{:^' + str(counts*20 + counts - 1) + '}|{:^20}|'
            print(s.format('Name', 'Phone', 'Days to birthday'))
            print('-'*(22 + (counts*21) + 21))
            for record in self.data:
                lists = [record]
                s = '|{:^20}|'
                for phone in self.data[record].phones:
                    s += '{:^20}|'
                    lists.append(phone.value)
                if counts - len(self.data[record].phones) > 0:
                    if counts - len(self.data[record].phones) == 1:
                        s += '{:^' + str(20*(counts - len(self.data[record].phones))) + '}|'
                    else:
                        s += '{:^' + str(20*(counts - len(self.data[record].phones)) + 1*(counts-2)) + '}|'
                    for _ in range(counts - len(self.data[record].phones), counts + 1):
                        lists.append('')
                if self.data[record].birthday.value:
                    lists.append(self.data[record].days_to_birthday())
                else:
                    lists.append('')
                s += '{:^20}|'
                print(s.format(*lists))
            print('-'*(22 + (counts*21) + 21))
        else:
            print('No records')
            
