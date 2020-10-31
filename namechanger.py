namect = int(input("How many names you want to add?\n"))
names = []
srnames = []
check = namect/2
check2 = namect//2

while namect>0:
	name = input("Enter name\n").split(" ")
	names.append(name[0])
	srnames.append(name[1])
	namect -= 1

if check!=check2:
	srnames[check2], srnames[check2 + 1] = srnames[check2 + 1], srnames[check2]
	
a = reversed(srnames)
for i, j in zip(names,a):
		print(i, j)
		continue
	