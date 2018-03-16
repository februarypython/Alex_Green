class Product(object):
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    
    def sell(self):
        self.status = "sold"
        return self
    
    def add_tax(self, tax):
        self.price += self.price * tax
        return self
    
    def returns(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
            return self
        elif reason == "new":
            self.status = "for sale"
            return self
        elif reason == "used":
            self.status = "used"
            self.price *= 0.8
            return self
    
    def display_info(self):
        print "$",self.price
        print self.name
        print self.status
        print self.weight, "pounds"
        print self.brand
        print "--------------"

headphones1 = Product(100, "headphones", 1, "sony")
dvdplayer = Product(200, "dvd player", 5, "Vizio")

headphones1.returns("used").add_tax(.11).sell().display_info()
dvdplayer.returns("new").add_tax(.17).display_info()