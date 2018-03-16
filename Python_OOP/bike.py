class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayinfo(self):
        print self.price, self.max_speed, self.miles
    
    
    def riding(self):
        print "Riding"
        self.miles += 10
        return self
    
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        return self

bike1 = Bike(400, "15mph")
bike2 = Bike(600, "20mph")
bike3 = Bike(200, "10mph")

bike1.riding().riding().riding().reverse().displayinfo()
bike2.riding().riding().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()

# What would you do to prevent the instance from having negative miles?
#     if miles is less than 0, set to 0

# Which methods can return self in order to allow chaining methods?
#     all of the methods returned self for chaining. I found that it wasn't necessary for displayinfo() though. I'm assuming because I didn't chain anything to it.