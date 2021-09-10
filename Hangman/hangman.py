import random
from words import words
import string
from hangman_visual import lives_visual_dict

def choose_valid_word(words):
	word=random.choice(words)
	while '-' in word or ' ' in word:
		word=random.choice(words)
		print(word)

	return word.upper()	

def hangman():
	word=choose_valid_word(words)
	letters=set(word)
	alphabet=set(string.ascii_uppercase)
	used_letters=set() # user's guesses

	lives=7

	while len(letters)>0 and lives>0:
		print("You have ",lives," lives left.""You've used these letters so far : ",' '.join(used_letters))
		word_list=[letter if letter in used_letters else '-' for letter in word]
		print(lives_visual_dict[lives])
		print('Current word: ',' '.join(word_list))
		user_letter=input("Guess a letter: ").upper()
		if user_letter in alphabet - used_letters:
			used_letters.add(user_letter)
			if(user_letter in letters):
				letters.remove(user_letter)
			else:
				lives=lives-1	
				print("Your letter is not in the word.")


		elif user_letter in used_letters:
			print("You've already used that letter! Try again")

		else:
			print('Invalid character. Try again')	

	if(lives==0):
		print(lives_visual_dict[lives])
		print(f"Sorry, you died the word was {word}!")
	else:
		print(f"Yay, you guessed the word {word}!")	

if __name__ == '__main__':
	hangman()

