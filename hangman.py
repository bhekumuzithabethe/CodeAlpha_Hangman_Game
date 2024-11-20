import random
from words import words
hangman_art ={
    0: (' ',
        ' ',
        ' '),

    1: (' O ',
        '  ',
        ' '),

    2: (' O ',
        ' | ',
        ' '),
    
    3: (' O ' ,
        '/| ',
        ' '),

    4: (' O ',
        '/|\\',
        ' '),

    5: (' O ',
        '/|\\ ',
        '/ ' ),
    
    6: (' O ',
        '/|\\ ',
        '/ \\ '),

}


def display_man(incorrect_guesses):
    print(f'\n\nYou have: {incorrect_guesses} attempts remaining')
    print('\n/////////////////////')
    for line in hangman_art[incorrect_guesses]:
        print('\t'+line)
    print('/////////////////////\n\n')
    
def display_hint(hint):
    print(f'The word has {len(hint)} letters: '+' '.join(hint))

def display_answer(answer):
    print(' '.join(answer))

def main():
    while True:
        start_game = int(input('\nEnter 1 to continue and 0 to quit: '))
        
        if start_game == 1:
            
            answer = random.choice(words).lower()
            hint = ['_']*len(answer)
            incorrect_guesses = 0
            guessed_letters = set()
            is_running = True
            
            print('\nThis is an a fruit Hangman game in which you guess a name of a fruit chosen at random from a fruit list consisting 61 fruits.\n\nRULES: \n1. You have 6 chances to guess the fruit name guessing only one letter of the whole word.\n2. Do not enter a number.\n3. Do not enter a whole word, just one character of the fruit you think it is.\n4. Do not enter any of the special characters such as(@, #,$.etc)')
            while is_running:
                display_man(incorrect_guesses)
                display_hint(hint)

                guess = input('\nEnter a letter: ').lower()
                
                #If the user enters a number or more than one character
                if len(guess)!=1 or not guess.isalpha():
                    print('\nInvalid input. \nYou need to guess 1 letter at a time, no numbers and no special charecters try again.')
                    continue
                
                #If the user enters a character they have alredy guessed
                if guess in guessed_letters and guess not in answer:
                    print(f'{guess} is already guessed and was incorrect.')
                elif guess in guessed_letters:
                    print(f'{guess} is already guessed.')
                    
                
                guessed_letters.add(guess)

                #If the guess is correct
                if guess in answer:
                    for i in range(len(answer)):
                        if answer[i] == guess:
                            hint[i] = guess
                    print('\nCORRECT! The word now looks like: '+' '.join(hint))    
                else:
                    incorrect_guesses +=1

                if '_' not in hint:
                    display_man(incorrect_guesses)
                    display_answer(f'The correct answer is: {answer}')
                    print('YOU WIN!')
                    is_running = False
                elif incorrect_guesses==6:
                    display_man(incorrect_guesses)
                    display_answer(f'The correct answer is: {answer}')
                    print('YOU LOOSE!')
                    is_running = False            
            
            
        else:
            print('GOODBYE!!!')
            break

if __name__ == '__main__':
    main()