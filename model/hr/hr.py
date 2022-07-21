from model import data_manager, util


ID = 0
NAME = 1
BIRTH = 2
DEPARTMENT = 3
CLEARANCE = 4


DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


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
    if int(customer[-1]) > 7:
        raise KeyError
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
    if int(data[-1]) > 7:
        raise KeyError
    data_manager.write_table_to_file(DATAFILE, file)


def delete(line_number):
    file = data_manager.read_table_from_file(DATAFILE)
    file.pop(line_number)
    data_manager.write_table_to_file(DATAFILE, file)


def get_age_names():
    file = data_manager.read_table_from_file(DATAFILE)
    list = []
    for row in range(len(file)):
        date = file[row][BIRTH].split("-")
        date_tuple = (int(date[0]+date[1]+date[2])), (file[row][1])
        list.append(date_tuple)
    list.sort(key=lambda x: x[0])
    oldest = list[0][1]
    youngest = list[-1][1]
    return (oldest, youngest)


def average_age():
    file = data_manager.read_table_from_file(DATAFILE)
    list = []
    for row in range(len(file)):
        date = file[row][BIRTH].split("-")
        date_tuple = (int(date[0]), int(date[1]), int(date[2]))
        list.append(date_tuple)
    sum_age = 0
    for i in list:
        sum_age += i[0]
    return 2021-int(sum_age/len(list))


def get_next_birthdays(input_date):
    file = data_manager.read_table_from_file(DATAFILE)
    months = {
        "1": 31,
        "2": 28,
        "3": 31,
        "4": 30,
        "5": 31,
        "6": 30,
        "7": 31,
        "8": 31,
        "9": 30,
        "10": 31,
        "11": 30,
        "12": 31}
    date_tuple_list = []
    for row in range(len(file)):
        date = file[row][BIRTH].split("-")
        date_tuple = (int(date[0]), int(date[1]), int(date[2]))
        date_tuple_list.append(date_tuple)
    day_counter_list = []
    for dates in date_tuple_list:
        counter = 0
        for key, value in months.items():
            counter += value
            if str(dates[1]) == key:
                counter += dates[2] - value
                break
        day_counter_list.append([counter, dates[0]])
    requested_day_counter_list = []
    counter = 0
    requested_date = input_date.split("-")
    requested_date_tuple = (int(requested_date[0]), int(requested_date[1]), int(requested_date[2]))
    for key, value in months.items():
        counter += value
        if str(requested_date_tuple[1]) == key:
            counter += requested_date_tuple[2] - value
            break
    requested_day_counter_list.append([counter, requested_date_tuple[0]])
    birthday_names = []
    for i in range(len(day_counter_list)):
        day_difference = requested_day_counter_list[0][0] - day_counter_list[i][0]
        year_difference = requested_day_counter_list[0][-1] - day_counter_list[i][-1]
        if (requested_day_counter_list[0][-1] - abs(year_difference)) % day_counter_list[i][-1] == 0 and day_difference >= -14 and day_difference <= 0:
            birthday_names.append(file[i][NAME])
        if ((requested_day_counter_list[0][-1] - abs(year_difference))) % day_counter_list[i][-1] == 0 and day_difference >= 351:
            birthday_names.append(file[i][NAME])
    return birthday_names


def get_clearance_level(level):
    file = data_manager.read_table_from_file(DATAFILE)
    counter = 0
    for row in file:
        if int(row[CLEARANCE]) >= int(level):
            counter += 1
    if int(level) > 7:
        raise KeyError
    return counter


def get_employees_per_dep():
    file = data_manager.read_table_from_file(DATAFILE)
    departments = {}
    for row in file:
        if row[DEPARTMENT] in departments:
            departments[row[DEPARTMENT]] += 1
        else:
            departments[row[DEPARTMENT]] = 1
    return departments
