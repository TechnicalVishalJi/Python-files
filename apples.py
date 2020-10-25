def divcalc(a,m,max):
	for child in range(m,max+1):
		j = a/child
		k = a//child
		if j ==k:
			print(f"{child} is the divisor of {a}")

if __name__=="__main__":
	apples = int(input("Enter number of apples\n"))

	minchild = int(input("Enter minimum number of children\n"))

	maxchild = int(input("Enter maximum number of children\n"))
			
	divcalc(apples, minchild, maxchild)

		