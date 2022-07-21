# from os import write
from model import data_manager, util


ID = 0
NAME = 1
EMAIL = 2
STATUS = 3


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]


def list_data():
    data = data_manager.read_table_from_file(DATAFILE)
    HEADER = list(map(lambda x: x.upper(), HEADERS))
    data.insert(ID, HEADER)
    return data


def append(customer):
    data = data_manager.read_table_from_file(DATAFILE)
    id = util.generate_id()
    customer.insert(ID, id)
    data.append(customer)
    data_manager.write_table_to_file(DATAFILE, data)


def check_id(id):
    data = data_manager.read_table_from_file(DATAFILE)
    for row in range(len(data)):
        if id == data[row][ID]:
            return True, row
    return False, 0


def update(data, line_number):
    file = data_manager.read_table_from_file(DATAFILE)
    file[line_number][NAME:] = data
    data_manager.write_table_to_file(DATAFILE, file)


def delete(line_number):
    file = data_manager.read_table_from_file(DATAFILE)
    file.pop(line_number)
    data_manager.write_table_to_file(DATAFILE, file)


def get_emails():
    file = data_manager.read_table_from_file(DATAFILE)
    subscribers = []
    for customer in file:
        if customer[STATUS] == "1":
            subscribers.append(customer[EMAIL])
    return subscribers
