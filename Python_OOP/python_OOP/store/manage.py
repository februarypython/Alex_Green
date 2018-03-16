from store import Store
from product import Product

Store1 = Store("111 Main St, Seattle, WA", "Arya Stark")
Store2 = Store("222 West Ave, Brooklyn, NY", "Jamie Lannister")

prod1 = Product("TV", 700, 20)
prod2 = Product("SmartPhone", 250, 2)
prod3 = Product("Toaster", 45, 5)
   
def add_product(self):
    Store.products.append({
    "product_name": Product.name,
    "price": Product.price,
    "weight": Product.weight
    })
    return self

print Store1.add_product(prod1)

# Store1.add_product(prod1)

#     def remove_product(self, product_name):
#         for product in self.products:
#             if product['product_name'] == product_name:
#                 self.products.remove(product)
#                 return self
        
#     def inventory(self):
#         print "Store location: " + self.location 
#         print "Owner: " + self.owner
#         for product in self.products:
#             print "Product: " + product['product_name'] +", Price: " + str(product['price']) + ", Weight: " + str(product['weight'])
#         print "*"*10
#         return self