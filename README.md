# Pacmann Python Projects - Super Cashier

## Quick Use
If you are interested to run the program feel free to clone this repo and run the ``script.py`` 

## Introduction
### Project Background
An Online Supermarket wants to add a new feature to their application to help their customers or users to add, modify and delete their transactions which contains the name of the items, the quantity of the items, the price of the items that. The desired feature is also required to provide transction checkers to notify user whether their items in their transaction are already valid or not. Also the apps wants to help the users to calculate of the total amount of the transactions along with the discount calculation if the certain amount of transaction is reached.

### Project Objectives and Requirement
From the background above we would provide a solution called **Cashier** program. The program is a Command Line Interface (CLI) progam which is coded in Python. Here are the requirement of the program:
- Absracting the cashier in a Class called Transaction.
- Create class' method for adding item name, item quantity and item price.
- Create class' method for updating item name on the cart.
- Create class' method for updating item quantity of a certain item.
- Create class' method for updating item price of a certain item.
- Create class' method for deleting a single item.
- Create class' method for deleting all of the items.
- Create class' method for checking the transaction, whether there is an empty cart or invalid value inside the cart.
- Create class' method for calculating the total purchase of the entire Transaction. If the the purchase reaches a certain limit, the purchase would be discounted.
- The discount requitements are:
    - if the total price of the purchase is greater than Rp. 500,000 the discount is 10%
    - if the total price of the purchase is greater than Rp. 300,000 the discount is 8%
    - if the total price of the purchase is greater than Rp. 500,000 the discount is 5%

Users can interact with these features through the interactive Command Line Interface (CLI).

### Flow Chart
The program will be created as CLI-based program or application, hence there will be menu for the users to be selected. Each selected menu will trigger another menu to appear and then call the appropriate method in the Transaction class. Here we will explore the flow of the menu and the method.

#### Main Menu Workflow
In the main menu, the Transaction class is instantiated then the main menu is shown and the user can select 7 available menu which leads to another menu or directly call the method in the Transaction class or exit program:
![main menu](workflow/main_menu.jpg)

For add item menu here is the workflow:
![add item menu](workflow/add_item.png)

