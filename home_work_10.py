from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        if record.key.name in self.data:
            self.data[record.key.name].update(record.data_dict)
        else:
            self.data[record.key.name] = record.data_dict

    def __str__(self):
        return f'Records in AddressBook: {self.data}'


class Record:

    def __init__(self, name, value, *phone):
        self.data_dict = {}
        self.value = value
        self.key = Name(name)
        self.phones = Phone(list(phone))

        if self.key not in self.data_dict:
            self.data_dict[self.value] = self.phones.phones

    def add_data(self, field, *data):
        if field in self.data_dict:
            for data_element in data:
                self.data_dict[field].append(data_element)
        else:
            self.data_dict[field] = list(data)

    def delete_data_in_field(self, field):
        for key, value in self.data_dict.items():
            if key == field:
                value.clear()

    def __str__(self):
        return f'{self.data_dict}'


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, phone):
        self.phones = phone
