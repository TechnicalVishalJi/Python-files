import re

str = input("Enter The line in which email addresses are junked\n")

def emailfinder(n):
	email = re.findall(r"\D\w+@\w+.\w+",n)
	return email
	
a = emailfinder(str)

for i in a:
	print(i)