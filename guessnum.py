import random

def guessnum(x):
	random_number=random.randint(1,x)
	guess=0
	while guess!=random_number:
		guess=int(input("Give me your best guess! --> "))
		if(guess<random_number):
			print("Too low! Try something higher!")
		if(guess>random_number):
			print("Too high! Try something smaller!")

	print(f"Yay you guessed the number {random_number} right!")		

guessnum(10)	