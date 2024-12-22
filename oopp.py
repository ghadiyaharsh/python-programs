class student:
    def __init__(self,name):
        self.name = name

s1 = student("harsh")
print(s1.name)




class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass        #privet

acc1 = Account("234567","becerty")
print(acc1.acc_no)
#print(acc1.acc_pass)


"""
class Person:
    __name = "anonymas"

    def _hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()    

p1 = Person()

print(p1.welcome())
"""



class car:            #inheritance-single 
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped.")



class toyotacar(car):
    def __init__(self,name):
        self.name = name

car1 = toyotacar("fortuner")
car2 = toyotacar("prius")      

print(car1.start())




#multi-level inheritence

class fortuner(toyotacar):
    def __init__(self, type):
        self.type = type
                    
car1 = fortuner("diesel")   
car1.start()             




class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"        

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)




#super method 
#class method
class marks:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math


    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"


m1 = marks(98,97,99)
print(m1.percentage)


m1.phy = 56
print(m1.percentage)

#polymorphism

#operater overloading

print(1+2)
print(type(1))

print("apna"+"college")   #concatenate
print(type("apna"))


print([1,2,3] + [4,5,6])    #merge
print(type([1,2,3]))



#complex numbers

class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real,"i +",self.img,"j")

        def __add__(self,num2):   #dunder function
            newReal = self.real + num2.real
            newImg = self.img + num2.img
            return complex(newReal,newImg)
   

num1 = complex(1,3)
num1.shownumber()

num2 = complex(4,6)
num2.shownumber()


#num3 = num1 + num2
#num3.shownumber()

#practice
"""
class circle:
    def __init__(self,radius):
        self.radius = radius
   


def area(self):
   return (22/7) * self.radius**2
   
def perimeter(self):
    return 2 * (22/7) * self.radius

c1=circle(20)   
print(c1.area())
print(c1.perimeter())
"""


class employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary


    def showdetails(self):
        print("role =",self.role)
        print("dept =",self.dept)
        print("salary =",self.salary)

e1  = employee("accountant","finance","90000")            
e1.showdetails()





