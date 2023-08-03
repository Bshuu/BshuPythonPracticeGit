import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #Randomly chooses a random word in the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

        return word.upper()
    
def hangman():
    word = get_valid_word(words) #Letters in the word
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase) 
    used_letters = set( )#What the user has guessed

    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - user_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print('You have already guessed that letter! Please try again')

user_input = input("Take a guess: ")
print(user_input)