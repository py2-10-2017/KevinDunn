class MathDojo(object):
    def __init__(self, total=0):
        self.total = total
    def add(self, *args):
        for arg in args:
            if type(arg) is list or type(arg) is tuple:
                for num in arg:
                    self.total += num
            else: 
                self.total += arg
        # print self.total
        return self

    def subtract(self, *args):
        amount = 0
        for arg in args:
            if type(arg) is list or type(arg) is tuple:
                for num in arg:
                    amount += num
            else:
                amount += arg
        
        self.total -= amount
        # print self.total
        return self

    def result(self):
        print self.total


md = MathDojo()
# \/ results showing on #1
md.add(2).add(2,5).subtract(3,2).result()
# \/ rusults not showing on #2, even though the numbers are still adding and subtracting?
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result 
