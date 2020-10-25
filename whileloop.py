def while_loop():
	while (True) :
		a =int(input("input any number\n"))
		if a<=100:
			print ("Try again\n")
			continue
		else:
			print ("Congratulations")
			i = input("Do you want to play again? 'yes' or 'no'\n")
			if i == "yes":
				while_loop()
			else:
				break

			
if __name__=="__main__":
	while_loop()

		

