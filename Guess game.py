n = 18
g = 10
print()
print ("Guess Game\n")
print ("Guess any number between 0 to 100 and you have 10 guesses")
while (True):
	i = float(input())
	g = g-1
	if i<18 and g>0:
		print("Somewhat small number!\n", "Guesses left=",g)
		continue
	elif i>18 and g>0:
		print("Somewhat bigger number!\n", "Guesses left=",g)
		continue
		
	elif i==18 and g>0:
		print("You won!\n", "Finished game in",10-g, "guesses")
		break
	
	elif g==0:
		print("You loose!\n", "Guesses left=0")
		break		