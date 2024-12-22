f=open("demo.txt","r")
#data = f.read(6)   #f.read(5)  -> only return first 5 letter/element/ of file
#print(data)

#line2=f.readline()
#print(line2)
#line2=f.readline()
#print(line2)

#print(type(data))

f = open("demo.txt","w")       #write mod
f.write("i want to learn javascript")


f= open("demo.txt","a")       #appened mod

f.write("\n then recat js")


f = open("demo.txt","a+")
f.write("abc")


with open("demo.txt","r") as f:
    data=f.read()
    print(data)



    def check_for_word():
        word = "xlearing"
        with open("practice.txt","r") as f:
            data = f.read()
            if(data.find(word) != -1):
                print("found")
            else:
                print("not found")

f.close()