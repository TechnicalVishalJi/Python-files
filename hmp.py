print("Health Management Programme")

nm = input("If you are client then write your name and you are observer then write 'Observer'.\n")
name = nm.capitalize()
type = input("Do you want to choose 'exercise' or 'diet'\n")

def getdate():
	import datetime
	return datetime.datetime.now()

if name == "Harry" and type == "diet":
	a = input("What you ate?\n")
	with open("harrydiet.txt", "a") as hd:
		hd.write("Date and time: ")
		hd.write(str(getdate()))
		hd.write("  Food:  ")
		hd.write(a)
		hd.write("\n")
		
elif name == "Rohan" and type == "diet":
	b = input("What you ate?\n")
	with open("rohandiet.txt", "a") as rd:
		rd.write("Date and time: ")
		rd.write(str(getdate()))
		rd.write("  Food:  ")
		rd.write(b)
		rd.write("\n")
		
elif name == "Hammad" and type == "diet":
	c = input("What you ate?\n")
	with open("hammaddiet.txt", "a") as dd:
		dd.write("Date and time: ")
		dd.write(str(getdate()))
		dd.write("  Food:  ")
		dd.write(c)
		dd.write("\n")
		
elif name == "Harry" and type == "exercise":
	d = input("What you did?\n")
	with open("harryexercise.txt", "a") as he:
		he.write("Date and time: ")
		he.write(str(getdate()))
		he.write("  Exercise:  ")
		he.write(d)
		he.write("\n")
		
elif name == "Rohan" and type == "exercise":
	e = input("What you did?\n")
	with open("rohanexercise.txt", "a") as re:
		re.write("Date and time: ")
		re.write(str(getdate()))
		re.write("  Exercise:  ")
		re.write(e)
		re.write("\n")
		
elif name == "Hammad" and type == "exercise":
	f = input("What you did?\n")
	with open("hammadexercise.txt", "a") as de:
		de.write("Date and time: ")
		de.write(str(getdate()))
		de.write("  Exercise:  ")
		de.write(f)
		de.write("\n")
		
elif name == "Observer" and type == "exercise":
		g = input("Write the name whose exercise you want to see.\n")
		ga = g.capitalize()
		if ga == "Harry":
			with open("harryexercise.txt", "r+") as ohe:
				print(ohe.read())
				y = input("Do you want to write this file? write 'yes' or 'no'.\n")
				if y == "yes":
					editohe = input("What you want to write in this file?\n")
					ohe.write(editohe)
					print("successfully written")
				
					
		 
		if ga == "Rohan":
			with open("rohanexercise.txt", "r+") as ore:
				print(ore.read())
				y = input("Do you want to write this file? write 'yes' or 'no'.\n")
				if y == "yes":
					editore = input("What you want to write in this file?\n")
					ore.write(editore)
					print("successfully written")
				
					
		if ga == "Hammad":
			with open("hammadexercise.txt", "r+") as ode:
				print(ode.read())
				y = input("Do you want to write this file? write 'yes' or 'no'.\n")
				if y == "yes":
					editode = input("What you want to write in this file?\n")
					ode.write(editode)
					print("successfully written")
				
					
					
elif name == "Observer" and type == "diet":
		h = input("Write the name whose diet you want to see.\n")
		ha = h.capitalize()
		if ha == "Harry":
			with open("harrydiet.txt", "r+") as ohd:
				print(ohd.read())
				z = input("Do you want to write this file? write 'yes' or 'no'.\n")
				if z == "yes":
					editohd = input("What you want to write in this file?\n")
					ohd.write(editohd)
					print("successfully written")
		 
		if ha == "Rohan":
			with open("rohandiet.txt", "r+") as ord:
				print(ord.read())
				z = input("Do you want to write this file? write 'yes' or 'no'.\n")
				if z == "yes":
					editord = input("What you want to write in this file?\n")
					ord.write(editord)
					print("successfully written")
				    
					
					
		if ha == "Hammad":
			with open("hammaddiet.txt", "r+") as odd:
				print(odd.read())
				z = input("Do you want to write this file? write 'yes' or 'no'.\n")
				if z == "yes":
					editodd = input("What you want to write in this file?\n")
					odd.write(editodd)
					print("successfully written")
				
				