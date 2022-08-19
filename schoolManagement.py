import pickle

def add():
	f = open("vi.bin", "ab")
	while True:
		name = input("Enter student name: ")
		while True:
			try:
				rno = int(input("Enter student roll no: "))
				marks = int(input('Enter student marks: '))
				break
			except Exception:
				print("You have entered wrong value")
				continue
		pickle.dump([rno, name, marks], f)
		choice1 = input("Do you want to continue? [y/n]: ")
		if choice1.lower() == "n":
			f.close()
			print("Records Saved!\n")
			break

def read():
	open("vi.bin", "ab").close()
	f = open("vi.bin", "rb")
	rec = []
	while True:
		try:
			rec1 = pickle.load(f)
			rec.append(rec1)
		except EOFError:
			f.close()
			break
	f.close()
	if len(rec) == 0:
		print("No Records found!")
	else:
		for i in rec:
			print(i[0], i[1], i[2])
	print("\n")
	
def searchAndUpdate():
		inp = input("What you want to search? [ name(n) / rollno(r) / marks(m) ]")
		rec = []
		#rec1 = []
		f = open("vi.bin", "rb")
		while True:
			try:
				data = pickle.load(f)
				rec.append(data)
				#rec1.append(data)
			except EOFError:
				f.close()
				break
		f.close()
		rec1 = str(rec)
		namerec = []
		rollrec = []
		markrec = []
		while True:
			if inp.lower() == "n":
				name = input("Enter name you want to search: ")
				for i in rec:
					if name.lower() in i[1].lower():
						namerec.append(i)
				if len(namerec) > 0:
					print("Following records found:")
					for i in namerec:
						print(i[0], i[1], i[2])
				else:
					print("No name found matching with " + name)
							
			elif inp.lower() == "r":
				rollno = int(input("Enter roll no you want to search: "))
				for i in rec:
					if i[0] == rollno:
						rollrec.append(i)
				if len(rollrec) > 0:
					print("Following records found:")
					for i in rollrec:
						print(i[0], i[1], i[2])
				else:
					print("No rollno found matching with " + str(rollno))
					
			elif inp.lower()== "m":
				marks = int(input("Enter marks you want to search: "))
				for i in rec:
					if i[2] == marks:
						markrec.append(i)
				if len(markrec) > 0:
					print("Following records found:")
					for i in markrec:
						print(i[0], i[1], i[2])
				else:
					print("No student marks found matching with " + str(marks))
			if (len(namerec) > 0) or (len(rollrec) >0) or (len(markrec)>0):
				break
			inp1 = input("Want to search again? [y/n]: ")
			if inp1.lower() == "n":
				break
			
		if (len(namerec) > 0) or (len(rollrec) >0) or (len(markrec)>0):
			choice1 = input('Do you want to update any record? [y/n]: ')
			if choice1.lower() == 'y':
				choice2 = input("What you want to update? [ name(n) / rollno(r) / marks(m) ] : ")
				if choice2.lower() == 'n':
					name1 = input("Enter name you want to update: ")
					searches = []
					count = 0
					for i in rec:
						if i[1].lower() == name1.lower():
							searches.append(count)
						count += 1
					if len(searches) > 1:
						print("Multiple names found matching with ", name1+"\n")
						for i in searches:
							print(rec[i][0], rec[i][1], rec[i][2])
						count = 1
						for i in searches:
							print("Type " , i+1 , " to update name" , count)
							count += 1
						print("Type 0 to update all names")
						choice3 = int(input("Enter your choice: "))
						if choice3 == 0 :
							name2= input("Enter new name to replace all names: ")
							for i in searches:
								rec[i][1] = name2
						else:
							name2 = input("Enter new name to replace name " + str(choice3) + ": ")
							rec[(choice3-1)][1] = name2
					elif len(searches) == 1:
						print("Name found: " + rec[searches[0]][1])
						name2 = input("Enter new name: ")
						rec[searches[0]][1] = name2
					else:
						print("No name found matching with " + name1)
									
				elif choice2.lower() == 'r':
					roll1 = int(input("Enter rollno you want to update: "))
					searches = []
					count = 0
					for i in rec:
						if i[0] == roll1:
							searches.append(count)
						count += 1
					if len(searches) > 1:
						print("Multiple roll no found matching with ",str(roll1)+"\n")
						for i in searches:
							print(rec[i][0], rec[i][1], rec[i][2])
						count = 1
						for i in searches:
							print("Type " , i +1, " to update roll no" , count)
							count += 1
						print("Type 0 to update all roll no")
						choice3 = int(input("Enter your choice: "))
						if choice3 == 0:
							roll2= int(input("Enter new roll no to replace all roll no: "))
							for i in searches:
								rec[i][0] = roll2
						else:
							roll2 = int(input("Enter new roll no to replace roll no " + str(choice3) + ": "))
							rec[(choice3-1)][0] = roll2
					elif len(searches) == 1:
						print("Roll no found:", rec[searches[0]][0], "with data\n", rec[searches[0]][0], rec[searches[0]][1],rec[searches[0]][2])
						roll2 = int(input("Enter new roll no: "))
						rec[searches[0]][0] = roll2
					else:
						print("No name found matching with " + str(roll1))
					
				elif choice2.lower() == 'm':
					mark1 = int(input("Enter marks you want to update: "))
					searches = []
					count = 0
					for i in rec:
						if i[2] == mark1:
							searches.append(count)
						count += 1
					if len(searches) > 1:
						print("Multiple students found with marks matching with ", str(mark1)+"\n")
						for i in searches:
							print(rec[i][0], rec[i][1], rec[i][2])
						count = 1
						for i in searches:
							print("Type " , i +1, " to update marks of" , count)
							count += 1
						print("Type 0 to update all marks")
						choice3 = int(input("Enter your choice: "))
						if choice3 == 0:
							mark2= int(input("Enter new marks to replace all old marks: "))
							for i in searches:
								rec[i][2] = mark2
						else:
							mark2 = int(input("Enter new marks to replace marks of student " + str(choice3) +": "))
							rec[(choice3-1)][2] = mark2
					elif len(searches) == 1:
						print("Marks found for:", rec[searches[0]][1])
						mark2 = int(input("Enter new marks: "))
						rec[searches[0]][2] = mark2
					else:
						print("No name found matching with " + str(mark1))
				
			if str(rec) != rec1:
				with open("vi.bin", "wb") as f:
					for i in rec:
						pickle.dump(i, f)
					print("Records updated!\n")
			else:
				print('Record not updated\n')

