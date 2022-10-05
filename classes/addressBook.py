from collections import UserDict
from classes.record import Record


class AddressBook(UserDict):
    def read_phonebook(self, path='phonebook.txt'): 
        with open(path) as f:
            line = f.readlines()
        for el in line:
            element = (el.replace('\n','')).split(' ')
            record = Record(*element)
            self.data[record.name.value.capitalize()] = record
    
    def write_phoneook(self, path='phonebook.txt'):
        with open(path, 'w') as f:
            for record in self.data:
                line = record
                for phone in self.data[record]:
                    line += ' ' + phone.value
                f.write(line + '\n')

    def show_phone(self, name, *args):
        name = name.capitalize()
        try:
            result = self.data[name]
            if self.data[name]:
                lists = []
                for phone in self.data[name].phones:
                    lists.append(phone.value)
                return ', '.join(lists)
        except KeyError:
            raise ValueError(f'Can not find record {name}')
        
    def add_record(self, name, *args):
        record = Record(name.capitalize(), *args)
        self.data.__setitem__(record.name.value, record)

    def remove_record(self, name, *args):
        name = name.capitalize()
        try:
            self.data.__delitem__(name)
            return
        except KeyError:
            raise ValueError(f'Can not find record {name}')

    def add_phone(self, name, *args):
        name = name.capitalize()
        try:
            self.data[name].add(*args)
            return
        except KeyError:
            raise ValueError(f'Can not find record {name}')
        
    def change_name(self, name, new_name):
        name = name.capitalize()
        new_name = new_name.capitalize()
        try:
            record = self.data[name]
            record = record.rename(new_name)
            self.data.__delitem__(name)
            self.data.__setitem__(record.name.value, record)
            return
        except KeyError:
            raise ValueError(f'Can not find record {name}')

    def change_phone(self, name, phone_old, new_phone):
        name = name.capitalize()
        try:
            for phone in self.data[name].phones:
                if phone.value.lower() == phone_old.lower():
                    phone.change(new_phone)
                    return
        except KeyError:
            raise ValueError(f'Can not find record {name}')

    def remove_phone(self, name, *args):
        name = name.capitalize()
        try:
            for phone in args:
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
        if counts > 0:
            print('-'*(22 + (counts*21)))
            s = '|{:^20}|{:^' + str(counts*20 + counts - 1) + '}|'
            print(s.format('Name', 'Phone'))
            print('-'*(22 + (counts*21)))
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
                print(s.format(*lists))
            print('-'*(22 + (counts*21)))
        else:
            print('No records')
            