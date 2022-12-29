from copy import deepcopy
from tabulate import tabulate


class Transaction:
    """
    A class to create transaction container object.
    Holding all of the Transaction items, quantities and prices.


    Attributes:
    -----------
    LOWER_AMOUNT : int
        The minimum amount that is required by user to get 5% discount.

    LOWER_DISCOUNT: float
        The 5% discount value in floating point.

    MID_AMOUNT : int
        The minimum amount that is required by user to get 8% discount.

    MID_DISCOUNT : float
        The 8% discount value in floating point.

    HIGH_AMOUNT : int
        The minimum amount that is required by user to get 10% discount.

    HIGH_DISCOUNT : float
        The 10% discount value in floating point.

    TABLE_HEADERS : list
        The list of headers to be used in the tabulate table.

    container : dict
        A dictionary to contain items that is stored in the transaction


    Methods
    -----------
    add_item(name, qty, price)
        Adding item to the container. When the exception is raised
        it will print message.

    update_item_name(name, new_name)
        Replacing item name in the transaction container.

    update_item_qty(name, new_qty)
        Replacing item quantity of a particular item name.

    update_item_price(name, new_price)
        Replacing item price of a particular item name.

    delete_item(name)
        Deleting a single item in the Transaction container.

    reset_transaction()
        Deleting the entire item in the Transaction container.

    check_order()
        Checking all of the item in the container,
        it will return in the form of table.

    total_price()
        Calculating total amount of the Transaction,
        and it will discount the amount
        if a certain transaction amount is reached.
    """

    LOWER_AMOUNT = 200000
    LOWER_DISCOUNT = 0.05
    MID_AMOUNT = 300000
    MID_DISCOUNT = 0.08
    HIGH_AMOUNT = 500000
    HIGH_DISCOUNT = 0.1
    TABLE_HEADERS = [
        "Item Name", "Item Quantity", "Price/Item", "Total"
    ]

    def __init__(self):
        """An object constructor to trigger container dictionary creation

        The self.container attributes will be triggered everytime the Class
        is instantiated.
        """

        self.container = {}

    def add_item(self, item_name, item_qty, item_price):
        """Adding item to the Transaction container like name,
        quantity(qty) and price of the item.

        All parameters input are in string (due to the CLI script). Hence,
        the data type should be checked and transformed with these guidlines:
            1. item_name should always a string if not error message is raised
            2. item_qty should be an integer if not error message is raised.
            3. item_price should be an integer if not error message is raised.

        Parameters
        ----------
        item_name : str
            The name of the item.

        item_qty : str
            The quantity of the item.

        item_price: str
            The price of the item

        Returns
        -------
        str
            Success message (text/str) when the execption is not raised.
            Failed message when the par
        """

        try:
            # Type checkers for item_name input
            if item_name.isdigit() or self._is_float(item_name=item_name):
                message = "Item can't be added. Item Name is not string "\
                          +"Please enter the correct format."
            else:
                self.container[item_name] = [int(item_qty), int(item_price)]
                message = "Item is successfully Added"
        except (ValueError):
            message = "Item can't be added, Item Qty or Item Price "\
                      +"is not integer, Please enter the correct format."

        return message

    def update_item_name(self, item_name, new_item_name):
        """Updating the current item name to the new one.

        if the item is not in the self.container, it will print error message.
        And if the new_item_name is a float or integer it will print
        error message.

        Parameters
        ----------
        item_name : str
            The name of the item we want to replace

        new_item_name : str
            The new item name to replace the existing item name.

        Exceptions
        ----------
        KeyError:
            If the the current name is not in the self.container dictionary.
            it will print error message.

        Returns
        -------
        str
            Success message (text/str) when the execption is not raised.
            Failed message (text/str) when the execption is raised.
        """

        try:
            if new_item_name.isdigit() or \
                self._is_float(item_name=new_item_name):
                message = "Item can't be added. Item Name is not string "\
                          +"Please enter the correct format."
            else:
                self.container[new_item_name] = self.container.pop(item_name)
                message = f"\nCurrent Item Name: {item_name}, "\
                        + f"is Successfully Updated to: {new_item_name}"
        except (KeyError):
            message = f"\nItem {item_name} is Not found, "\
                      + "please enter the correct name"

        return message

    def update_item_qty(self, item_name, new_item_qty):
        """Updatig the quantity of a certain item.

        if the item is not in the self.container, it will print error message.

        Parameters
        ----------
        item_name : str
            The name of the item we want to replace

        new_item_qty : int
            The new quantity value to replace the existing quantity
            of a certain item.

        Exceptions
        ----------
        KeyError:
            If the the current item name is not in
            the self.container dictionary. it will print error message.

        ValueError:
            If the new qty (quantity) parameter is not in integer
            it will print error message.

        Returns
        -------
        str
            Success message (text/str) when the execption is not raised.
            Failed message (text/str) when the execption is raised.
        """

        try:
            self.container[item_name][0] = int(new_item_qty)
            message = "\nUpdating Item Quantity is Successfull"
        except (KeyError):
            message = f"\nItem {item_name} is Not found "\
                      + "please enter the correct name"
        except (ValueError):
            message = f"\nNew Quantity Value: {new_item_qty} is Invalid"

        return message

    def update_item_price(self, item_name, new_item_price):
        """Updatig the price of a certain item.

        if the item is not in the self.container, it will
        print error message.

        Parameters
        ----------
        name : str
            The name of the item we want to replace

        new_price : int
            The new quantity value to replace
            the existing price of a certain item.

        Exceptions
        ----------
        KeyError:
            If the the current name is not in the self.container dictionary.
            it will print error message.

        ValueError:
            If the qty (quantity) parameter is not in integer
            it will print error message.

        Returns
        -------
        str
            Success message (text/str) when the execption is not raised.
            Failed message (text/str) when the execption is raised
        """

        try:
            self.container[item_name][1] = int(new_item_price)
            message = "\nUpdating Item Price is Successfull"
        except KeyError:
            message = f"\nItem {item_name} is Not found, "\
                      + "Please Enter The Correct Name"
        except ValueError:
            message = f"\nNew Price {new_item_price} Value is Invalid"

        return message

    def delete_item(self, item_name):
        """Deleting a single item in the self.container dictionary

        If the item is not in the self.container dictionary,
        it will print error message.

        Parameters
        ----------
        item_name : str
            The name of the item that should be replaced.

        Exceptions
        ----------
        KeyError:
            If the name of the item is not in the
            self.container dictionary. it will print error message.

        Returns
        -------
        str
            Success message (text/str) when the execption is not raised.
            Failed message (text/str) when the execption is raised
        """

        try:
            del self.container[item_name]
            message = f"\nItem {item_name} Has Been Deleted Successfully"
        except KeyError:
            message = f"\nItem {item_name} is Not found, "\
                      + "Please Enter The Correct Name"

        return message

    def reset_transaction(self):
        """Deleting all of the item in the self.container dictionary.

        Deleting all items by assingning the self.container attribute
        with empty dictionary

        Returns
        -------
        str
            Success message
        """

        self.container = {}
        message = "All Transactions Have Been Deleted Successfully"
        return message

    def check_order(self):
        """Checking and verifying the self.container dictionary

        Checking 'self.container'  dictionary whether there are empty
        values or not. If yes it will return text if not it will
        contnue to check the whether there are invalid input or not
        from the submitted item name, quantity and price. If there
        are invalid input it will print invalid message else
        it will print a valid message.

        Regardless the validity of the input, this method will
        print the self.container dictionary as Pandas DataFrame

        Returns
        -------
        str
            Total mount message if the container is not empty.
            If the container is empty it will return notification message
        """

        # Checking whether the cart is empty or not
        if len(self.container) == 0:
            message = "You Have No Transaction, " \
                      + "Please Add Item to Your Transaction"
            return message

        # Make a Deep Copy for the self.container to maintain data integrity
        container_copy = deepcopy(self.container)

        # Finding Missing Value the self.container
        count = 0
        for key, value in container_copy.items():
            if (key == "") or (value[0] == "") or (value[1] == ""):
                count += 1
            else:
                amount = int(container_copy[key][0]) \
                            * int(container_copy[key][1])
                container_copy[key].append(amount)

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

    def total_price(self):
        """Calculate the amount of all transactions on the container.

        Discount will be calculated based on this rule:
        1. If an amount is more than 500000,
           it will calculte the total amount with 10% discount

        2. If an amount is more than 300000 but less than or equal to 500000 \
           it will calculate the total amount with 8% discount

        3. If an amount is more than 200000 but less than or equal to 300000  \
           it will calculate the total amount with 5% discount

        This method, first, will check whether the container is empty or not.
        if yes it will return a warning text.

        Exception
        ---------
        TypeError:
            If there are invalid amount during total price calculation
            The program will return a message

        Returns
        -------
        str
            Total mount message if the container is not empty.
            If the container is empty it will return notification message
        """

        # Checking whether the cart is empty or not
        if len(self.container) == 0:
            return "You Have No Transaction, "\
                   + "Please Add Item to Your Transaction"

        # Calculating Total Amount
        total = 0
        for value in self.container.values():
            total += (value[0])*(value[1])

        # Deciding discount value
        if (total > self.HIGH_AMOUNT):
            print("CONGRATULATION, YOU GET 10% DISCOUNT!")
            total = total - (total*self.HIGH_DISCOUNT)
        elif (total > self.MID_AMOUNT) and (total <= self.HIGH_AMOUNT):
            print("CONGRATULATION, YOU GET 8% DISCOUNT!")
            total = total - (total*self.MID_DISCOUNT)
        elif (total > self.LOWER_AMOUNT) and (total <= self.MID_AMOUNT):
            print("CONGRATULATION, YOU GET 5% DISCOUNT!")
            total = total - (total*self.LOWER_DISCOUNT)

        # Create Message to be Shown
        message = f"\nThe products you buy are: {self.container}\n"\
                  + f"Your Total Amount of Purchase is {total}"
        return message

    def _is_float(self, item_name):
        """Checking whether an item_name is a float or not

        Parameters:
        -----------
        Item_name: str
            Name of the item

        Exceptions:
        -----------
        ValueError:
            Will be triggered if the item_name cannot be transformed
            into a float.

        Return:
        -------
        boolean:
            True if the string is a float, False otherwise
        """
        try:
            float(item_name)
            return True
        except (ValueError):
            return False

if __name__ == "__main__":
    pass
