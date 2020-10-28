i = "My Name is Vishal Singh" 
print (i[4])
print (len(i))
print (i[0:9])
print (i[::3])
print (i[3::])
print (i[:10:])
print (i[-5::])
print (i[::-1])
print (i, end=" and\n")
print (i.isalnum())
print (i.startswith("My"))
print (i.endswith("Singh"))
print (i.replace("Vishal", "Raja"))
print (i.count(i))
print (i.upper())
print (i.lower())
print (i.find("is"))

i = "my name is Vishal Singh"

print (i.capitalize())
print (i.encode())
print (i.isidentifier())
print (i.isprintable())
print (i.isspace())
print (i.join("ab"))
print(i.rfind("is"))
print (i.swapcase())
print (i.title())


a = ["home", "home", "web", "string", "what"]
print(a[2])

num = [8,99,3,73,388,62,85,37,73]
print (num[:4:2])
num.sort()
print (num)
num.reverse()
print (num)
print (len(num))
print (max(num))
print (min(num))
num.append(73)
print (num)
num.insert(2, 34)
num.pop()
print (num)

num = (1,)
print (type(num))

z = 3
s = 4
x = 6
z,s,x= x,z,s
print (z,s,x)

dictionary = {"egg":"anda", "boil":"ubalna", "fry":"pakana"}

print (dictionary)
dictionary["rules"] = {"kanoon", "niyam"}
print (dictionary)
del dictionary ["rules"]
print (dictionary)
dictionary.update({"rules":{"kanoon","niyam"}})
print (dictionary.keys())
print (dictionary.items())
print(dictionary.copy())


list = [3,34,34,24,24,34,23]
a = set(list)
print (a)

a.add(29)
print (a)
a.remove(23)
print (a)

b = a.union([343,434,4])
b = a.intersection([343,434,4])
print (b)

g = [433,434,453]
f = int(input("enter the number\n"))
if f in g:
	print("true")
else:
	print("false")


#Age identifier

a = int(input("Enter your age\n"))
if a>70:
	print ("Please enter your correct age")
elif a<5:
	print ("Please enter your correct age")
elif a>18:
	print ("You can drive")
elif a==18:
	print ("We cannot determine, so come for checking")
else :
	print ("You cannot drive")