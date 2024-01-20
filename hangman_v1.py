import random
from os import system, name

#Clear screen function
def clear_screen():
    #Windows
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def hangman():

    clear_screen()
    print('\nBem Vinde ao jogo da forca!')
    print('Adivinhe a palavra abaixo:\n')
    
    #List of possible words
    words = ['banana', 'uva', 'manga', 'melancia', 'goiaba']
    #Choose word
    word = random.choice(words)
    #Print the spaces for the letters
    uncovered = ['_' for letter in word]
    print(uncovered)
    #Number of chances
    chances = len(word)
    wrong = []
    
    #Ask for letter   
    while chances > 0:
        print('\nVocê tem ', chances, ' chances!')
        guess = input('Escolha uma letra: ').lower()
        
        if guess in word:
            i = 0
            for letter in word:
                if guess == letter:
                    uncovered[i] = guess
                i += 1
        else:
            wrong.append(guess)
            print('Letras erradas: ', wrong)
            chances -= 1
        print(uncovered)
        
        if "_" not in uncovered:
            print("\nVoce venceu! A palavra é :", word)
            break
            
    print("\nVoce perdeu =( A palavra era :", word)
        
hangman()