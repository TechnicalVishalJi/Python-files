def isCorrect(n):
	tO = n[1]-n[0]
	tO2 = n[0]
	ino = 1
	if tO == tO2:
		for no in n:
			res = tO*ino
			if no == res:
				print(tO, " * ", ino, " = ",no, "is correct")
			else:
				print(tO, " * ", ino, " = "f"{no} is wrong, {res} is correct")
			ino += 1

if __name__=="__main__":
	wrong_tables = [6, 12, 18, 24, 30, 39, 42, 48, 54, 60]	
	print(wrong_tables)
	isCorrect(wrong_tables)
	
	wrong_tables2 = []
	res2 = 10
	while res2>0:
		anTa = int(input("If you want to check another table check it here! Input values one by one.\n"))
		wrong_tables2.append(anTa)
		res2 -= 1
	
	isCorrect(wrong_tables2)