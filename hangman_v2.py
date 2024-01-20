import random
from clear_screen import clear

word_list = ['manga', 'goiaba', 'uva', 'geladeira', 'banana', 'melancia', 'carro', 'aviao', 'livro', 'casa']

#Functions

def initialise_game(word_list):
    clear()
    print('\nBem Vinde ao jogo da forca!')
    print('Adivinhe a palavra abaixo:\n')
    word = random.choice(word_list)
    chances = len(word)
    wrong = []
    uncovered = ['_' for letter in word]
    return uncovered, word, chances, wrong
    
def game_status(uncovered, chances, wrong):
    print(uncovered)
    print(f'\nVocê tem {chances} chances!')
    print('Letras erradas: ', wrong)

def update_game_status(uncovered, word, guess, chances, wrong):
    if guess in wrong:
        print('Voce ja escolheu essa letra!\n')
    elif guess in word:
        for i, letter in enumerate(word):
            if guess == letter:
                uncovered[i] = guess
    else:
        wrong.append(guess)
        chances -= 1
    return chances, wrong, uncovered 

def get_guess():
    guess = input('\nEscolha uma letra: ').lower()
    print()
    return guess     

def check_game_over(uncovered, word):
    if "_" not in uncovered:
        print(uncovered)
        print(f"\nVoce venceu! A palavra é : {word}\n") 
        return True
    else:
        return False
    
#Game function
def hangman():

    initialise_game(word_list)
    uncovered, word, chances, wrong = initialise_game(word_list)
    
    while chances > 0:
        game_status(uncovered, chances, wrong)
        guess = get_guess()
        chances, wrong, uncovered = update_game_status(uncovered, word, guess, chances, wrong)
        if check_game_over(uncovered, word):
            break
    else:
        print(f'Voce perdeu =( A palavra era : {word} \n')

#Main
hangman()