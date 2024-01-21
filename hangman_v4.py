# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from clear_screen import clear

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

word_list = ['manga', 'goiaba', 'uva', 'geladeira', 'banana', 'melancia', 'carro', 'aviao', 'livro', 'casa']

# Classe
class Hangman:
    uncovered = []
    wrong = []
    chances = 6
    board_index = 0
    
	# Método Construtor
    def __init__(self, word_list):
        self.word_list = word_list
        self.board = board
        self.word = random.choice(word_list)
        print(board[0])
        clear()
    
    def choose_word(self):
        word = random.choice(word_list)
        uncovered = ['_' for letter in word]
        return word, uncovered
    
    def get_guess(self):
        guess = input('\nEscolha uma letra: ').lower()
        return guess  
                    
    def check_game_over(self, uncovered, word):
        if "_" not in uncovered:
            print(uncovered)
            print(f"\nVoce venceu! A palavra é : {word}\n") 
            return True
        else:
            return False       
    
    def update_uncovered(self, word, guess, uncovered):
        for i, letter in enumerate(word):
            if guess == letter:
                uncovered[i] = guess
        return uncovered
    
    def update_game_status(self, guess, uncovered, word, chances, wrong, board_index):
        if guess in wrong:
            print('Voce ja escolheu essa letra!\n')
        elif guess in word:
            self.update_uncovered(word, guess, uncovered)
        else:
            wrong.append(guess)
            chances -= 1
            board_index += 1
        print()
        return chances, wrong, uncovered, board_index
        
    def game_status(self, uncovered, chances, wrong, board_index):
        print(board[board_index])
        print()
        print(uncovered)
        print(f'\nVocê tem {chances} chances!')
        print('Letras erradas: ', wrong)
        
    def hangman(self, uncovered, word, chances, wrong, board_index):

        while chances > 0:
            self.game_status(uncovered, chances, wrong)
            guess = self.get_guess()
            chances, wrong, uncovered, board_index = self.update_game_status(uncovered, word, guess, chances, wrong, board_index)
            if self.check_game_over():
                break
        else:
            print(f'Voce perdeu =( A palavra era : {word} \n')
        
#Main
if __name__ == "__main__":
    game = Hangman(word_list)