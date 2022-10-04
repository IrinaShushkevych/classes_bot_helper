from classes.userDict import UserDict
from classes.record import Record


class AddressBook(UserDict):
    def __init__(self, path='phonebook.txt'):
        self.path = path
        self.read_phonebook()

    def read_phonebook(self): 
        self.records = []
        with open('phonebook.txt') as f:
            line = f.readlines()
        for el in line:
            element = (el.replace('\n','')).split(' ')
            self.records.append(Record(*element))
    
    def write_phoneook(self):
        with open('phonebook.txt', 'w') as f:
            for record in self.records:
                line = record.name.value
                for phone in record.phones:
                    line += ' ' + phone.value
                f.write(line + '\n')

    def show_phone(self, name, *args):
        for record in self.records:
            if record.name.value.lower() == name.lower():
                lists = []
                for phone in record.phones:
                    lists.append(phone.value)
                return ', '.join(lists)
        raise ValueError(f'Can not find record {name}')
        
    def add_record(self, name, *args):
        self.records.append(Record(name, *args))

    def remove_record(self, name, *args):
        for record in self.records:
            if record.name.value.lower() == name.lower():
                self.records.remove(record)
                return
        raise ValueError(f'Can not find record {name}')

    def add_phone(self, name, *args):
        for record in self.records:
            if record.name.value.lower() == name.lower():
                record.add(*args)
                return
        raise ValueError(f'Can not find record {name}')
        
    def change_name(self, name, new_name):
        for record in self.records:
            if record.name.value == name:
                record.name.change(new_name)
                return
        raise ValueError(f'Can not find record {name}')

    def change_phone(self, name, phone_old, new_phone):
        for record in self.records:
            if record.name.value.lower() == name.lower():
                for phone in record.phones:
                    if phone.value.lower() == phone_old.lower():
                        phone.change(new_phone)
                        return
        raise ValueError(f'Can not find record {name}')

    def remove_phone(self, name, *args):
        for record in self.records:
            if record.name.value.lower() == name.lower():
                for phone in args:
                    for rec_phone in record.phones:
                        if rec_phone.value.lower() == phone.lower():
                            record.phones.remove(rec_phone)
                            return
        raise ValueError(f'Can not find record {name}')

    def print_addressbook(self):
        counts = 0
        for record in self.records:
            if len(record.phones) > counts:
                counts = len(record.phones)
        print('-'*(22 + (counts*21)))
        s = '|{:^20}|{:^' + str(counts*20 + counts - 1) + '}|'
        print(s.format('Name', 'Phone'))
        print('-'*(22 + (counts*21)))
        for record in self.records:
            lists = [record.name.value]
            s = '|{:^20}|'
            for phone in record.phones:
                s += '{:^20}|'
                lists.append(phone.value)
            if counts - len(record.phones) > 0:
                s += '{:^' + str(20*(counts - len(record.phones)) ) + '}|'
                for _ in range(counts - len(record.phones), counts + 1):
                    lists.append('')
            print(s.format(*lists))
        print('-'*(22 + (counts*21)))
            
