#classes
class Employee:
	no_of_leaves = 8
	#initialisation function
	def __init__(self, name, salary, role):
		self.name = name
		self.salary = salary
		self.role = role
		
	#function for objects
	def printDetails(self):
	     return f"Name is {self.name}, salary is {self.salary} and role is {self.role}"
	
	#classmethod changes class variables
	@classmethod
	def set_no_of_leaves(cls, newLeaves):
	  	cls.no_of_leaves = newLeaves
   	
vishal = Employee("Vishal", 45000, "Manager")
raj = Employee("Raj", 30000, "Worker")
print(raj.printDetails())
raj.set_no_of_leaves(30)#change main class variable
print(vishal.no_of_leaves)#also affected other objects

#decorators
def dec(func):
	def exec():
		func()
	return exec
	
@dec
def show():
	print("yes")
	
show()
#dec(show) #both are same

#args
def add(a,b,*other):
	sum = a+b
	for i in other:
		sum += i
	return sum
	
print(add(1,2,3,4,5,6,7))
print(add(1,2,*[3,4,5,6,7]))#both are same