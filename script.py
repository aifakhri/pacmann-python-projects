import pandas as pd





class Transaction:
    """
    This is the feature to add, update, delete and calculate user shopping cart
    """
    COLUMN_NAME = ["Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]
    LOWER_AMOUNT = 200_000
    LOWER_DISCOUNT = 0.05
    MID_AMOUNT = 300_000
    MID_DISCOUNT = 0.08
    HIGH_AMOUNT = 500_000
    HIGH_DISCOUNT = 0.1


    def __init__(self):
        self.cart = []
    
    def add_item(self, name: str, qty=0, price=0.0):
        self.items_info = {
            "name": name,
            "qty": qty,
            "price": price,
            "amount": price*qty
        }
        self.cart.append(self._items_info)

    def update_item_name(self, name: str, new_name: str):
        item_location = self.find_item(name)

        if (item_location != None):
            self.cart[item_location]["name"] = new_name
        else:
            print("Item Tidak Ditemukan, Mohon Cek Kembali Keranjang Anda")        

    def update_item_qty(self, name: str, new_qty: int):
        item_location = self.find_item(name)

        if (item_location != None):
            self.cart[item_location]["qty"] = new_qty
            self.cart[item_location]["amount"] = self.cart[item_location]["price"]*new_qty  
        else:
            print("Item Tidak Ditemukan, Mohon Cek Kembali Keranjang Anda")

    def update_item_price(self, name: str, new_price: float):
        item_location = self.find_item(name)

        if (item_location != None):
            self.cart[item_location]["price"] = new_price
            self.cart[item_location]["amount"] = self.cart[item_location]["price"]*new_price
        else:
            print("Item Tidak Ditemukan, Mohon Cek Kembali Keranjang Anda")
        

    def delete_item(self, name: str):
        item_location = self.find_item(name)

        if (item_location != None):
            self.cart = [i for i in self.cart if not i["name"] == name]
        else:
            print("Item Tidak Ditemukan, Mohon Cek Kembali Keranjang Anda")

    def reset_transaction(self):
        self.cart = []

    def check_order(self):
        if self.cart:
            return "Anda Tidak Memiliki Barang di Keranjang"
        
        count = 0
        for item in self.cart:
            if (item["name"] == "") or (item["qty"] == 0) or (item["price"] == 0.0):
                count += 1
            else:
                continue
        
        df = pd.DataFrame(self.cart)
        df.columns = self.COLUMN_NAME
        
        if (count == 0):     
            print("Pemesanan Sudah Sesuai")
        elif (count > 0):
            print("TERDAPAT KESALAHAN INPUT")
        
        print(df)
        

    def total_price(self):
        if self.cart:
            return "Anda Tidak Memiliki Barang di Keranjang"

        total = 0
        for elem in self.cart:
            total += elem["amount"]
        
        if (total > self.HIGH_AMOUNT):
            total = total - (total*self.HIGH_DISCOUNT)
            print("SELAMAT ANDA MENDAPATKAN DISKON 5%!, Total Belanja Anda Adalah: ", total)
        elif (total > self.MID_AMOUNT) and (total < self.HIGH_AMOUNT):
            total = total - (total*self.MID_DISCOUNT)
            print("SELAMAT ANDA MENDAPATKAN DISKON 8%!, Total Belanja Anda Adalah: ", total)
        elif (total > self.LOWER_AMOUNT) and (total < self.MID_AMOUNT):
            total = total - (total*self.LOWER_AMOUNT)
            print("SELAMAT ANDA MENDAPATKAN DISKON 10%!, Total Belanja Anda Adalah: ", total)
        else:
            print("Total Belanja Anda Adalah: ", total)

    # Additional Functions That Is Not on The Project Requirement

    def find_item(self, item_name):
        # print(item_name)
        for i, item in enumerate(self.cart):
            if item["name"] == item_name:
                return i

if __name__ == "__main__":
    test = Transaction()
    test.add_item("test", 1, 100_000)
    test.add_item("test2", 2, 2000)

    test.check_order()

    test.update_item_name("test3", "test10")
    test.update_item_price("test3", 1000)
    test.update_item_qty("test3", 10)
    # test.add_item("")
    test.check_order()
    test.total_price()