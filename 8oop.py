class Student:
     
     def __init__(self,name,marks):
          self.name = name
          self.marks = marks
          print("adding new student in database")

     def hello(self):
          print("hello i am harsh") 

     def get_marks(self):
          return self.marks         







s1 = Student("karsan",98)
print(s1.name)

s2 = Student("mayank",90)
print(s2.name,s2.marks)


s1.hello()
print(s1.get_marks())


class Student:
     def __init__(self,name,marks):
          self.name = name
          self.marks = marks

     def get_avg(self):
          sum = 0
          for val in self.marks:
           sum += val
          print("hi",self.name,"your avg score is:",sum/3)

s1 = Student("tony",[66,87,98])
s1.get_avg()     

class Acoount:
     def __init__(self,balance,accountno):
          self.balance = balance
          self.accountno = accountno

acc1 =Acoount(1000,9867)
print(acc1.balance)
print(acc1.accountno)          
          








     

          