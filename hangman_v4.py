# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name

# Board (tabuleiro)
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
    def __init__(self, word_list):
        self.word_list = word_list
        self.board = board
        self.word = random.choice(word_list)
        self.uncovered = []
        self.wrong = []
        self.chances = len(self.word)
        self.clear_screen()

    def clear_screen(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
            
	# Método para adivinhar a letra
    def guess(self, uncovered):
        self.guess = input('Choose a letter: ').lower()
        self.wrong = []
        if self.guess in word:
            i = 0
            for letter in word:
                if guess == letter:
                    uncovered[i] = guess
                i += 1
        else:
            wrong.append(guess)
            print('Letras erradas: ', wrong)
            chances -= 1
        
	# Método para verificar se o jogo terminou
    def endgame(self, uncovered):
        while chances > 0:
            self.status(uncovered, chances, wrong)
            guess = get_guess()
            chances, wrong, uncovered = update_game_status(uncovered, word, guess, chances, wrong)
            if win(uncovered, word):
                break
            else:
                print("\nVoce perdeu =( A palavra era :", word)
        
	# Método para verificar se o jogador venceu
    def win(self, uncovered):
        if "_" not in uncovered:
            print(uncovered)
            print("\nVoce venceu! A palavra é :", word, "\n") 
            return True
        else:
            return False
        
	# Método para não mostrar a letra no board
    def uncovered(self, word):
        self.uncovered = ['_' for letter in word]
        print(self.uncovered)
        
	# Método para checar o status do game e imprimir o board na tela
    def status(self, uncovered, chances, wrong):
        print(uncovered)
        print('\nVocê tem ', chances, ' chances!')
        print('Letras erradas: ', wrong)