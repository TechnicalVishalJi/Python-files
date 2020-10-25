import os

i = 0

def soldier(c):
	for file in os.listdir(c):
		d = file.split(".")[0]
		os.rename(d, i)
		i += 1
		

soldier()