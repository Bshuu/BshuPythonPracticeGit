import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #Randomly chooses a random word in the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()
    
def hangman():
    word = get_valid_word(words) 
    word_letters = set(word) #Letters in the word
    alphabet = set(string.ascii_uppercase) 
    used_letters = set() #What the user has guessed

    lives = 6

    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have ', lives ,' lives left and used these letters: ', ' '.join(used_letters))

        # what the current word is (ie. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))


        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1 # Takes away a life if wrong
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have already guessed that character! Please try again')

        else:
            print('Invalid character. Please try again')

    if lives == 0:
        print('You died sorry, the word was', word)
    else:
        print('You won! the word was', word)

hangman()