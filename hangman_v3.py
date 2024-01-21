import random
from clear_screen import clear

#todo Maybe change to read from file
word_list = ['manga', 'goiaba', 'uva', 'geladeira', 'banana', 'melancia', 'carro', 'aviao', 'livro', 'casa']

#todo Handle non letter inputs
#todo More modularization > word choice

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

#Functions

#Initialise game
def initialise_game(word_list):
    clear()
    print('\n>>>>>>>>>>Hangman<<<<<<<<<<\n')
    print('\nBem Vinde ao jogo da forca!')
    print('Adivinhe a palavra abaixo:')
    word = random.choice(word_list)
    chances = 6
    board_index = 0
    wrong = []
    uncovered = ['_' for letter in word]
    print(board[0])
    return uncovered, word, chances, wrong, board_index

#Game status
def game_status(uncovered, chances, wrong):
    print()
    print(uncovered)
    print(f'\nVocê tem {chances} chances!')
    print('Letras erradas: ', wrong)

#Update game
def update_game_status(uncovered, word, guess, chances, wrong, board_index):
    if guess in wrong:
        print('Voce ja escolheu essa letra!\n')
    elif guess in word:
        for i, letter in enumerate(word):
            if guess == letter:
                uncovered[i] = guess
    else:
        wrong.append(guess)
        chances -= 1
        board_index += 1
    print(board[board_index])
    print()
    return chances, wrong, uncovered, board_index

#Get guess
def get_guess():
    guess = input('\nEscolha uma letra: ').lower()
    return guess     

#Check if game is over
def check_game_over(uncovered, word):
    if "_" not in uncovered:
        print(uncovered)
        print(f"\nVoce venceu! A palavra é : {word}\n") 
        return True
    else:
        return False
    
#Game function
def hangman():

    uncovered, word, chances, wrong, board_index = initialise_game(word_list)
    
    while chances > 0:
        game_status(uncovered, chances, wrong)
        guess = get_guess()
        chances, wrong, uncovered, board_index = update_game_status(uncovered, word, guess, chances, wrong, board_index)
        if check_game_over(uncovered, word):
            break
    else:
        print(f'Voce perdeu =( A palavra era : {word} \n')

#Main
if __name__ == "__main__":
    hangman()