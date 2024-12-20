#program to implement string functions


#str.endswith()

s="naman"
print(s.endswith("n"))   #true
print(s.endswith("an"))  #true
print(s.endswith("man")) #false


s="satyarajsingh"
print(s.endswith("singh")) #true
print(s.endswith("jsingh")) #true
print(s.endswith("rajsingh")) #true


#str.capitalize()
 
s="mayankesh"
print(s.capitalize())

s="rajeshchand"
print(s.capitalize())

#str.replace(old,new)

s="kaushik"
print(s.replace("au","ik"))
print(s.replace("s","ab"))
print(s.replace("k","cdef"))
print(s.replace("ku","gh"))
print(s.replace("i","o"))
print(s.replace("ik","p"))
print(s.replace("shi","r"))


#str.find(word)

s="Rajkot is a big city"
print(s.find("r"))
print(s.find("is"))


#str.count()

s="ahmedabad"
print(s.count("e"))
print(s.count("a"))

                          
                          
                          
