class Laptop:
    storage_type = "SSD"
       
    @classmethod
    def getStorageType(cls):
        return cls.storage_type

    def __init__(self, RAM, Storage):
        self.RAM = RAM
        self.Storage = Storage


    def getInfo(self):
        print(f"Laptop Info: RAM: {self.RAM}, Storage: {self.Storage}, Storage Type: {self.storage_type}") 
        print("=====Instance method is accessing class attribute storage_type using self.storage_type====")

    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (price * discount / 100)
        print(f"Final price after {discount}% discount is: {final_price}")

l1 = Laptop("16GB", "512GB")
l1.calc_discount(10000, 10)    # Accessing static method using instance

print("-------Adding separator in amount--------")
l1.calc_discount(10_000, 10)  # Accessing static method using instance