def searchAndDelete():
	inp = input("What you want to search? [ name(n) / rollno(r) / marks(m) ]")
	rec = []
	f = open("vi.bin", "rb")
	while True:
		try:
			data = pickle.load(f)
			rec.append(data)
		except EOFError:
			f.close()
			break
	f.close()
	rec1 = str(rec)
	searchrec = []
	deletedItems = []
	while True:
		if inp.lower() == "n":
			name = input("Enter name you want to search: ")
			index = 0
			for i in rec:
				if name.lower() in i[1].lower():
					searchrec.append(index)
				index += 1
			if len(searchrec) > 0:
				print("Following records found:")
				for i in searchrec:
					print(rec[i][0], rec[i][1], rec[i][2])
			else:
				print("No name found matching with " + name)
							
		elif inp.lower() == "r":
			rollno = int(input("Enter roll no you want to search: "))
			index = 0
			for i in rec:
				if i[0] == rollno:
					searchrec.append(index)
				index += 1
			if len(searchrec) > 0:
				print("Following records found:")
				for i in searchrec:
					print(rec[i][0], rec[i][1], rec[i][2])
			else:
				print("No rollno found matching with " + str(rollno))
					
		elif inp.lower()== "m":
			marks = int(input("Enter marks you want to search: "))
			index = 0
			for i in rec:
				if i[2] == marks:
					searchrec.append(index)
				index += 1
			if len(searchrec) > 0:
				print("Following records found:")
				for i in searchrec:
					print(rec[i][0], rec[i][1], rec[i][2])
			else:
				print("No student marks found matching with " + str(marks))
		if len(searchrec) > 0:
			break
		inp1 = input("Want to search again? [y/n]: ")
		if inp1.lower() == "n":
			break
			
	if len(searchrec) > 0:
		choice1 = input("Do you want to delete any record? [y/n]: ")
		if choice1.lower() == "y":
			print("Type")
			for i in searchrec:
				print(i, "to delete", rec[i])
			print("\nTo delete more than one record, type numbers of them, separated by comma")
			values = []
			while True:
				try:
					choice2 = input("Enter your choice: ")
					for i in choice2.split(","):
						values.append(int(i))
					break
				except Exception:
					print("Please enter correct values")
					continue
			intVal = sorted(values, reverse=True)
			for i in intVal:
				item = rec.pop(int(i))
				deletedItems.append(item)
		
	if str(rec) != rec1:
		with open("vi.bin", "wb") as f:
			for i in rec:
				pickle.dump(i,f)
		print("Below records deleted:")
		for i in deletedItems:
			print(i)
	else:
		print("No record deleted\n")

while True: #to run this program again and again
	choice = input("What you want to do? [ add(a) / read(r) / searchAndUpdate(s) / searchAndDelete(d) ] records : ") #asking user wish
	if choice.lower() == "a": #add new record
		add() #calling add new record function
		
	elif choice.lower() == "r": #read all records
		read() #calling read function
		
	elif choice.lower() == "s": #search and update records
		searchAndUpdate() #calling function
	
	elif choice.lower() == "d": #search and delete records
		searchAndDelete() #calling function