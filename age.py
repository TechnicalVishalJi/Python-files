def age(i):
	if inp <100:
		print("You will become 100 years old in ", 100-inp, "years and year will be ", 2020+(100-inp))
	
	elif inp>1920:
		print("You will become 100 years old in " , 100-(2020-inp), "years and year will be ", inp+100)
	
	elif inp<1920 or inp>100:
		print("You seem to be the oldest person alive!\n")
	
	elif inp<=0 or inp>2020:
		print("You are not yet born\n!")
	
	else:
		print("Only write numbers\n")

try:
	inp = int(input("Enter age\n"))
except Exception as e:
	print("Write only numbers")
	
else:
	age(inp)

