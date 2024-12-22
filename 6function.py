def calc_sum(a,b):
    sum=a+b
    print(sum)
    return sum
calc_sum(8,9)
calc_sum(7,9)


def average(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg

average(2,3,4)


def printhello():
    print("hello world")
printhello()    



cities = ["delhi","gurgaon","noida","pune","mumbai","chhenai"]
def print_len():
    print(len(cities))
print_len()


def print_list(list):
    for item in list:
        print(item, end=" ")  #end=" " -> print same line element of list 
print_list(cities)        


def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
        print(fact)
factorial(5)           


def converter(usd_val):
    inr_val=usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")
converter(100)    


def oddeven():
 num =   int(input("enter the number :-"))
 if( num % 2 == 0):
     print("even")
 else:
    print("odd")

oddeven()



def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    show(3)