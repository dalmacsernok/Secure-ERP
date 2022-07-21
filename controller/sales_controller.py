from model.sales import sales
from view import terminal as view


def list_transactions():
    result = sales.list_data()
    view.print_table(result)


def add_transaction():
    data = view.get_inputs(["Product", "Price", "Date"])
    sales.append(data)


def update_transaction():
    id = view.get_input("ID")
    check, line_number = sales.check_id(id)
    if check is True:
        data = view.get_inputs(["Product", "Price", "Date"])
        sales.update(data, line_number)
    else:
        view.print_error_message("This ID is not existing!")


def delete_transaction():
    id = view.get_input("ID")
    check, line_number = sales.check_id(id)
    if check is True:
        sales.delete(line_number)
    else:
        view.print_error_message("This ID is not existing!")


def get_biggest_revenue_transaction():
    biggest = sales.biggest_revenue_id()
    view.print_general_results(biggest, "Biggest revenue transaction")


def get_biggest_revenue_product():
    product = sales.biggest_revenue_name()
    view.print_general_results(product, "Biggest revenue product")


def count_transactions_between():
    dates = view.get_inputs(["Starting date", "Ending date"])
    counter = sales.count_transactions(dates)
    view.print_general_results(counter, "Number of transactions between dates")


def sum_transactions_between():
    dates = view.get_inputs(["Starting date", "Ending date"])
    sum_price = sales.count_transaction_sum(dates)
    view.print_general_results(sum_price, "Sum of transactions between dates")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
