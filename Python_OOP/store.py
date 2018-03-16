class Store(object):
    def __init__(self, location, owner):
        self.products = []
        self.location = location
        self.owner = owner

    def add_product(self, product_name, price, weight):
        self.products.append({
            "product_name": product_name,
            "price": price,
            "weight": weight
        })
        return self

    def remove_product(self, product_name):
        for product in self.products:
            if product['product_name'] == product_name:
                self.products.remove(product)
                return self
        
    def inventory(self):
        print "Store location: " + self.location 
        print "Owner: " + self.owner
        for product in self.products:
            print "Product: " + product['product_name'] +", Price: " + str(product['price']) + ", Weight: " + str(product['weight'])
        print "*"*10
        return self

Store1 = Store("111 Main St., Seattle, WA 98110", "Bob Loblaw")

Store1.add_product("speakers", 200, 10).add_product("tv", 600, 40). remove_product("tv")
Store1.inventory()