#eg: 1
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    def print_detail(self):
        print(self.name, ' ', self.age)
s = Student('dharshini',24)
s.print_detail() # print value
print_detail() # throw error
Student.print_detail() #throw error because object values are assigned from class to method. It is only done by init

# eg: 2

class Student1:
    def __init__(self,mark):
        self.mark = mark
    def getMark(self,limit=100): # assigning default value
        if self.mark>limit:
            return True
        else:
            return False
s1 = Student1(100)
s2 = Student1(200)
print(s1.getMark())# False
print(s2.getMark())# true
        
