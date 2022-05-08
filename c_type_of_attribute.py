class ExpenseTracker:
    #class attribute
    version = '1.1.0'
    def __init__(self,amount,credit):
        # instance attribute
        self.amount = amount
        self.credit = credit
obj = ExpenseTracker(1000, 10)
print(obj.version) #returns class attr value
print(obj.__dict__) #return instance attr value only
obj2= ExpenseTracker(2000,1)
print(obj2.version) # returns same class attr value
print(obj2.__dict__)

# Note: Using object if we change class attr value then only that instance/obj will change. 
# Other object remain same. So change in definition itself

obj.version = '1.1.1'
print(obj.version) # 1.1.0
print(obj2.version) #1.1.1

