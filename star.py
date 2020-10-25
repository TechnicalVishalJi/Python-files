n = int(input("Enter the number of lines\n"))
b = int(input("do you want ascending(0) or descending order(1)"))

if b is 0:
	a = 0
	while a<=n:
		print("*"*a, end=" ")
		print("\n", end=" ")
		a = a+1
elif b is 1:
	while n>0:
		print("*"*n, end=" ")
		print("\n", end="")
		n = n-1