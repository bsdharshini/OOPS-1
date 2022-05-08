class ExpenseTracker:
    def __init__(self,caterory,balance,credit):
        self.caterory = caterory
        self.balance = balance
        self.credit = credit
    @staticmethod
    def convert_float(amount):
        return float(amount)

    @classmethod
    def get_attr_from_str(cls,total_value:str):
        caterory,balance,credit = total_value.split(' ')
        return cls(caterory, cls.convert_float(balance),cls.convert_float(credit))
obj = ExpenseTracker.get_attr_from_str('Travel 5000 100')
print(obj.balance)
print(obj.__dict__)


