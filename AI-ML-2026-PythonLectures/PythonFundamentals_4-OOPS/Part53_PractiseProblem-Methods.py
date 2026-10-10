# Product store
# Design & create an online store for Products (name, price).
# Track total products being created.
# Create a static method to calculate discount on each product based on a % parameter.


class Product:

    count = 0

    def __init__(self, name , price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"Product Name: {self.name}, Price: {self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total products created: {cls.count}")

    @staticmethod
    def calculate_discount(price, discount_percent):
        discount_amount = price * (discount_percent / 100)
        discounted_price = price - discount_amount
        print(f"Original Price: {price}, Discounted Price: {discounted_price}")   


p1 = Product("Laptop", 1000)
p2 = Product("Mobile", 500)

p1.get_info()
p2.get_info()

print("--------Calculating count of Products :-------------")
Product.get_count()  

print("--------Calculating discount for Laptop :-------------")
p1.calculate_discount(p1.price, 10)  # 10% discount
p1.calculate_discount(20_000, 10)  # 10% discount