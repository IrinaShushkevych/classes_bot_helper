from classes import Helper

def handler_error(func):
    def print_error(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(e)
            return True
        except IndexError :
            print('Command is wrong')
            return True
        except Exception as e:
            print(e)
            return True
    return print_error


@handler_error
def handler(cmd, helper):
    command =cmd.split(' ')
    if command[0].lower() in helper.handler_command:
        return helper.handler_command[command[0].lower()](*command[1:])
    elif (' '.join(command[0:2]).lower()) in helper.handler_command:
        return helper.handler_command[' '.join(command[0:2]).lower()](*command[2:])
    else:
        raise IndexError

def main():
    helper = Helper()
    while True:
        cmd = input('Enter command (help - show all commands): ')
        if not handler(cmd, helper):
            break
        
if __name__ == '__main__':
    main()

# from classes import AddressBook

# ab = AddressBook()
# ab.print_addressbook()

