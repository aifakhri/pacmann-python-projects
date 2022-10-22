class Transaction:

    def __init__(self):
        self._cart = []

    def add_item(self, name: str, qty: int, price: float):
        self._items_info = {
            "name": name,
            "qty": qty,
            "price": price,
            "amount": price*qty
        }
        self._cart.append(self._items_info)

    def update_item_name(self, name: str, newName: str):
        for key in self._cart:
            if key["name"] == name:
                key["name"] = newName

    def update_item_qty(self, name: str, newQty: int):
        for key in self._cart:
            if key["name"] == name:
                key["qty"] = newQty
                key["amount"] = key["price"]*newQty

    def update_item_price(self, name: str, newPrice: float):
        for key in self._cart:
            if key["name"] == name:
                key["price"] = newPrice
                key["amount"] = key["qty"]*newPrice

    def delete_item(self, name: str):
        self._cart = [i for i in self._cart if not i["name"] == name]

    def reset_transaction(self):
        self._cart = []

    def check_order(self):
        print(self._cart)

    def total_price(self):
        pass

    def _modify_chart(self, field, oldEntry, newEntry):
        pass
                

if __name__ == "__main__":
    test = Transaction()
    test.add_item("test", 1, 10)
    test.add_item("test2", 2, 20)
    test.add_item("test3", 3, 30)
    test.add_item("test4", 4, 40)
    # test.check_order()
    # print("Test modify chart")
    test.update_item_name("test2", "testUpdate")
    test.update_item_qty("test3", 100 )
    test.update_item_price("test4", 1000)
    # test.check_order()
    print("Test Delete")
    test.delete_item("test")
    test.check_order()
    test.reset_transaction()
    test.check_order()