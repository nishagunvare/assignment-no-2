assignment-no-2import random
name = input("Enter your name? ")

print("Good Luck ! ", name)

words = ['mobile','laptop','smartwatch','colours','watch','camera', 'bullet','google','sunglasses','medicine'] word = random.choice(words)

print("Guess the characters")

guesses = ''

turns = 12

while turns > 0:

failed = 0

for char in word: 	
	if char in guesses: 
		print(char)
		
	else: 
		print("_")
		
		failed += 1
		
if failed == 0:
	
	print("You Win") 
	print("The word is: ", word) 
	break
	
guess = input("guess a character:")
guesses += guess 

if guess not in word:
	turns -= 1
			
	print("Wrong")
	
	print("You have", + turns, 'more guesses')
 
	if turns == 0:
		print("You Loose , better luck next time") 
#OUTPUT Enter your name? komal Good Luck ! komal Guess the characters _ _ _ _ _ _ guess a character:s Wrong You have 11 more guesses _ _ _ _ _ _ guess a character:a _ a _ _ _ _ guess a character:w Wrong You have 10 more guesses _ a _ _ _ _ guess a character:o _ a _ _ o _ guess a character:l l a _ _ o _ guess a character:p l a p _ o p guess a character:t l a p t o 
