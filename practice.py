import time

def dec1(func1):
	def jd():
		print("jsjsjdjjdjfkm")
		func1()
	return jd
@dec1
def who():
	print("jou")
	
#who = dec1(who)
who()

class Army:
	workingdays = 365
	def __init__(self, sname, ssalary, swork):
		self.name = sname
		self.salary = ssalary
		self.work = swork
	def __add__(self, n):
		return self.salary + n.salary
	def __truediv__(self, n):
		return self.salary / n.salary
	def __repr__(self):
		return f"Soldier({self.name}, {self.salary}, {self.work})"
	def __str__(self):
		return f"Name is {self.name}, Salary is {self.salary}, Work is {self.work}"
	def info(self):
		return f"Name is {self.name}, Salary is {self.salary}, he is a {self.work}"
	def cl(cls, k):
		cls.workingdays = k
		
Vishal = Army("Vishal", 90000, "soldier")

#soldier.name = "Vishal"
#soldier.salary = 90000
#soldier.work = "soldier"

print(Vishal.info())
Vishal.cl(34)
print(Vishal.workingdays)

class Programmer(Army):
	holidays = 56
	def __init__(self, a,b,c,d):
		self.name = a
		self.salary = b
		self.work = c
		self.language = d

#This class will work when we will remove single inheritence
#class cool(Army ,Programmer):
	#pass
	
Mukesh = Programmer("Mukesh", 586545, "Programmer", "Java")

print(Mukesh.salary)
print(Vishal+ Mukesh)
print(Vishal/Mukesh)
print(Vishal)
print(repr(Mukesh))
#There is also super().__init__() for functions
#Also check mapping operaters in funvtions

print(type(Vishal))
print(dir(Vishal))

import inspect
print(inspect.getmembers(Vishal))

#def search():
#	print("Starting")
#	time.sleep(2)
#	
#	text = (yield)
#	print("done")
#	
#	
#search=search ()
#next(search)

#search.send("yes")

#os module

import os

print(os.getcwd())
#os.chdir("//storage/emulated/0")
print(os.getcwd())
print(os.listdir("//storage/emulated/0"))
#os.mkdir("Vishal")
#os.makedirs("t/jsjs")
#os.rename("harrydiet.txt", "vishaldiet.txt")
print(os.environ.get("Path"))
print(os.path.join("storage","emulated","0"))
print(os.path.exists("jdjd"))
print(os.path.isdir("t"))
print(os.path.isfile("Vishal"))

import pickle

friends = ["Mukesh", "Prince"]
with open("pickling.vi", "wb") as obj:
	pickle.dump(friends, obj)
	
with open("pickling.vi", "rb") as reading:
	print(pickle.load(reading))
