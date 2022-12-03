import os
from cashier import Transaction


# Common Messages During User Interaction
MENU_NOT_AVAILABLE_MSG = "Menu is not Available, Please Select \
    the Available Menu"
SELECTION_NOT_INTEGER_MSG = "Please Enter Numbers, not String"
BACK_TO_MAIN_MENU_MSG = "\nBack to main Menu\n"


def add_new_item_menu(transaction_class, command):
    """Adding item to the transaction

    The main menu will be cleared and the adding item menu is prompted.
    User will be asked to input the item name, item quantity and
    item price in order. When the input is finished
    it will call Transaction.add_item() method.

    Parameters
    ----------
    transaction_class : Class
       The Transaction Class object.

    command : str
        The command to clear the
    """

    # Clear the main menu
    os.system(command)

    # Displaying the add item menu
    print("================================================\n",
          "** Please adding item to the menu accordingly **\n",
          "================================================\n")
    item_name = input("Enter the Item Name [String]: ")
    item_qty = input("Enter the Item Quantity [Integer]: ")
    item_price = input("Enter the Item Price [Integer]: ")

    # Calling the transaction_class.add_item method
    message = transaction_class.add_item(
                item_name=item_name,
                item_qty=item_qty,
                item_price=item_price)
    print(message)


def modify_item_menu(transaction_class, command):
    """Displaying transaction modification menu.

    The main menu will be cleared and then user will be prompted with menu
    to be selected with integer:
    - Menu 1 - Update Old Item Name with the new one
        User will enter the old item name to be replaced and the new item name
        then it will call Transaction.update_item_name() method and
        update the transaction.
    - Menu 2 - Update the current item quantity with the new quantity
        User will be asked to enter the item name of the quantity (qty)
        they want to update. Then it will call Transaction.update_item_qty()
        method and update the transaction.
    - Menu 3 - Update the current item price with the new item price
        User will be asked to enter the item name of the price they
        want to update along with the new price value. Then it will call
        Transaction.update_item_price() method and update the transaction
    - Menu 4 - Back to main menu
        User decide to not update any value in the transaction,
        and back to main menu.

    Parameters
    ----------
    transaction_class : Class
       The Transaction Class object.

    command : str
        The command to clear the

    Exceptions
    ----------
    ValueError:
        If the user enter string when they select the menu,
        the exception will be raised, then it will print warning message
        and reset is cancelled.
    """

    # Clear the main menu
    os.system(command)

    # Displaying the modify transaction menu
    print("================================\n",
          "** Modifying Transaction Menu **\n",
          "================================\n"
          "1. Update Item Name\n"
          "2. Update Item Quantity\n"
          "3. Update Item Price\n"
          "4. Back to Main Menu\n")

    try:
        choice = int(input("Select Menu [1-4]: "))
        if (choice == 1):
            # Prompt input the be submitted by user
            item_name = input("\nEnter The Item Name: ")
            new_item_name = input("Enter The New Item Name: ")

            # Call Transation.update_item_name() method
            message = transaction_class.update_item_name(
                item_name=item_name,
                new_item_name=new_item_name)
            print(message)
        elif (choice == 2):
            # Prompt input the be submitted by user
            qty_item_name = input("\nEnter The Item Name: ")
            new_item_qty = input("Enter The New Quantity of the Item: ")

            # Call Transation.update_item_qty() method
            message = transaction_class.update_item_qty(
                item_name=qty_item_name,
                new_item_qty=new_item_qty)
            print(message)
        elif (choice == 3):
            # Prompt input the be submitted by user
            price_item_name = input("\nEnter The Item Name: ")
            new_item_price = input("Enter The New Price of the Item: ")

            # Call Transation.update_item_price() method
            message = transaction_class.update_item_price(
                item_name=price_item_name,
                new_item_price=new_item_price)
            print(message)
        elif (choice == 4):
            print(BACK_TO_MAIN_MENU_MSG)
        else:
            print(MENU_NOT_AVAILABLE_MSG)
    except (ValueError):
        print(SELECTION_NOT_INTEGER_MSG)


