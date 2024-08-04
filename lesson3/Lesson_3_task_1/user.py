class User:
    def __init__(self, fairst_name, last_name):
        self.first_name = fairst_name
        self.last_name = last_name
    def print_first_name(self):
        print(self.first_name)
    def print_last_name(self):
        print(self.last_name)
    def print_full_name(self):
        print(f'{self.first_name} {self.last_name}')