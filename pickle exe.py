import requests
import pickle

link = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

try:
	requ = requests.get(link)
except Exception as e:
	print("No Internet connection!")
else:
	req = requ.text
	list1 = req.split("\n")
	list2 = [response.split(",") for response in list1]

def save():
	with open("project.vishal", "wb") as obj:
		pickle.dump(list2, obj)
			
def show():
	with open("project.vishal", "rb") as file:
		print(pickle.load(file))

while True:		
	inp = input("Enter the given keywords for showing or saving data\n1. save\n2. show\n")

	try:
		if inp=="1" or inp=="save":
			save()
			print("Successful!")
			
		elif inp=="2" or inp=="show":
			show()
		
		else:
			print("Error! Enter 1 or 2")
		continue
		
	except Exception as e:
		print("Firstly, apply save option! or you have no web connection")