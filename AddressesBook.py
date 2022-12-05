from collections import UserDict
from datetime import datetime


class Field:
    pass


class Name(Field):
    def __init__(self, value):
        self.value = value


class Phone(Field):
    def __init__(self):
        self.value = None

    @property
    def number(self):
        return self.value

    @number.setter
    def number(self, value: str):
        if value.isnumeric():
            self.value = value
        else:
            print('Number must contain only digits')


class Birthday:
    def __init__(self, value=None):
        self.value = value

    @property
    def birthday(self):
        return self.value

    @birthday.setter
    def birthday(self, value: str):
        try:
            self.value = datetime.strptime(value, '%d %B %Y')
        except ValueError:
            print('Invalid input form. Need for example: 10 January 2020')





class Record:
    def __init__(self, name):
        self.birthday = Birthday()
        self.name = Name(name)
        self.phone = Phone()
        self.phones = []

    def add_birthday(self, value):
        self.birthday(value)

    def days_to_birthday(self):
        if self.birthday.birthday:
            birthday_in_this_year = datetime(year=datetime.now().year, month=self.birthday.birthday.month, day=self.birthday.birthday.day)
            birthday_in_next_year = datetime(year=datetime.now().year + 1, month=self.birthday.birthday.month, day=self.birthday.birthday.day)
            if birthday_in_this_year < datetime.now():
                days_to_birthday = birthday_in_next_year - datetime.now()
                return days_to_birthday.days
            else:
                days_to_birthday = birthday_in_this_year - datetime.now()
                return days_to_birthday.days

    def add_phone(self, phone):
        self.phone.number = phone
        self.phones.append(self.phone.number)
        print(f"You added {phone} to {self.name.value}")

    def delete_phone(self, phone):
        for p in self.phones:
            if p.number == phone:
                self.phones.remove(p)
                print(f"You remove {phone} from {self.name.value}")
                return True
        return False

    def editing(self, old_phone, new_phone):
        if self.delete_phone(old_phone):
            self.add_phone(new_phone)

    def get_contacts(self):
        result = []
        for phone in self.phones:
            result.append(phone.number)
        return result


class AddressBook(UserDict):
    def __init__(self):
        self.step = 3
        self.boundary = self.step
        self.count = -1
        self.keys = [i for i in self.data.keys()]

    def __iter__(self):
        return self

    def __next__(self):
        if self.count + 1 < self.boundary:
            if self.count + 1  == len(self.keys):
                self.boundary = self.step
                self.count = -1
                raise StopIteration
            self.count += 1
            return self.data[self.keys[self.count]]
        if self.count + 1 == self.boundary:
            self.boundary += self.step
            raise StopIteration

    def add_record(self, Record):
        self.data[Record.name.value] = Record






        