import random

print("Snake Water Gun game")

choices = ["Snake", "Water", "Gun"]

n = 10
tie = 0
wins = 0

while n>0:
	c = random.choice(choices)
	pc = input("Enter Your Choice. s for Snake, w for water and g for gun\n")
	
	if pc == "s" and c == "Snake":
		print("No one won this round because computer also chosen Snake")
		tie = tie+1
		
	elif pc == "w" and c == "Snake":
		print("You lost this round because computer chosen Snake")
		
	elif pc == "g" and c == "Snake":
		print("You won this round because computer chosen Snake")
		wins = wins+1
		
	elif pc == "s" and c == "Water":
		print("You won this round because computer chosen Water")
		wins = wins+1
		
	elif pc == "w" and c == "Water":
		print("No one won this round because computer also chosen Water")
		tie = tie+1
		
	elif pc == "g" and c == "Water":
		print("You lost this round because computer chosen Water")
		
	elif pc == "s" and c == "Gun":
		print("You lost this round because computer chosen Gun")
		
	elif pc == "w" and c == "Gun":
		print("You won this round because computer chosen Gun")
		wins = wins +1
		
	elif pc == "g" and c == "Gun":
		print("No one won this round because computer also chosen Gun")
		tie = tie+1
		
	else:
		print("Your input was wrong! Try again")
		n=n+1
		
	n = n-1
	

print("You won", wins, "round(s)")
print("No one won in", tie, "round(s)")
print("I won", 10-(wins+tie), "round(s)")