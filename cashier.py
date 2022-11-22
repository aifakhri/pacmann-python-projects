import os
from script import Transaction



MENU_NOT_AVAILABLE_MSG = "Menu is not Available, Please Select the Available Menu"
SELECTION_NOT_INTEGER = "Please Enter Numbers, not String"



def add_new_item_menu(cart):
    item_name = input("Enter the Item Name: ")
    item_qty = int(input("Enter the Item Quantity [Integer]: "))
    item_price = int(input("Enter the Item Price [Integer]: "))
    cart.add_item(name=item_name, qty=item_qty, price=item_price)


def modify_item_menu(cart, clear_command):
    os.system(clear_command)
    print("1. Update Item Name\n"
          "2. Update Item Quantity\n"
          "3. Update Item Price\n"
          "4. Back to Main Menu\n")
    
    try:
        choice = int(input("Select The Menu [1-4]: "))
        if (choice == 1):
            item_name = input("Enter The Item Name: ")
            new_item_name = input("Enter The New Item Name: ")
            cart.update_item_name(name=item_name, new_mame=new_item_name)
        elif (choice == 2):
            qty_item_name = input("Enter The Item Name: ")
            new_item_qty = input("Enter The New Quantity of the Item: ")
            cart.update_item_qty(name=qty_item_name, new_qty=new_item_qty)
        elif (choice == 3):
            price_item_name = input("Enter The Item Name: ")
            new_item_price = input("Enter The New Price of the Item: ")
            cart.update_item_name(name=price_item_name, new_price=new_item_price)
        else:
            print(MENU_NOT_AVAILABLE_MSG)
    except ValueError:
        print(SELECTION_NOT_INTEGER)

def reset_cart_menu(cart, clear_command):
    os.system(clear_command)
    print("Are You Sure you Want to Delete all of the Transaction\n"
          "1. Yes\n"
          "2. No\n"
          "3. Back to Main Menu")
    
    try:
        choice = int(input("Select Menu [1-3]: "))

        if (choice == 1):
            cart.reset_transaction()
        elif (choice == 2):
            print("\nDelete is Cancelled, Back to Main Menu")
        else:
            print("\nPlease Select the Available Menu")
    except ValueError:
        print(SELECTION_NOT_INTEGER)

def delete_item_menu(cart, clear_command):
    os.system(clear_command)
    item_name = input("\nPlease Enter the Item Name to be Deleted: ")
    cart.delete(name=item_name)


def main():
    """
    """
    cart = Transaction()

    ## Select Clear Command for the Command Line Interface based on the OS
    clear_command = "cls" if os.name == "nt" else "clear"

    # Setup the Menu For Our Program
    while True:
        print("1. Add Item for Transaction\n"
              "2. Modify Item in Transaction\n"
              "3. Delete Item in Transaction\n"
              "4. Delete All of the Transactions\n"
              "5. Check Transaction\n"
              "6. Check Total Amount of Transaction\n"
              "7. Exit From Program\n")

        try:
            choice = int(input("Select Menu [1-7]: "))
            if (choice == 1):
                add_new_item_menu(cart)
            elif (choice == 2):
                modify_item_menu(cart, clear_command)
            elif (choice == 3):
                delete_item_menu(cart, clear_command)
            elif (choice == 4):
                reset_cart_menu(cart, clear_command)
            elif (choice == 5):
                cart.check_order()
            elif (choice == 6):
                cart.total_price()
            elif (choice == 7):
                exit()
            else:
                print("Menu Tidak Tersedia, Harap Pilih Menu Yang Tersedia")

            input("\nPress Enter to Continue")
            os.system(clear_command)
        except ValueError:
            print(SELECTION_NOT_INTEGER)
            os.system(clear_command)

if __name__ == "__main__":
    main()