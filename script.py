class Transaction:

    def __init__(self):
        self._chart = []

    def add_item(self, name, qty, price):
        self._items_info = {
            "name": name,
            "qty": qty,
            "price": price,
            "amount": price*qty
        }
        self._chart.append(self._items_info)

    def update_item_name(self, name, newName):
        for i in self._chart:
            pass

    def update_item_qty(self, qty, newQty):
        pass

    def update_item_price(self, price, newPrice):
        pass

    def delete_item(self, name):
        self.name = ""

    def reset_transaction(self):
        self.chart = {}

    def check_order(self):
        print(self._chart)

    def total_price(self):
        pass

    def _search_chart(self):
        pass

if __name__ == "__main__":
    test = Transaction()
    test.add_item("test", 1, 10)
    test.add_item("test2", 2, 10)
    test.add_item("test3", 3, 10)
    test.add_item("test4", 4, 10)
    test.check_order()