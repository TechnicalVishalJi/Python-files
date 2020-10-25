class library:
	global books
	global lenders
	lenders = {}
	books = ["Maths", "English", "StoryBook"]
	def __init__(self, n):
		self.name = n
		
	def a(self, f):
		return books.append(f)
	
	def r(self, d):
		return books.append(d)
		
	def d(self):
		return books
		
	def ll(self):
		print(lenders)
		
	def l(self, m):
			if m in books:
				i = input("Enter your name\n").capitalize()
				lenders.update({i:m})
				books.remove(m)
				print(f"{m} is lended to you!")
			else:
				print(f"{m} book is not available our library or you have entered a wrong value")
		
Library = library("Library")
print("This is the list of available books-", Library.d())



while (True):
	inp = input("Do you want to get or add or return or see available or lended books in the library? 'yes' or 'no'.\n")
	if inp=="yes":
		g = input("What you want to do? 'add' or 'return' or 'seebooks' or 'get' or 'seelenders'.\n")
		if g == "add":
			i = input("Write book name\n").capitalize()
			Library.a(i)
			print("Successfully added")
		if g == "get":
			i = input("Write book name\n").capitalize()
			Library.l(i)
		if g == "seelenders":
			Library.ll()
			
		
		if g == "return":
			i = input("Write book name\n").capitalize()
			Library.r(i)
			print("Successfully returned")
		if g == "seebooks":
			print(Library.d())
			continue
	elif inp == "no":
		break
		
	else:
		print("You have entered a wrong value. Please correct it.\n")
		continue
		
