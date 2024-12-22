#string

str1 = "this is  a string . \n we are create a string in python"
print(str1)
print(len(str1))


str2 = "hello world"
final_str = str1 + "    " +str2
print(final_str)
print(len(final_str))    #calculate lenth of sstring by len()


#indexing

str3="harsh_patel"
print(str3[4])
print(str3[6])

#slicing

str4="harshghadiya"
print(str4[1:5])
print(str4[4:])
print(str4[:3])     #automatically count starting index


str5="apple"
print(str5[-3:-1])   #negative indexing




#string function

str6="i am studing python from"
print(str6.endswith("ube"))
print(str6.endswith("om"))
print(str6.capitalize()) #become 1st latteer is capital of string 
print(str6.replace("o","a"))
print(str6.find("o"))
print(str6.count("o"))


#practice

str7=input("enter the first name:-")
print("first name is",str7)
print((len(str7)))


#condition statement

age=21
if(age>=18):
    print("can vote and apply for license")
else:
   print("CANNOT vote")




light="green"

if(light == "red"):
 print("stop")   #indentation --  proper space

elif(light == "yellow"):
   print("look")

elif(light == "green"):
   print("go")   

else:
   print("light is broken")



   #practice

marks=45
if(marks>=90):
   print("grade is A")
elif(marks>=80 and marks<90):
   print("grade is B")   
elif(marks>=70 and marks<80):
   print("grade is C")
elif(marks>70):
   print("grade is D") 
else:
   print("fail")        



   number=int(input("enter the number:-"))
   if(number%2==0):
      print("number is even")
   else:
      print("the number is odd") 


num1=int(input("enter the num1 :-"))
num2=int(input("enter the num2 :-"))
num3=int(input("enter the num3 :-"))
if(num1>num2 and num1>3):
   print("num1 is greatest")
elif(num2>num1 and num2>num3):
   print("num2 is greatest")
else:
   print("num3 is greatest")      


   num4=int(input("enter the number:-"))
   if(num4%7==0):
      print("number is multiple of 7.")
   else:
      print("number is not multiple of 7.")   

