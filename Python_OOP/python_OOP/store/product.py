class Product(object):
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

if __name__ == "__main__":
    prod1 = Product("TV", 700, 20)
    prod2 = Product("SmartPhone", 250, 2)
    prod3 = Product("Toaster", 45, 5)
    prod4 = Product("E-reader", 85, 1)
    prod5 = Product("Washing Machine", 500, 75)
