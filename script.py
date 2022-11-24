import pandas as pd



class Transaction:
    """
    A class to create transaction container object. Holding all of the Transaction 
    items, quantities and prices.  

    ...

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
    
    COLUMN_NAME_MAP : dictionary
        Manual mapping of column to be displayed in Pandas DataFrame.

    container : dict
        A dictionary to contain items that is stored in the transaction


    Methods
    -----------
    add_item(name, qty, price)
        Adding item to the container. When the exception is raised it will print message.
    
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
        Checking all of the item in the container, it will return in the form of table.

    total_price()
        Calculating total amount of the Transaction, and it will discount the amount -
        if a certain transaction amount is reached.
    """

    LOWER_AMOUNT = 200000
    LOWER_DISCOUNT = 0.05
    MID_AMOUNT = 300000
    MID_DISCOUNT = 0.08
    HIGH_AMOUNT = 500000
    HIGH_DISCOUNT = 0.1
    COLUMN_NAME_MAP = {
        "index": "Nama Item",
        0: "Jumlah Item", 
        1: "Harga/Item", 
        2: "Total Harga"
    }

    def __init__(self):
        """An object constructor, which is used to trigger dictionary creation -
        everytime this Class is instantiated.

        Parameter
        ----------
        No parameter required,
        """

        self.container = {}
 
    def add_item(self, item_name, item_qty, item_price):
        """Adding item to the Transaction container like name, -
        quantity(qty) and price of the item.
        
        Parameters
        ----------
        item_name : str (mandatory)
            The name of the item.
        
        item_qty : int (mandatory)
            The quantity of the item.

        item_price: int (mandatory)
            The price of the item
        
        Exception
        ---------
        ValueError
            If the object type from quantity and price is not what is expected.
            It will print invalid message.
        """

        try:
            self.container[item_name] = [int(item_qty), int(item_price)]
        except ValueError:
            print(f"\nAdding Item Failed, Quantity: {item_qty} and Price: {item_price} are Invalid Data")

    def update_item_name(self, item_name, new_item_name):
        """Updating the current item name to the new one.

        if the item is not in the self.container, it will print error message

        Parameters
        ----------
        item_name : str
            The name of the item we want to replace

        new_item_name : str
            The new item name to replace the existing item name.

        Exceptions
        ----------
        KeyError:
            If the the current name is not in the self.container dictionary. it will print error message.
        """

        try:
            self.container[new_item_name] = self.container.pop(item_name)
            print(f"\nCurrent Item Name: {item_name}, is successfully Updated to: {new_item_name}")
        except (KeyError):
            print(f"\nItem {item_name} is Not found, please enter the correct name")

    def update_item_qty(self, item_name, new_item_qty):
        """Updatig the quantity of a certain item.

        if the item is not in the self.container, it will print error message.

        Parameters
        ----------
        item_name : str
            The name of the item we want to replace

        new_item_qty : int
            The new quantity value to replace the existing quantity of a certain item.

        Exceptions
        ----------
        KeyError:
            If the the current item name is not in the self.container dictionary. it will print error message.
        
        ValueError:
            If the new qty (quantity) parameter is not in integer it will print error message.
        """

        try:
            self.container[item_name][0] = int(new_item_qty)
            print("\nUpdating Item Quantity is Successfull")
        except (KeyError):
            print(f"\nItem {item_name} is Not found, please enter the correct name")
        except (ValueError):
            print(f"\nNew Quantity Value: {new_item_qty} is Invalid") 

    def update_item_price(self, item_name, new_item_price):
        """Updatig the price of a certain item.

        if the item is not in the self.container, it will print error message.

        Parameters
        ----------
        name : str
            The name of the item we want to replace

        new_price : int
            The new quantity value to replace the existing price of a certain item.

        Exceptions
        ----------
        KeyError:
            If the the current name is not in the self.container dictionary. it will print error message.
        
        ValueError:
            If the qty (quantity) parameter is not in integer it will print error message.
        """

        try:
            self.container[item_name][1] = int(new_item_price)
            print("\nUpdating Item Price is Successfull")
        except KeyError:
            print(f"\nItem {item_name} is Not found, Please Enter The Correct Name")
        except ValueError:
            print(f"\nNew Price {new_item_price} Value is Invalid") 
        
    def delete_item(self, item_name):
        """Deleting a single item in the self.container dictionary

        If the item is not in the self.container dictionary, it will print error message.

        Parameters
        ----------
        item_name : str
            The name of the item that should be replaced.

        Exceptions
        ----------
        KeyError:
            If the name of the item is not in the self.container dictionary. it will print error message.
        """

        try:
            del self.container[item_name]
            print(f"\nItem {item_name} Has Been Deleted Successfully")
        except KeyError:
            print(f"\nItem {item_name} is Not found, Please Enter The Correct Name") 

    def reset_transaction(self):
        """Deleting all of the item in the self.container dictionary. 
        
        Deleting all items by assingning the self.container attribute with empty dictionary
        Parameters
        ----------
        No parameter is required
        
        """

        self.container = {}
        print("\nAll Transactions Have Been Deleted Successfully")

    def check_order(self):
        """Checking and verifying the self.container dictionary
        
        Checking 'self.container'  dictionary whether there are empty values or not.
        If yes it will return text if not it will contnue to check the whether 
        there are invalid input or not from the submitted item name, quantity and price.
        If there are invalid input it will print invalid message else it will print a valid message.
        Regardless the validity of the input, this method will print the self.container dictionary
        as Pandas DataFrame

        Parameters
        ----------
        No Parameter is required.
        """

        # Checking whether the cart is empty or not
        if len(self.container) == 0:
            return "You Have No Transaction, Please Add Item to Your Transaction"

        count = 0
        for key, value in self.container.items():
            if (key == "") or (value[0] == "") or (value[1] == "") \
                or (type(key) != str) or (type(value[0]) != int) \
                    or (type(value[1]) != int):
                count += 1
            else:
                amount = self.container[key][0]*self.container[key][1]
                self.container[key].append(amount)

        if count == 0:
            print("\nYour Input is Valid\n")
        elif count > 0:
            print("\nYour Input is Invalid\n")

        data = pd.DataFrame(self.container)
        data = data.transpose().reset_index().rename(columns=self.COLUMN_NAME_MAP)

        print(data.to_string(index=False))

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

        Parameters
        ----------
        No parameter is required
        """

        # Checking whether the cart is empty or not
        if len(self.container) == 0:
            return "You Have No Transaction, Please Add Item to Your Transaction"

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
        
        print("The products you buy are: ", self.container)
        print("Yourt Total Amount of Purchase is ", total)

if __name__ == "__main__":
    pass