#object._classname__variable or method name
class One:
    def __init__(self,name,age):
        self.__name =name
        self.age =age
    def __getDetail(self):
        return self.__name,self.age
s = One('Dhar',20)
print(s._One__name)
print(s._One__getDetail())
print(s.name)#error
print(s.__name)#error

