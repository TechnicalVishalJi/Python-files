#pylint:disable=E1101
import time
import sys
from functools import reduce

print(time.asctime(time.localtime(time.time())))

print(sys.path)

lis = ["adc", "john", "Maven"]

a = " and ".join(lis)
print(a, "others")

#map function

n = [1,2,3,4,5]

print(list(map(lambda a: a*a, n)))

def square (a):
	return a*a
	
def cube(a):
	return a*a*a

math = [square, cube]

n= [1,2,3,4,5]

for numb in n:
	v = list(map(lambda x: x(numb), math))
	
	print(v)
	
# filter

lit = [57,9,36,8,89,52]

def filtr(a):
	return a>10
for i in lit:
		v = list(filter(filtr, lit))	
		print(v)
		
#Reduce

print(reduce(lambda x, y : x*y, lit))

list = [items for items in range(2, 101) if items%2==0]
for a in list:
	print(a)
	
#print(list)

dictionary = {a:f"Item{a}" for a in range(50)}

print(dictionary)

#for reversing it
print({b:a for a, b in dictionary.items()})

#Exercise

lis = []
dict = {}
se = set((()))


while(True):
	 
	 try:
	 	i = int(input("How many items do you want to add?\n"))
	 except Exception as e:
	 	print("error! enter a number")
	 	continue
	 a = input("Which type of comprehension do you want?\nl for list\nd for dictionary\ns for set\ne for exit\n")
	 if a =="l":
	 	while i>0:
	 		l = input("Write the item\n")
	 		lis.append(l)
	 		i -= 1
	 	print(lis)
		
	 elif a =="d":
		 while i>0:
		 	l = input("Write the first item\n")
		 	v = input("Write the second item\n")
		 	dict.update({l:v})
		 	i -= 1
		 print(dict)
		
	 elif a =="s":
	 	
		 while i>0:
			 l = input("Write the item(!The repeated item will no be printed)\n")
			 se.add(l)
			 i -= 1
		 print(se)
	
	 elif a =="e":
			break		
				
	 else:
		 print("You have entered a wrong input. Try again!")
		 continue
		
print("Thanks")