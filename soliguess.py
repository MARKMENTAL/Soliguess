import random
import sys


def endgame(tries):
	print("\n\nPoint Limit reached, game over.")
	print("Total tries before winning: ", tries)
	sys.exit()


def coregame():
	points = 0
	tries = 0
	cards = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
	suits = ["of ♥","of ♦","of ♠", "of ♣"]

	print("Welcome to Soliguess. The goal of the game is to guess one less")
	print("than the number the computer will guess to get a pair of cards.")
	print("Each pair of cards is worth 1 point")
	print("Game ends when you get 5 points\n\n")
	suitchoice = int(input("First, Enter a suit to use:\n1.Hearts\n2.Diamonds\n3.Spades\n4.Clubs\n"))

	while (points < 5):
		num = input("Enter a number from 0 to 12\n")
	
		# pulling a joker card is a way to skip to the end screen
		if (num.lower() == "j"):
			print("Cheat: you pulled a Joker card")
			endgame(tries);
	
		if (num.isnumeric() == False):
			num = "1"
	
		if(int(num) > 12):
			num = "1"
		
		cpunum = random.randint(0, 12)
		print("Your Card: ", cards[int(num) - 1], suits[suitchoice - 1])
		print("\nCPU Card: ", cards[cpunum - 1], suits[suitchoice - 1])

		if (int(num) == cpunum - 1):
			print("You guessed right")
			points+=1
			tries+=1
			print("Your current points: " +str(points))
			
		elif (int(num) != cpunum - 1):
			print("You guessed wrong")
			tries+=1
			print("Your current points: " +str(points))	
				
		if (points >= 5):
			endgame(tries);

coregame()
