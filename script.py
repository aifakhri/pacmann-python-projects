import pandas as pd



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
    COLUMN_NAME_MAP = {
        "index": "Nama Item",
        0: "Jumlah Item", 
        1: "Harga/Item", 
        2: "Total Harga"
    }

    def __init__(self):
        self.cart = {}
 
    def add_item(self, name, qty, price):
        try:
            self.cart[name] = [int(qty), int(price)]
        except ValueError:
            print("Adding Item Failed, Quantity and Price are Invalid")

    def update_item_name(self, name, new_name):
        if (type(name) == str) and (type(new_name) == str):
            try:
                self.cart[new_name] = self.cart.pop(name)
            except (KeyError):
                print("Item Not found, please enter the correct name")
        else:
            print("Item Name is Not String, Please Enter the Correct Value")     

    def update_item_qty(self, name, new_qty):
        try:
            self.cart[name][0] = int(new_qty)
        except KeyError:
            print("Item Not found, please enter the correct name")
        except ValueError:
            print("New Quantity Value is Invalid") 

    def update_item_price(self, name: str, new_price: float):
        try:
            self.cart[name][1] = int(new_price)
        except KeyError:
            print("Item Not found, please enter the correct name")
        except ValueError:
            print("New Price Value is Invalid") 
        
    def delete_item(self, name: str):
        try:
            del self.cart[name]
        except (KeyError, ValueError):
            print("Item Not found, please enter the correct name") 

    def reset_transaction(self):
        self.cart = {}

    def check_order(self):
        # if self.cart:
        #     return "Your transaction is empty"
        
        count = 0
        for key, value in self.cart.items():
            if (key == "") or (value[0] == "") or (value[1] == "") \
                or (type(key) != str) or (type(value[0]) != int) \
                    or (type(value[1]) != int):
                count += 1
            else:
                    amount = self.cart[key][0]*self.cart[key][0]
                    self.cart[key].append(amount)


        if count == 0:
            print("Your Input is Correct")
        elif count > 0:
            print("There are Incorrect Input, Please Update The Value")

        data = pd.DataFrame(self.cart)
        data = data.transpose().reset_index().rename(columns=self.COLUMN_NAME_MAP)

        print(data)

    def total_price(self):
        if self.cart:
            return "Anda Tidak Memiliki Barang di Keranjang"


        total = 0
        for value in self.cashier.values():
            total += value[0]*value[1]
        
        if (total > self.HIGH_AMOUNT):
            total = total - (total*self.HIGH_DISCOUNT)
            print("CONGRATULATION, YOU GET 5% DISCOUNT!")
        elif (total > self.MID_AMOUNT) and (total < self.HIGH_AMOUNT):
            total = total - (total*self.MID_DISCOUNT)
            print("CONGRATULATION, YOU GET 8% DISCOUNT!")
        elif (total > self.LOWER_AMOUNT) and (total < self.MID_AMOUNT):
            total = total - (total*self.LOWER_AMOUNT)
            print("CONGRATULATION, YOU GET 10% DISCOUNT!:")
        
        print("The products you buy are: ", self.cart)
        print("Yourt Total Amount of Purchase is ", total)

    # Additional Functions That Is Not on The Project Requirement

    def display_item(self):
        print("You have ordered this items ", self.cart)

if __name__ == "__main__":
    test = Transaction()
    test.add_item("Ayam", 1, 20_000)
    test.add_item("Ikan", 5, 10_000)
    test.add_item("Delete", 1, 20_000)
    test.display_item()
    test.update_item_name("Ayam", "Daging")
    test.display_item()
    test.update_item_name("Ikang", "Fauzi")
    test.update_item_price("Daging", 50_000)
    test.display_item()
    test.update_item_price("Dagang", 70_000)
    test.update_item_qty("Ikan", 17)
    test.display_item()
    test.update_item_qty("Mobil", 18)
    test.delete_item("delete")
    test.display_item()
    test.delete_item("Delete")
    test.check_order()    
