# Pacmann Python Projects - Super Cashier

## Introduction
### Project Background
An Online Supermarket wants to add a new feature to their application to help their customer adding, modifying and deleting the items, the quantity of the items, the price of the items that the customer wants to buy. The desired feature is also required to provide calculation of the amount of bought items along with the total purchase of all of the items. For the total purchase the Online Supermarket will always provide discount for the total purchase that reaches a certain value.

### Project Objectives and Requirement
From the background above we would provide a solution called **cart** feature. However, Before the feature is created and intregared to the existing app, we will create a mock up application of this feature with Python script. 

This mock up is a Command Line Interace application, it will have the same requorements as the feature that want to be added. The requitements are:
- Adding item name, item quantity and item price to the cart. The addition will also created a total amount or a total price of this item, which can be calculated by multipying the quantity of the item with the price.
- Update item name on the cart.
- Update item quantity of a certain item.
- Update item price of a certain item.
- Delete a single item.
- Reset the entire cart.
- Check the cart, whether there is an empty cart or invalid value inside the cart.
- Calculate the total purchase of the entire cart. If the the purchase reaches a certain limit, the purchase would be discounted.
- The discount requitements are:
1. if the total price of the purchase is greater than Rp. 500,000 the discount is 10%
2. if the total price of the purchase is greater than Rp. 300,000 the discount is 8%
3. if the total price of the purchase is greater than Rp. 500,000 the discount is 5%

All of these requirements would be created as methods in a class called `Transaction` so it can be reusable.


### Flow Chart
Will be loaded later

## Code Explanation
### The script.py Function
In this Python script we will store the Transaction class. As we mentioned before, the Transaction class holds all the requirement of our program. The name of the methods can be viewed in the Objective and Requirement section.

First, we have various class variable or class instance. These are the constant that we will use on our class:

The variable contains underscore which indicates that this instance shouldn't be called outside the class. And here are the explanation of the variables:
* The column_name variable is used as a constant to replace the column in the cart table.
* The rest of the variables are the number of discount and the threshold of which discount is given. 
 

Next, in our class we have an object constructor with no argument:
The purpose of this constructor is to instantiate the ``self.cart`` attribute everytime the class is instantiated. This attribute is a list, and it will be populated with Item Name, Item Qty, Item Price and Item Amount from the ``add_item()`` method.

Here are the methods in our class:
#### 1. ``add_item()``
Here is the code snippet for the method

The function requires 3 arguments, which will be stored in the variable ``self.items_info`` as a dictionary the dictionary. Here are the arguments:
* item_name is for the name of the item
* qty is for the quantity of the item
* price is for the price of the item

After the data is stored in the dictionary it will be appended in the ``self.cart``. With this every time a user added new item it will be stored in the ``self.cart`` attribute.

We provide default value if somehow the user forget to enter the option that is needed. Also, we setup try-except statement to anticipate 

#### 2. ``update_item_name()``
Here is the code snippet for the method


The method requires 2 arguments:
* item_name is for the name of the item we want to replace
* item_name is for the new name of the item

This function works by finding the item on the ``self.cart`` by using another method called ``find_item()``. We use this method because every time we want to update something in our cart, we need to make sure the item we want to modify is in the cart. The find item will return the index in the cart and if there is no match it will return ``None``. These return values are assigned to the ``item_location`` variable.

We could use this return value to create a simple decision where if the ``item_location`` is None, we will print a notification message else we will update the new item name

#### 3. ``update_item_qty()``
Here is the code snippet for the method

The method requires 2 arguments:
* item_name is for the name of the item for the item quantity we want to replace.
* item_name is for the new item quantity we want to insert as new price.

Just like ``update_item_name()``. this method will use ``find_item()`` to find item on the cart, and use the return value (which is stored in the ``item_location`` variable) to make decision whether the quantity is updated or not. 

#### 4. ``update_item_price()``
Here is the code snippet for the method

The method requires 2 arguments:
* item_name is for the name of the item for the item price we want to replace.
* item_name is for the new item price we want to insert as new price.

Just like ``update_item_name()``. this method will use ``find_item()`` to find item on the cart, and use the return value (which is stored in the ``item_location`` variable) to make decision whether the price is updated or not. 


#### 5. ``delete_item()``
Here is the code snippet for the method

The method requires 1 arguments:
* ``item_name`` is for the name of the item for the item price we want to delete.

First, we will use ``find_item()`` function to find whether the item is in the cart or not. Then we use the return value to make decision whether the item should be deleted or not.


#### 6. ``reset_transaction()``
Here is the code snippet for the method

The method requires no argument. To reset the cart we just assign an empty list to the ``self.cart``  attribute because, the cart is stored as a list.

#### 7. ``check_order()``
Here is the code snippet for the method

The method requires no argument. The code will not return any information if the ``self.cart`` is empty. Otherwise, we would loop through the cart and check whether there is an empty or 0 value in the columns. If there is any, we still return the table and add message "Terdapat kesalahan input di kerjanang". Else, we would return otherwise.

