
class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed 
        self.fuel = fuel 
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def display_all(self):
        print "____ Car Info: ________"
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax
        return self

car_a = Car("35000", "130mph", "Full", "32mpg")
car_b = Car("22000", "120mph", "kind of Full", "29mpg")
car_c = Car("8000", "100mph", "Not Full", "27mpg")
car_d = Car("12000", "110mph", "kind of Full", "30mpg")
car_e = Car("2000", "60mph", "Empty", "18mpg")
car_f = Car("19000", "120mph", "Full", "25mpg")

car_a.display_all()
car_b.display_all()
car_c.display_all()
car_d.display_all()
car_e.display_all()
car_f.display_all()

