class Laptop:

    storage_type = "SSD"

    def __init__(self, RAM, Storage):
        self.RAM = RAM
        self.Storage = Storage


    def getInfo(self):
        print(f"Laptop Info: RAM: {self.RAM}, Storage: {self.Storage}, Storage Type: {self.storage_type}") 
        print("=====Instance method is accessing class attribute storage_type using self.storage_type====")       


l1 = Laptop("16GB", "512GB")
l1.getInfo()   