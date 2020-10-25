import time


name = ["Vishal", "Mukesh", "Shubham", "Prince"]
works = {"Vishal":"kuch bhi", "Mukesh":"Youtuber"}

def a(b, *args, **kwargs):
	print(b)
	for nam in args:
		print(nam)
		
	for names, work in kwargs.items():
		print(f"{names} is {work}")
		
a("These are my friends", *name, **works)

time.sleep(2)

print(time.asctime(time.localtime()))