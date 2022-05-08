# 1
class Student:
    name = 'dhar'
    age = 20
s1 =Student()
s2=Student()
print(s1.name,end = " ")
print(s2.name,end = " ") #o/p: dhar dhar

#2
class Student:
    p =50
s1 = Student()
s2 = Student()
s1.p =40
s2.p =60 
print(s1.p) # 40

#3
class Student:
    name = 'dhar'
    def store_detail(self):
        self.age = 20
    def print_detail(self):
        print(self.name,end=" ")
        print(self.age)
s = Student()
s.store_detail() # without this call age will not be set. So error will be thrown
s.print_detail() # dhar 20

#4
class Student:
    def store_detail(self):
        self.age = 20
    def print_detail(self):
        print(self.name,end=" ")
        print(self.age)
s = Student()
s.store_detail()
s1=Student()
s1.print_detail() # throws error. Because self.age is only accessble by s not by s1

# 5
class S:
    def __init__(self,name,age):
        self.name = 'dha'
        self.age = 20
    def print_detail(self):
        print(self.name)
        print(self.age)
s= S()
s.print_detail() # error.Because Student pass need 2 parameter to pass

#6
class S:
    def __init__(self,name,age):
        self.name = 'dha'
        self.age = 20
    def print_detail():
        print(self.name)
        print(self.age)
s= S('a'2)
s.print_detail()#Error. Because print_detail has no self

#7
class S:
    def __init__(self,name,age):
        self.__name = name
        self.age = age
    def getdetail(self):
        return(self.__name,self.age)
s =S('Dhar',20)
print(s.getdetail())#('Dhar',20)

    