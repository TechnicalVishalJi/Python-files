def printer(m):
	n = 1
	while m > 0:
		print(n)
		n +=1
		m -=1

pw = input("Enter Password\n")
if pw == "8755655vishal":
	while True:
		try:
			inp = int(input ("Enter Maximum Numbers\n"))
		except Exception as a:
			print("Enter a number")
		else:
			printer(inp)
else:
	print("Wrong Password\n")