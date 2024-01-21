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
    
	# Método Construtor
    def __init__(self):
        self.chances = 6
        self.board_index = 0
        self.wrong = []
        self.uncovered = []
        
    def get_guess(self):
        self.guess = input('\nEscolha uma letra: ').lower()
        return self.guess 
    
    def choose_word(self, word_list):
        self.word = random.choice(word_list)
        self.uncovered = ['_' for letter in self.word]
        return self.word
    
    def update_status(self):
        if self.guess in self.word:
            for i, letter in enumerate(self.word):
                if self.guess == letter:
                    self.uncovered[i] = self.guess
        elif self.guess in self.wrong:
            print('Você já escolheu essa letra.')
        else:
            self.chances -= 1
            self.wrong.append(self.guess)
            self.board_index += 1
        return self.chances, self.board_index, self.wrong, self.uncovered
    
    def check_win(self):
        if '_' not in self.uncovered:
            self.show_status()
            print(f"\nVoce venceu! A palavra é : {self.word}\n") 
            return True
        else:
            return False
    
    def show_status(self):
        print(board[self.board_index])
        print(f'\nPalavra: {" ".join(self.uncovered)}')
        print(f'Letras erradas: {" ".join(self.wrong)}')
        print(f'Chances: {self.chances}')
	
 
#Main
def main():
    game = Hangman()
    game.choose_word(word_list)
    
    while game.chances > 0:
        game.show_status()
        game.get_guess()
        game.update_status()
        if game.check_win():
            break
    else:
        game.show_status()
        print(f'\nVoce perdeu =( A palavra era : {game.word} \n')

# Execute o programa
if __name__ == "__main__":
    main()