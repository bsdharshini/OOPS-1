#parent class
class Vehicle:
    current_year = 2022
    base_price = 10000
    def __init__(self,fuel,model):
        self.fuel =fuel
        self._model = model
    def _getValue(self):
        age = Vehicle.current_year - self._model
        print('Default Method')
        return Vehicle.base_price * (1/age)
class Car(Vehicle):
    def __init__(self,fuel,model,a_c,sunroof):
        super(Car,self).__init__(fuel,model)
        self.a_c =a_c
        self.sunroof =sunroof
    #method overriding
    def _getValue(self):
        Vehicle.base_price = 5000
        age = Vehicle.current_year - self._model
        print('Overridden child Method')
        return Vehicle.base_price * (1/age)

obj = Car('Petrol',2020,True,False)
print(obj.a_c)#True
print(obj._getValue()) # Overridden child Method # 2500
