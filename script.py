class Transaction:
    """
    This is the feature to add, update, delete and calculate user shopping cart
    """
    LOWER_AMOUNT = 200_000
    LOWER_DISCOUNT = 0.05
    MID_AMOUNT = 300_000
    MID_DISCOUNT = 0.08
    HIGH_AMOUNT = 500_000
    HIGH_DISCOUNT = 0.1


    def __init__(self):
        """
        Instance Attributes to store item information that is submitted by user
        """
        self._cart = []

    def add_item(self, name: str, qty: int, price: float):
        """
        Method that is used to store the details of information
        of the item that is submitted by user into user cart.
        """
        self._items_info = {
            "name": name,
            "qty": qty,
            "price": price,
            "amount": price*qty
        }
        self._cart.append(self._items_info)

    def update_item_name(self, name: str, newName: str):
        """
        Method that is used to update item name in the current cart.
        """
        for key in self._cart:
            if key["name"] == name:
                key["name"] = newName

    def update_item_qty(self, name: str, newQty: int):
        """
        Method that is used to update item quantity in the current cart.
        Each update would also update the amount.
        """
        for key in self._cart:
            if key["name"] == name:
                key["qty"] = newQty
                key["amount"] = key["price"]*newQty

    def update_item_price(self, name: str, newPrice: float):
        """
        Method that is used to update item price in the current cart.
        Each update would also update the amount.
        """
        for key in self._cart:
            if key["name"] == name:
                key["price"] = newPrice
                key["amount"] = key["qty"]*newPrice

    def delete_item(self, name: str):
        """
        Method that is used to delete one item from the cart.
        """
        self._cart = [i for i in self._cart if not i["name"] == name]

    def reset_transaction(self):
        """
        Method for delete the entire item on the cart.
        """
        self._cart = []

    def check_order(self):
        """
        Method to validate the entry of the cart. And also shows the user
        the information about the current cart. 
        """
        header = "| No | Name Item | Harga/Item | Total Harga |\n"
        for i, elem in enumerate(self._cart, start=1):
            if (elem["name"] == "") or (elem["qty"] == "") or (elem["price"] == ""):
                print("Invalid Input Data")
                exit()
            else:
                content = f"| {i} | {elem['name']} | {elem['qty']} | {elem['price']}, | {elem['amount']} |\n"
                header += content
        print(header)

    def total_price(self):
        """
        Calculate the total amount of the item price in the cart.
        This method also calculcate the discount if the total amount reaches
        a certain number
        """
        total = 0
        for elem in self._cart:
            total += elem["amount"]

        print("Total amount of your shopping cart is ", total)
        
        if (total > self.HIGH_AMOUNT):
            total = total - (total*self.HIGH_DISCOUNT)
            print("Congratulation You Get a discount, your total shopping amount is ", total)
        elif (total > self.MID_AMOUNT) and (total < self.HIGH_AMOUNT):
            total = total - (total*self.MID_DISCOUNT)
            print("Congratulation You Get a discount, your total shopping amount is ", total)
        elif (total > self.LOWER_AMOUNT) and (total < self.MID_AMOUNT):
            total = total - (total*self.LOWER_AMOUNT)
            print("Congratulation You Get a discount, your total shopping amount is ", total)
        
### Another things to do: Add data validation on total_price() method.
                

if __name__ == "__main__":
    test = Transaction()
    test.add_item("test", 1, 100_000)
    test.add_item("test2", 2, 2000)
    test.add_item("test3", 3, 3000)
    test.add_item("test4", 4, 4000)
    test.check_order()
    test.total_price()
    # print("Test modify chart")
    # test.update_item_name("test2", "testUpdate")
    # test.update_item_qty("test3", 100 )
    # test.update_item_price("test4", 1000)
    # test.check_order()
    # print("Test Delete")
    # test.delete_item("test")
    # test.check_order()
    # test.reset_transaction()
    # test.check_order()