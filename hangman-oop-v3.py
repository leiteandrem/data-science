# Hangman Game
# Object-oriented programming [OOP]

# Imports
import random
from os import system, name

# Funcion to clear the screen on each execution
def clear_screen():
 
    # Windows
    if name == 'nt':
        _ = system('cls')
 
    # Mac ou Linux
    else:
        _ = system('clear')

# Board
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.wrong_letters = []
		self.chosen_letters = []
		
	# Method to guess the letter
	def guess(self, letter):
		
		if letter in self.word and letter not in self.chosen_letters:
			self.chosen_letters.append(letter)
		
		elif letter not in self.word and letter not in self.wrong_letters:
			self.wrong_letters.append(letter)
		
		else:
			return False
		
		return True
		
	# Method to check if the game has ended
	def hangman_over(self):
		return self.hangman_won() or (len(self.wrong_letters) == 6)
		
	# Method to check if the player has won
	def hangman_won(self):
		
		if '_' not in self.hide_word():
			return True
		return False
		
	# Method to not show the letter on the board
	def hide_word(self):
		
		rtn = ''
		
		for letter in self.word:
			if letter not in self.chosen_letters:
				rtn += '_'
			else:
				rtn += letter
		return rtn
		
	# Method to check the game status and print the board on the screem
	def print_game_status(self):
		
		print (board[len(self.wrong_letters)])
		
		print ('\nWord: ' + self.hide_word())
		
		print ('\nWrong letters: ',)
		
		for letter in self.wrong_letters:
			print (letter,)
		
		print ()
		
		print ('Correct letters: ',)
		
		for letter in self.chosen_letters:
			print (letter,)
		
		print ()

# Method to randomly read a word from the words list
def rand_word():

	# Words lits
    words = ['hangover', 'troy', 'badboys', 'avatar', 'avenger']

    # Randamly chooses a word
    word = random.choice(words)
        
    return word

# Main Method
def main():

	clear_screen()

	# Creates the object and randomly selects a word
	game = Hangman(rand_word())

	# While the game is not over, print the status, prompt for a letter and read a character
	while not game.hangman_over():
		
		#  Status do game
		game.print_game_status()
		
		# Get  input letter
		user_input = input('\nInput a letter: ')
		
		# Checks if the typed letter is part of  the word
		game.guess(user_input)

	# Checks the game status
	game.print_game_status()	

	# According to the status, prints a message on the screen for the user
	if game.hangman_won():
		print ('\nCongratulations! YOU WON \O/ !!')
	
	else:
		print ('\nGame over! You Loose :( !!')
		print ('The word was ' + game.word)
		
	print ('\nTry again!!\n')

# Starts the game
if __name__ == "__main__":
	main()

