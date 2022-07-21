from model.hr import hr
from view import terminal as view


def list_employees():
    result = hr.list_data()
    view.print_table(result)


def add_employee():
    data = view.get_inputs(["Name", "Date of birth", "Department", "Clearance"])
    hr.append(data)


def update_employee():
    id = view.get_input("ID")
    check, line_number = hr.check_id(id)
    if check is True:
        data = view.get_inputs(["Name", "Date of birth", "Department", "Clearance"])
        hr.update(data, line_number)
    else:
        view.print_error_message("This ID is not existing!")


def delete_employee():
    id = view.get_input("ID")
    check, line_number = hr.check_id(id)
    if check is True:
        hr.delete(line_number)
    else:
        view.print_error_message("This ID is not existing!")


def get_oldest_and_youngest():
    names = hr.get_age_names()
    view.print_general_results(names, "Oldest and youngest employees")


def get_average_age():
    sum = hr.average_age()
    view.print_general_results(sum, "The average age of employees")


def next_birthdays():
    date = view.get_input("Date")
    names = hr.get_next_birthdays(date)
    view.print_general_results(names, "Employees whose birthday is approaching")


def count_employees_with_clearance():
    level = view.get_input("Clearance level")
    counter = hr.get_clearance_level(level)
    view.print_general_results(counter, "Employees with the appropriate clearance level")


def count_employees_per_department():
    counter = hr.get_employees_per_dep()
    view.print_general_results(counter, "Employees per departments")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError:
            view.print_error_message("Please enter valid data!")
