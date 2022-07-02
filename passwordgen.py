import random

print("Password Generator")

chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()><.,0123456789'

number=int(input('Number of passwords to generate? '))
length=int(input("Enter desired length of each password: "))

print('\nHere are your passwords: \n')

for pwd in range(number):
	password=''
	for c in range(length):
		password+=random.choice(chars)
	print(password)

