# from os import read
from model.crm import crm
from view import terminal as view


def list_customers():
    result = crm.list_data()
    view.print_table(result)


def add_customer():
    data = view.get_inputs(["Name", "Email", "Sub"])
    crm.append(data)


def update_customer():
    id = view.get_input("ID")
    check, line_number = crm.check_id(id)
    if check is True:
        data = view.get_inputs(["Name", "Email", "Sub"])
        crm.update(data, line_number)
    else:
        view.print_error_message("This ID is not existing!")


def delete_customer():
    id = view.get_input("ID")
    check, line_number = crm.check_id(id)
    if check is True:
        crm.delete(line_number)
    else:
        view.print_error_message("This ID is not existing!")


def get_subscribed_emails():
    results = crm.get_emails()
    view.print_general_results(results, "Subscribed emails")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