in this method we also called the Transaction.add_item( method from our class. The workflow of the method can be seen in the diagram above.

For modify menu, it will display another menu and call ``Transaction.update_item_name()``, ``Transaction.update_item_qty()`` and ``Transaction.update_item_price()`` methods. Here are the workflow of the menu and the methods:
![modify item menu](workflow/modify_item_menu.png)
![Transaction update methods](workflow/transaction_update_methods.png)

For the delete menu here is the workflow along with the workflow of the method that is called:
![delete item menu](workflow/delete_item.png)

Here is the menu for for reset all of the items in our transaction and its method:
![reset menu](workflow/reset_item.png)

The menu 5 - 6 will directly call the ``Transaction.check_order()`` and ``Transaction.total_price()`` menu which have the following flowchart:
![check order](workflow/check_order.jpg)
![total price](workflow/total_price.jpg)

## Code Explanation
### The script.py Function
In this Python script we will store the Transaction class. which holds all the requirement of our program. There are few elements in our Class. There are 2 external modules that is imported to this file:
```Python
from copy import deepcopy
from tabulate import tabulate
```
The ``copy.deepcopy()`` is used to create a full copy of an object, whilst ``tabulate.tabulate()`` is used to create a structured table.

#### 1. Class instance
The class instance in this class are the constants that we will use on our class:
```Python
LOWER_AMOUNT = 200000
LOWER_DISCOUNT = 0.05
MID_AMOUNT = 300000
MID_DISCOUNT = 0.08
HIGH_AMOUNT = 500000
HIGH_DISCOUNT = 0.1
TABLE_HEADERS = [
    "Item Name", "Item Quantity", "Price/Item", "Total" 
]
```
#### 2. Class Attributes
There is only one class attribute in our class which is self.containers, which will holds all the transaction items in a Dictionary:
```Python
self.container = {}
``` 

#### 3. Methods
Here are the methods in the Class:
##### 1. ``add_item(item_name, item_qty, item_price)``
Here is the code snippet for the method

```Python
try:
    self.container[item_name] = [int(item_qty), int(item_price)]

    message = "\nItem is successfully Added" 
    return message
except ValueError:
    message = f"\nAdding Item Failed, Quantity: {item_qty} "\
                + f"and Price: {item_price} are Invalid Data" 
    return message
```
The function requires 3 parameters:
* item_name: The name of the item
* item_qty: The quantity of the item
* item_price: The price of the item

The ``item_name`` parameter is used as the dictionary key while the value is a list that contains ``item_qty`` and ``item_price`` parameter.

We have a convention for the order of the list. The index ``0`` is always for the quantity (qty) of the item value, whilst the index ``1`` is always for the price of the value.

There is also an exception that will be raised when the ``ValueError`` is occured due to inability to transform qty and price into integer. The program will return success message if the Exception is not raised, otherwise failed message.

##### 2. ``update_item_name(item_name, new_item_name)``
Here is the code snippet for the method
```Python
try:
    self.container[new_item_name] = self.container.pop(item_name)
    
    message = f"\nCurrent Item Name: {item_name}, "\
              + f"is Successfully Updated to: {new_item_name}"
    return message
except (KeyError):
    message = f"\nItem {item_name} is Not found, \
        please enter the correct name"
    return message
```
The method requires 2 parameters:
* ``item_name``: The item which its name the user want to replace
* ``new_item_name``: The new name of the item

The ``pop()`` method would drop the existing item name value and if the name is not on the self.container dictionary it will catch KeyError exception. When the execption is caught it will return "Item Not Found" message, otheriwse successful message is shown.

##### 3. ``update_item_qty(item_name, new_item_qty)``
Here is the code snippet for the method
```Python
try:
self.container[item_name][0] = int(new_item_qty)

message = "\nUpdating Item Quantity is Successfull"
return message
except (KeyError):
message = f"\nItem {item_name} is Not found "\
            + "please enter the correct name"
return message
except (ValueError):
message = f"\nNew Quantity Value: {new_item_qty} is Invalid"
return message 
```
The method requires 2 parameters:
* ``item_name``: The item which its quantitiy (qty) the user want to replace
* ``new_item_qty``: The new qty of the item

The ``item_name`` parameter is used to find the key of specific item we want to delete. The ``[0]`` syntax indicate the index of the list, where the item quantity is always be in the index ``0`` as per our convention before.

We need to caught 2 Exception here, the first one is the KeyError. It is triggered when the item name is not in the dictionary. The second one is the ValueError, which is triggered when the ``new_qty`` parameter is a string instead of integer or floating point. Each exception will return separate messages based on the error. When exception is not caught success message is shown.

##### 4. ``update_item_price(item_name, new_item_price)``
Here is the code snippet for the method
```Python
try:
    self.container[item_name][1] = int(new_item_price)

    message = "\nUpdating Item Price is Successfull"
    return message
except KeyError:
    message = f"\nItem {item_name} is Not found, "\
              + "Please Enter The Correct Name"
    return message
except ValueError:
    message = f"\nNew Price {new_item_price} Value is Invalid"
    return message
```
The method requires 2 parameters:
* ``item_name``: The item which its price the user want to replace
* ``new_item_qty``: The new price of the item

The ``item_name`` parameter is used to find the key of specific item we want to delete. The ``[1]`` syntax indicate the index of the list, where the item quantity is always be in the index ``1`` as per our convention before.

We need to caught 2 Exception here, the first one is the KeyError. It is triggered when the item name is not in the dictionary. The second one is the ValueError, which is triggered when the ``new_qty`` parameter is a string instead of integer or floating point.

##### 5. ``delete_item(item_name)``
Here is the code snippet for the method
```Python
try:
    del self.container[item_name]

    message = f"\nItem {item_name} Has Been Deleted Successfully"
    return message
except KeyError:
    message = f"\nItem {item_name} is Not found, "\
              + "Please Enter The Correct Name"
    return message
```
The method requires 1 parameter:
* ``item_name``: The item which the user want to delete

The ``del`` statement/keyword is used to delete object. Here we want to delete a single dictionary object hence we just need the ``self.container[item_name]`` syntax because it holds the object of the specific item we want to delete.

The exception KeyError is triggered when the item_name is not available in the dictionary.

##### 6. ``reset_transaction()``
Here is the code snippet for the method
```Python
self.container = {}

message = "All Transactions Have Been Deleted Successfully"
return message
```
This method is used to delete all items in the transaction container. Since the container is in a dictionary, to remote all dictionary values we just put new dictionary instead.

##### 7. ``check_order()``
Here is the code snippet for the method
```Python
# Checking whether the cart is empty or not
if len(self.container) == 0:
    message = "You Have No Transaction, " \
                + "Please Add Item to Your Transaction"
    return message

# Make a Deep Copy for the self.container to maintain data integrity
container_copy = deepcopy(self.container)

# Finding Missing Value or Invalid Value in the self.container
count = 0
for key, value in container_copy.items():
    try:
        if (key == "") or (value[0] == "") or (value[1] == "") \
            or (key.isdigit()) or (type(int(value[0])) is not int) \
                or (type(int(value[0])) is not int):
            count += 1
        else:
            amount = int(container_copy[key][0])*int(container_copy[key][1])
            container_copy[key].append(amount)
    except (ValueError):
        count += 1

# Deciding whether the input is valid or not
if count == 0:
    print("\nYour Input is Valid\n")
elif count > 0:
    print("\nYour Input is Invalid\n")

# Gather the Value of the dictionary
data = [value for value in container_copy.values()]

# Insert the self.container dictionary key into list in the data
for num, key in enumerate(container_copy):
    data[num].insert(0, key)

# Transform the data into table with tabulate
table = tabulate(data, self.TABLE_HEADERS)
return table
```
This method is used to checking 'self.container'  dictionary whether there are empty values or not. If yes it will return text if not it will contnue to check the whether. there are invalid input or not from the submitted item name, quantity and price.If there are invalid input it will print invalid message else it will print a valid message.

Regardless the validity of the input, this method will return a table with tabulate module. The module require nested list, hence we need to transform the ``self.container`` because it is in a dictionary. The first step of transformation is to make a deepcopy of the ``self.container`` then we use the copy to find invalid or missing value in the container. If there is missing values or invalid values, then the progam will increase the count. Otherwise, it will add new value in the list which is the multiplication of the item quantity and its price.

The code will continue to get all the values in the ``copy_dictionary`` dictionary, then we insert the key from ``copy_dictionary`` to the list. Then, we use ``tabulate`` function from the ``tabulate`` module, the return value of this function is a string.

##### 8. ``total_price()``
Here is the code snippet for the method
```Python
# Checking whether the cart is empty or not
if len(self.container) == 0:
    return "You Have No Transaction, "\
            + "Please Add Item to Your Transaction"

# Calculating Total Amount
total = 0
for value in self.container.values():
    total += value[0]*value[1]

# Deciding discount value
if (total > self.HIGH_AMOUNT):
    print("CONGRATULATION, YOU GET 10% DISCOUNT!")
    total = total - (total*self.HIGH_DISCOUNT)
elif (total > self.MID_AMOUNT) and (total <= self.HIGH_AMOUNT):
    print("CONGRATULATION, YOU GET 8% DISCOUNT!")
    total = total - (total*self.MID_DISCOUNT)
elif (total >= self.LOWER_AMOUNT) and (total <= self.MID_AMOUNT):
    print("CONGRATULATION, YOU GET 5% DISCOUNT!")
    total = total - (total*self.LOWER_DISCOUNT)

# Create Message to be Shown
message = f"\nThe products you buy are: {self.container}\n"\
          + f"Your Total Amount of Purchase is {total}"
return message
```
This method, first, will check whether the container is empty or not. if yes it will return a warning text and the process is halted. This method is also used to calculate the amount of all transactions on the container.

If the amount reaches a certain value the amount will get discont and it will be calculated based on this rule:
1. If an amount is more than 500000, it will calculte the total amount with 10% discount.
2. If an amount is more than 300000 but less than or equal to 500000 it will calculate the total amount with 8% discount.
3. If an amount is more than 200000 but less than or equal to 300000 it will calculate the total amount with 5% discount.

### The ``script.py`` Script Explanation
The ``script.py`` is where the user would interact with the Transaction class. On this file we would like to import these modules:
```Python
import os
from cashier import Transaction
```
the Transaction class is from the cashier module we've created before. As for the ``os`` module, We will use two methods from it, which are:
* ``os.system()``: To send command to the system CLI
* ``os.name()``: To get the information of the operating system which the program will run

The ``os.name()`` method is important because the command of each system CLI will be different, hence, we need to define the type of the operating system.

#### The ``main()`` Function
Here is the code snippet:
```Python
transact = Transaction()

# Select Clear Command for the Command Line Interface based on the OS
# The clear command is used to clear the menu when user switching between menu  
clear_command = "cls" if os.name == "nt" else "clear"

# Main Menu For Our Program
transact = Transaction()

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
            add_new_item_menu(transact, clear_command)
        elif (choice == 2):
            modify_item_menu(transact, clear_command)
        elif (choice == 3):
            delete_item_menu(transact, clear_command)
        elif (choice == 4):
            reset_menu(transact)
        elif (choice == 5):
            message = transact.check_order()
            print(message)
        elif (choice == 6):
            message = transact.total_price()
            print(message)
        elif (choice == 7):
            exit()
        else:
            print(MENU_NOT_AVAILABLE_MSG)

        input("\nPress Enter to Continue\n")
        os.system(clear_command)
    except ValueError:
        print(SELECTION_NOT_INTEGER_MSG)
        os.system(clear_command)
```

Explanation:
* The ``Transaction`` is instantiated in the cart object, it will be called everytime the program is started.
* The ``clear_command`` is used to store clear command for specific operating system because we want to refresh the Command Line Interface (CLI) everytime the process on each menu is completed.
* The ``while`` loop is used to always show the main menu of the program.
* There are 7 menu that can be selected by users, if users enter number beyond 7 it will prompt warning. If users enter as string instead number (integer) it will raise exception and warning message is shown.
* When the user select menu number 1-4, it will call function that shows sub-menu, respectively.
* Menu number 5-6 will call ``Transaction.check_order()`` method and ``Transaction.total_price()`` method respectively.

#### ``add_new_item_menu(transaction_class, command)`` Function
By selecting number from the main menu, 1 the user we will call ``add_new_item()`` function:

````Python
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
transaction_class.add_item(
    item_name=item_name, 
    item_qty=item_qty, 
    item_price=item_price
)
````
The function requires 2 parameters:
* transaction_class: provide the Transaction class in this function
* command: The command to clear the program

The function, first, would clear the CLI then show a message to the user to input the item name. Then we prompt item qty and item price message, respectively. The the program will call the ``Transaction.add_item()`` method to store the values users have submitted.

#### ``modify_item_menu(transaction_class, command)`` Function
When this option is selected by user, the program would call ``modify_item_menu()`` function.
```Python
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
        item_name = input("Enter The Item Name: ")
        new_item_name = input("Enter The New Item Name: ")

        # Call Transation.update_item_name() method
        transaction_class.update_item_name(name=item_name, new_name=new_item_name)
    elif (choice == 2):
        # Prompt input the be submitted by user
        qty_item_name = input("Enter The Item Name: ")
        new_item_qty = input("Enter The New Quantity of the Item: ")

        # Call Transation.update_item_qty() method
        transaction_class.update_item_qty(name=qty_item_name, new_qty=new_item_qty)
    elif (choice == 3):
        # Prompt input the be submitted by user
        price_item_name = input("Enter The Item Name: ")
        new_item_price = input("Enter The New Price of the Item: ")
        
        # Call Transation.update_item_price() method
        transaction_class.update_item_price(name=price_item_name, new_price=new_item_price)
    elif (choice == 4):
        pass
    else:
        print(MENU_NOT_AVAILABLE_MSG)
except ValueError:
    print(SELECTION_NOT_INTEGER)
```
The function requires 2 parameters:
* transaction_class: provide the Transaction class in this function
* command: The command to clear the program

Code Explanation:
* First, the code would clear the CLI screen
* User can select 4 menu where the menu number 4 is to exit the program.
* When user select menu 1-3 the program would asked user to enter the values they wish to modify, then the program will call some methods from Transaction class:
    * ``Transaction.modify_item_name()`` will be called in the menu number 1.
    * ``Trsansaction.modify_item_qty()`` will be called in the menu number 2.
    * ``Transaction.modify_item_price()`` will be called in the menu number 3.

#### ``delete_item(transaction_class, command)`` Function
This function is triggered when user select menu number 3. Here is the code snippet:
```Python
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
except ValueError:
    print(SELECTION_NOT_INTEGER_MSG)
```
First, the ``os.system(command)`` will clear the CLI. Then it will show the menu and a prompt asking the user to enter the item name they wish to delete. Then the CLI screen will be cleared and the user will be asked whether they are sure to delete the desired item.

#### ``reset_menu()`` Function
This function is triggered when user select menu number 4. Here is the code snippet:
```Python
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
except ValueError:
    print(SELECTION_NOT_INTEGER_MSG)
```
The function will prompt question to the user whether they want to delete all items in the transaction. Choice 1 is to agree to delete while Choice 2 is to disagree to delete.

#### Test Case
There are few test cases that should be run in order to verify whether some of the requirements operate as expected. The test case is run within the ``test_cases.ipynb`` file.
##### 1. Test 1
This is test is to check whether the ``add_item()`` method is working as expeceted. Here is expected result:
[test case 1](img/test_cases/test_case1.JPG)
Here is the test result:
[test case 1 result](img/test_cases/test_case1_result.JPG)
As you can see the test result is as expected.

##### 2. Test 2
This is test is to check whether the ``delete_item()`` method is working as expeceted. Here is expected result:
[test case 2](img/test_cases/test_case2.JPG)
Here is the test result:
[test case 2 result](img/test_cases/test_case2_result.JPG)
As you can see the test result is as expected.

##### 3. Test 3
This is test is to check whether the ``reset_transaction()`` method is working as expeceted. Here is expected result:
[test case 3](img/test_cases/test_case3.JPG)
Here is the test result:
[test case 3 result](img/test_cases/test_case3_result.JPG)
As you can see the test result is as expected.
##### 4. Test 4
This is test is to check whether the ``total_price()`` method is working as expeceted. Here is expected result:
[test case 4](img/test_cases/test_case4.JPG)
Here is the test result:
[test case 4 result](img/test_cases/test_case4_result.JPG)
As you can see the test result is as expected.

#### Conclusion
From the workflow the application might look complex, however, the core application itself is simple enough to build except for the ``check_order()`` method where we need to make a deepcopy and transform dictionary into nested list so it can be transformed into a table.

##### Future works
Since, the core program is simple, we could use it in different application environment such as web application or mobile application. Then, we use database to collect the data that is submitted by user then use the data to provide visualization for the users.