# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
import clear_screen as clear

# Lista de palavras
word_list = ['manga', 'goiaba', 'uva', 'geladeira', 'banana', 'melancia', 'carro', 'aviao', 'livro', 'casa']
 
# Board (tabuleiro)
board = ['''

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
    def __init__(self):
        clear
        self.board = board
        self.uncovered = []
        self.wrong = []
        self.chances = 6
        self.board_index = 0
            
    def choose_word(self, word_list):
        self.word = random.choice(word_list)
        self.uncovered = ['_' for letter in self.word]
        return self.word, self.uncovered
        
    def get_guess(self):
        self.guess = input('\nEscolha uma letra: ').lower()
        return self.guess

    def check_guess(self):
        if self.guess in self.wrong:
            print('Voce ja escolheu essa letra!')
        elif self.guess in self.word:
            for i, letter in enumerate(self.word):
                if self.guess == letter:
                    self.uncovered[i] = self.guess
        else:
            self.wrong.append(self.guess)
            print('Letras erradas: ', self.wrong)
            self.chances -= 1
            self.board_index += 1
        return self.uncovered, self.chances, self.board_index, self.wrong
            
	# Método para verificar se o jogo terminou
    def endgame(self):
        if self.win() or self.chances == 0:
            return True
        else:
            return False
        
	# Método para verificar se o jogador venceu
    def win(self):
        if "_" not in self.uncovered:
            print(self.board[self.board_index])
            print(''.join(self.uncovered))
            print(f"\nVoce venceu! =D \nA palavra é : {self.word} \n") 
            return True
        else:
            return False
  
	# Método para checar o status do game e imprimir o board na tela
    def status(self):
        print(self.board[self.board_index])
        print(''.join(self.uncovered))
        if self.chances == 0:
            print(f"\nVoce perdeu =( \nA palavra era : {self.word} \n")
        else:
            print(f'\nVocê tem {self.chances} chances!')
            print('Letras erradas: ', self.wrong)

if __name__ == '__main__':
    game = Hangman()
    game.choose_word(word_list)
    
    while not game.endgame():
        game.status()
        game.get_guess()
        game.check_guess()
    if not game.win():
        game.status()
        
        
        
    
    
    