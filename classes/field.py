class Field:
    def __init__(self, value):
        if self.check(value):
            self.value = value
    
    def check(self, value):
        return True

    def change(self, value):
        self.value = value

