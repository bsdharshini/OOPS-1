# __init__ example
#class definition
class Calculate_Interest:
    def __init__(self, rate, time, amount):
        self.rate = rate
        self.time = time
        self.amount = amount
    # left side assigning to class - right side getting value from obj creation
    def calculate(self):
        return self.rate * self.time * self.amount    
obj1 = Calculate_Interest(2,1,1000)
print(obj1.rate)
print(obj1.calculate())
obj2 = Calculate_Interest(1.5,2,1000)
print(obj2.rate)
print(obj2.calculate())
        

