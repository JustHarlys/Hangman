import random
from words_for_hangman import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what user has guessed
    
    lives = 10
    
    
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have used these letters ', ' '.join(used_letters))
        
        # what current word is (i.e W - R D)
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list)) 
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                
            else:
                lives = lives - 1 # takes away a life if wrong
                print(f'Letter is not in word. {lives} lives' )
        elif user_letter in used_letters:
            print('You have already used that character. Please try another')
            
        else:
            print('Invalid character. Please try again.')
            
    # gets here when word_letters length is equal to 0 or when lives equal to 0
    if lives == 0:
        print('You died, sorry.')
    else:
        print(f'You guessed the word: {word}')
    
hangman()
        