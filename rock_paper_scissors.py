import random

def play():
	user=input("Enter 'r' for rock, 'p' for paper and 's' for scissors: ")
	computer=random.choice(['r','p','s'])

	if(user==computer):
		return "It's a tie!"

	elif who_won(user,computer):
		return "You won!"

	return "You lost..."	


#r>s,s>p,p>r
def who_won(player1,player2):
	if(player1=='r' and player2=='s') or (player1=='s' and player2=='p') or (player1=='p' and player2=='r'):
		return True

print(play())