We use Pandas' DataFrame to create table to make us easier to create a table in a CLI. Also, we would replace the name of the columns, which based on the keys in the ``self.item_info`` dictionary. The replacement just to make the table prettier. 
#### 8. ``total_price()``
Here is the code snippet for the method

This method requires no argument. First, the code will try to find whether the cart is empty. If yes, then we will notify the user with message. If not, we start calculte the total proce of our purchase by looping through the cart and add each total amount.

Then, we would provide discount if the total price of the purchase have reached a certain amount as per our requirement above.
Here is the code snippet for the method

This method requires 1 argument:
* ``item_name`` is for the name of the item for the item price we want to find in the cart.

First, we loop through the ``self.cart`` with enumerate, because what we want to get is the index in which the item name resides. Hence, when the name is matched then, the program would return the index. Otherwise, it would return None.

### The main.py Script Explanation
The ``main.py`` is the main program where the user can interact with the main menu. These menus are stored in the ``main()`` function. Some of the menus would have individual function for readibility purpose.

#### The ``main()`` Function

(( Code Snippet with Picture ))

Explanation:
* The ``Transaction`` is instantiated in the cart object, it will be called everytime the program is started.
* The ``clear_command`` is used to store clear command for specific operating system because we want to refresh the Command Line Interface (CLI) everytime the process on each menu is completed.
* The ``while`` loop is used to always show the main menu of the program. It will end when we select "Keluar Dari Program" menu, which is for exiting the program.
* The ``print()`` function is used to display the menu
* ``choice`` variable would store the user input as an integer, hence, if user enter any kind of string it will be captured by the ``expect`` statement because we expect a ``ValueEror`` error type.
* For choice number 1, 2, 3 and 4, we have created a new function for code readability purpose, respectively.
* For choice number 5, the user is going to check the cart status by calling the ``check_order()`` method from ``Transaction`` clas.
* For choice number 6, the user is going to check the total price of their purchase by calling the ``total_price()``. 
We expect the user to select the menu with numbers, hence we wrap the ``input`` function in the ``int`` function which transform any user input into integer. If user enter string or text we capture the error with try-except statement to notify the user.
* If the user enter any number outside the menu we would also notify the user.

From this view, user free to interact with the application by selecting the menu's number. If a user enter a value beyond the menu it will print a notification.


#### ``add_new_item_menu()`` Function
By selecting number from the main menu, 1 the user we will call ``add_new_item()`` function:

--Code Snippet--

The function, first, would clear the CLI then show a message to the user to input the item name. Then we prompt item qty and item price message, respectively.

#### ``modify_item_menu()`` Function
When this option is selected by user, the program would call ``modify_item_menu()`` function. 


The function would clear the current CLI terminal and then shows the new menu called "Modifikasi Item Di Keranjang" with following menu
1. Modifikasi Nama Barang di Keranjang
2. Modifikasi Jumlah Barang di Keranjang
3. Modifikasi Harga Barang di Keranjang
4. Kembali ke Menu Utama

The menu number 4 is to go back to the main menu. The other menu would prompt a message depending the menu

##### Selecting Menu Number 1
This menu is used to change item name on the cart. When the menu is selected the program would prompt a message for the user to enter item name they want to change. Then the program would prompt a message for the desired item name to be submitted.

After the user finished entering the data, the program would call the ``update_item_name()`` method with the ``item_name`` and ``new_item_name`` as the parameter.

When the process is done, the CLI display will be cleared and the display will change to the main menu display.

##### Selecting Menu Number 2
This menu is used to change item price on the cart. When the menu is selected the program would prompt a message for the user to enter item name of the item quantity they want to change. Then the program would prompt a message for the desired item quantity to be submitted.

After the user finished entering the data, the program would call the ``update_item_wty()`` method with the ``qty_item_name`` and ``new_item_qty`` as the parameter.

When the process is done, the CLI display will be cleared and the display will change to the main menu display.

##### Selecting Menu Number 3
This menu is used to change item price on the cart. When the menu is selected the program would prompt a message for the user to enter item name of the item price they want to change. Then the program would prompt a message for the desired item price to be submitted.

After the user finished entering the data, the program would call the ``update_item_price()`` method with the ``item_name`` and ``new_item_price`` as the parameter.

When the process is done, the CLI display will be cleared and the display will change to the main menu display.

#### Selecting Number 4 - Hapus Item di Keranjang
By selecting menu number 3, the program will call ``delete_item_menu()``, which contains this code:

The code will reset clear the main menu display and showing new menu. The user is prompted with the message to enter the item name they want to delete. After that the program will call ``delete_item()`` method from Transaction class.

#### Selecting Number 5 - Reset Keranjang
By selecting this menu, the program will call ``reset_cart_menu()``, which contains this code:

The code will reset clear the main menu display and showing new menu. The user is prompted with a choice whether they want to reset the current cartt. If they select number 1 user will After that the program will call ``delete_item()`` method from Transaction class. if they select number 2, reset is cancelled and the current menu is cleared and main menu is shown.

The user can opt out by selectint the number 3 menu. There is also try-expect statement to make sure the program will not error when the user enter a string to the program

## Test

## Conclusion

