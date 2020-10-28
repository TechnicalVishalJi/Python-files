import math

a = 2 
b =3 
if (a==b):
	print("equal")
else:
	print("unequal")

'''
it is a multiline comment 
'''	
#to find out the variable assigned is of which type, so you can use the commands below
c = type(a)
print(c)
#then if  you wnat to change this type to another

d = float(a)
print(d)
d = int(a)
print(d)
d = str(a)
print(d)

new = "variable"
print(new[2:7])

print(len(new))

# to finish space between the variables
any = "         vishal        "
print(any.strip())

names = "vishal, shubham, mukesh"

print(names.lower())
print(names.upper())
print(names.replace("," , "singh,"))

# for printing a letter inside a line

name1 = "vishal singh"
name2 = "boy"
line = "my name is {} and i am a bad {}".format(name1, name2)
#or you can use
line2 = f"my name is {name1} and i am a bad {name2} "
print(line)
print(line2)

# operators is python
l= 4
m = 5
print(l+m)
print(l-m)
print(l*m)
print(l/m)
print(l%m) #it is used for finding the remainder
print(l**m) #it is  an operator used for finding the power
print(l//m) #it will convert the result into whole number

''''
there are 4 types of collections in python
1.  list
2.  set
3.  tuple
4.  dictionary'
'''
#list has square brackets
lst = [54,453,4,34]
print(lst)
print(len(lst))

print(type(lst))

print(lst[1:3])
print(lst)

#you can also change the list items

lst[2] = 23
print(lst)

lst.append(58)
print(lst)

lst.remove(453)
print(lst)

lst.insert(1, 76)
print(lst)

del lst[0]
print(lst)

# if you want to delete the list you can use "del lst" here lst is  a variable name

#tuple use round brackets
tupl = ("vishal", "shubham", "mukesh")
print(tupl)
print(type(tupl))

# set have curly brackets
s1 = {23,3,6,5,5,6,4,5,6,6,5,5,4,5,5,3}
print(s1)
print(len(s1))
s1.add(40)
print(s1)
s1.update([35,67,34])
print(s1)
s1.discard(67) #you can use discard if set has or has not that number
print(s1)

#input is always taken as string
amount = input("Enter your salary\n")
amount = int(amount)

if (amount>20000):
	print("you have a very nice salary")

elif (amount==20000):
	print("your salary is good")
	
else:
	print("your salary is not as much as should be")
