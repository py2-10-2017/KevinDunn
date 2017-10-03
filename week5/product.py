

class Product(object):
    
    def __init__(self, price, item_name, weight, brand, cost, status='for sale'):
        if status is not 'for sale':
            self.status = status
        self.price = price 
        self.item_name = item_name 
        self.weight = weight 
        self.brand = brand 
        self.cost = cost 
        
    def sell(self):
        status = "sold"
        return self

    def addTax(self, item_tax):
        price = self.price * item_tax + self.price
        return self

    def itemReturn(self, reason):
        if reason == 'defective':
            self.status = "defective"
        if reason == 'defective':
            self.price = 0.0
            return self.price
        if reason == 'like new':
            self.status = "for sale"
            return self.status
        if reason == 'opened':
            self.status = "used"
        if reason == 'opened':
            discount = self.price * 0.20
            return discount

    def displayInfo(self): 
        print "_____Product INfo:_________"
        print "Item Name: {}".format(self.item_name)
        print "Brand: {}".format(self.brand)
        print "Price ${}".format(self.price)
        print "Weight: {}".format(self.weight)
        print "Status: {}".format(self.status)
        return self

item_1 = Product(0.89, "Can_o_Beans", "15.5oz", "S-mart", 0.45)
item_547 = Product(499.99, "hdtv", "24.5lbs", "S-mart", 300.99)

item_1.displayInfo()
item_547.displayInfo()
item_547.addTax(0.20).displayInfo()
item_547.sell().displayInfo()