def delete_item_menu(transaction_class, command):
    """Displaying the menu for deleting single item

    The function will ask user to enter the name of the item
    they want to delete. Then it will call Transaction.delete_item method
    to execute the deletion.

    Parameters
    ----------
    transaction : Class
       The Transaction Class object.
    command : str
        The command to be used to clear the CLI
    """

    # Clearing the main menu
    os.system(command)

    # Displaying the delete menu
    print("================================\n"
          + "** Delete Single Item Menu    **\n"
          + "================================\n")
    item_name = input("Please Enter the Item Name to be Deleted: ")

    print(f"\nAre You Sure You want to delete '{item_name}' item?\n"
          + "1. Yes\n"
          + "2. No\n")

    try:
        choice = int(input("Select The Menu [1-2]: "))
        if (choice == 1):
            # Calling Transaction.delete_item() method
            message = transaction_class.delete_item(item_name=item_name)
            print(message)
        elif (choice == 2):
            print(BACK_TO_MAIN_MENU_MSG)
        else:
            print(MENU_NOT_AVAILABLE_MSG)
    except (ValueError):
        print(SELECTION_NOT_INTEGER_MSG)


def reset_menu(transaction_class):
    """Displaying the option whether user want to reset transaction or not.

    User will be asked to select whether to chose to delete 
    all item in transaction or not.

    Parameters
    ----------
    transaction_class : Class
       The Transaction Class object.

    Exceptions
    ----------
    ValueError:
        If the user enter string when they select the menu,
        the exception will be raised, then it will print warning message
        and reset is cancelled.
    """

    print("\nAre You Sure you Want to Delete all of the Transaction\n"
          "1. Yes\n"
          "2. No\n")

    try:
        choice = int(input("Select Menu [1-3]: "))
        if (choice == 1):
            message = transaction_class.reset_transaction()
            print(message)
        elif (choice == 2):
            print("\nDelete is Cancelled, Back to Main Menu")
        else:
            print(MENU_NOT_AVAILABLE_MSG)
    except (ValueError):
        print(SELECTION_NOT_INTEGER_MSG)


def main():
    """Displaying the main menu of the application

    The function will instantiate Transaction function in
    the transact varialble everytime the program is run.
    The program will show CLI-Based menu, where the user can select
    option based on The number of the menu. If the user select the number
    outside the number on the menu warning message will be shown.

    Exceptions
    ----------
    ValueError
        The exception will raise if a user enter string instead of an integer.
    """

    trnsct_123 = Transaction()

    # Select Clear Command for the Command Line Interface based on the OS
    clear_command = "cls" if os.name == "nt" else "clear"

    # Main Menu For Our Program
    while True:
        print("=======================================\n"
              + "**   Cashier Application             **\n"
              + "=======================================\n"
              + "1. Add Item for Transaction\n"
              + "2. Modify Item in Transaction\n"
              + "3. Delete Item in Transaction\n"
              + "4. Delete All of the Transactions\n"
              + "5. Check Transaction\n"
              + "6. Check Total Amount of Transaction\n"
              + "7. Exit From Program\n")

        try:
            choice = int(input("Select Menu [1-7]: "))
            if (choice == 1):
                add_new_item_menu(trnsct_123, clear_command)
            elif (choice == 2):
                modify_item_menu(trnsct_123, clear_command)
            elif (choice == 3):
                delete_item_menu(trnsct_123, clear_command)
            elif (choice == 4):
                reset_menu(trnsct_123)
            elif (choice == 5):
                message = trnsct_123.check_order()
                print(message)
            elif (choice == 6):
                message = trnsct_123.total_price()
                print(message)
            elif (choice == 7):
                exit()
            else:
                print(MENU_NOT_AVAILABLE_MSG)

            input("\nPress Enter to Continue\n")
            os.system(clear_command)
        except (ValueError):
            print(SELECTION_NOT_INTEGER_MSG)
            input("\nPress Enter to Continue\n")
            os.system(clear_command)


if __name__ == "__main__":
    main()
