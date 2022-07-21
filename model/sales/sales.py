from model import data_manager, util


ID = 0
CUSTUMER = 1
PRODUCT = 2
PRICE = 3
DATE = 4


DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]


def list_data():
    data = data_manager.read_table_from_file(DATAFILE)
    HEADER = list(map(lambda x: x.upper(), HEADERS))
    data.insert(ID, HEADER)
    return data


def append(customer):
    data = data_manager.read_table_from_file(DATAFILE)
    id = util.generate_id()
    customer.insert(0, id)
    id = util.generate_id()
    customer.insert(1, id)
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
    file[line_number][PRODUCT:] = data
    data_manager.write_table_to_file(DATAFILE, file)


def delete(line_number):
    file = data_manager.read_table_from_file(DATAFILE)
    file.pop(line_number)
    data_manager.write_table_to_file(DATAFILE, file)


def biggest_revenue_id():
    file = data_manager.read_table_from_file(DATAFILE)
    counter = 0
    biggest = []
    for row in range(len(file)):
        if float(file[row][PRICE]) > counter:
            counter = float(file[row][PRICE])
    for row in range(len(file)):
        if float(file[row][PRICE]) == counter:
            biggest.append(file[row][ID])
    return biggest


def biggest_revenue_name():
    file = data_manager.read_table_from_file(DATAFILE)
    revenues = {}
    for row in file:
        if row[PRODUCT] not in revenues.keys():
            revenues[row[PRODUCT]] = float(row[PRICE])
        else:
            revenues[row[PRODUCT]] += float(row[PRICE])
    return list([max(revenues, key=revenues.get)])


def count_transactions(dates):
    start = dates[0].split("-")
    end = dates[1].split("-")
    start_date = (int(start[0]), int(start[1]), int(start[2]))
    end_date = (int(end[0]), int(end[1]), int(end[2]))
    file = data_manager.read_table_from_file(DATAFILE)
    counter = 0
    for row in file:
        date = row[-1].split("-")
        product_date = (int(date[0]), int(date[1]), int(date[2]))
        if start_date <= product_date <= end_date:
            counter += 1
    return counter


def count_transaction_sum(dates):
    start = dates[0].split("-")
    end = dates[1].split("-")
    start_date = (int(start[0]), int(start[1]), int(start[2]))
    end_date = (int(end[0]), int(end[1]), int(end[2]))
    file = data_manager.read_table_from_file(DATAFILE)
    counter = 0
    for row in file:
        date = row[-1].split("-")
        product_date = (int(date[0]), int(date[1]), int(date[2]))
        if start_date <= product_date <= end_date:
            counter += float(row[3])
    return counter
