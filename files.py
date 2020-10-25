#Reading file

with open("//storage/emulated/0/qpython/scripts3/bluetooth_chat.py", "rt") as w:
	print(w.readline())
	print(w.tell())
	print(w.readline())
	w.seek(20)
	print(w.readline())
	print(w.tell())

#for a in w:
#	print (a)

#print(w.read())

#Writing file

#x = open("//storage/emulated/0/qpython/scripts3/bluetooth_chat.py", "w")

#print(x.write("This is a completely edited file\n"))

#x.close()

#Appending file

#y = open("//storage/emulated/0/qpython/scripts3/bluetooth_chat.py", "a")

#print(y.write("This is an appended file\n"))

#y.close()

#Reading and writing File

#z = open("//storage/emulated/0/qpython/scripts3/bluetooth_chat.py", "r+")

#print(z.read())

#print(z.write("This is a written file\n"))
#print(z.write("This is a written file\n"))