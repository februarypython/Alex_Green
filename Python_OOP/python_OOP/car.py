# Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. 
# If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

# Create six different instances of the class Car. In the class have a method called display_all() that returns all the information 
# about the car as a string. In your __init__(), call this display_all() method to display information about the car once the 
# attributes have been defined.

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.displayall()
    
    def displayall(self):
        print "Price:", self.price
        print "Speed:", self.speed, "mph"
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage, "mpg"
        if self.price > 10000:
            print "Tax: 0.15"
        else:
            print "Tax: 0.12"
        print "---------------"

car1 = Car(11000, 100, "full", 25)
car2 = Car(8000, 75, "empty", 15)
car3 = Car(14000, 85, "mostly full", 7000)
car4 = Car(200, 25, "none", 8)
car5 = Car(55000, 200, "full", 15)
car6 = Car(6500, 112, "mostly empty", 28)
