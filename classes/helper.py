from itertools import count
from classes.addressBook import AddressBook

class Helper:
    def __init__(self):
        self.handler_command = {
            'hello': self.func_hello, 
            'add': self.func_add, 
            'addphone': self.func_add_phone,
            'addbirthday': self.func_add_birthday,
            'rename': self.func_changename, 
            'changephone': self.func_changephone, 
            'changebirthday': self.func_change_birthday, 
            'remove': self.func_remove,
            'delete': self.func_remove,
            'deletephone': self.func_remove_phone,
            'removephone': self.func_remove_phone,
            'phone': self.func_phone,
            'show all': self.func_show_all,
            'exit': self.func_exit, 
            'close': self.func_exit, 
            'good buy': self.func_exit,
            'help': self.func_help,
            'iter': self.func_print_iter
            }
        self.phonebook = AddressBook()

    def check_args(self, count_args=None, name=None, phone=None, birthday=None, *args):
        if count_args == 1:
            if not name:
                raise ValueError('Enter user name')
        elif count_args == 2:
            if not (name and phone):
                raise ValueError('Give me name and phone please')
        elif count_args == 3:
            if not (name and birthday):
                raise ValueError('Give me name and birthday please')
        return True

    def func_hello(self, ):
        print('How can I help you?')
        return True

    def func_exit(self):
        print('Good bye!')
        return False

    def func_add(self, name=None, phone=None, *args):
        self.check_args(1, name, *args)
        self.phonebook.add_record(name, phone, *args)
        print(f'Record {name} is add')
        return True

    def func_add_phone(self, name=None, phone=None, *args):
        self.check_args(1, name, *args)
        self.phonebook.add_phone(name, phone, *args)
        print(f'Phone is add into record {name}')
        return True

    def func_add_birthday(self,name, birthday, *args):
        self.check_args(2, name, birthday, *args)
        self.phonebook.add_birthday(name, birthday)
        print(f'Birthday is add into record {name}')
        return True

    def func_changename(self, name_old=None, name_new=None, *args):
        self.check_args(2, name_old, name_new, *args)
        self.phonebook.change_name(name_old, name_new)
        print(f'Name of record {name_old} is change')
        return True

    def func_changephone(self, name=None, phone_old=None, phone_new=None, *args):
        self.check_args(2, name, phone_old, phone_new, *args)
        self.phonebook.change_phone(name, phone_old, phone_new)
        print(f'Phone {phone_old} of record {name} is change')
        return True

    def func_change_birthday(self, name, birthday, *args):
        self.check_args(3, name, None,  birthday, *args)
        self.phonebook.change_birthday(name, birthday)
        print(f'Birthday of record {name} is change')
        return True

    def func_remove(self, name=None, *args):
        self.check_args(1, name, *args)
        self.phonebook.remove_record(name)
        print(f'Record {name} is delete')
        return True

    def func_remove_phone(self, name=None, phone=None, *args):
        self.check_args(2, name, phone, *args)
        self.phonebook.remove_phone(name, phone, *args)
        print(f'Phone {phone} is delete from record {name}')
        return True

    def func_phone(self, name=None, *args):
        self.check_args(1, name, *args)
        print(self.phonebook.show_phone(name))
        return True

    def func_show_all(self):
        self.phonebook.print_addressbook()
        return True

    def func_help(self):
        print('Commands:')
        print('hello')
        print('add <name> {<phone> {<phone> ...}}')
        print('addphone <name> <phone> {<phone>}')
        print('addbirthday <name> <birthday>')        
        print('changephone <name> <phone old> <phone new>')
        print('rename <name old> <name new>')
        print('phone <name>')
        print('remove <name>')
        print('delete <name>')
        print('removephone <name> <phone> {<phone>}')
        print('deletephone <name> <phone> {<phone>}')
        print('show all')
        print('good by || close || exit')
        print('iter <count element in iteration>')
        return True

    def func_print_iter(self, counts):
        try:
            self.phonebook.set_iter_count(int(counts))
        except:
            raise ValueError(f'{counts} is not integer')
        for el in self.phonebook:
            print(el)
        return True