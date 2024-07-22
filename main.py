import random
import string

from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    lives = 6  # number of lives
    print(word)
    # game loop
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have used these letters:', ' '.join(used_letters))

        # what current word is (ie W_RD)
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f"Letter '{user_letter}' is not in the word.")
        elif user_letter in used_letters:
            print('You have already guessed that letter.')
        else:
            print('Invalid character.')

        # hangman visual (you can customize this)
        print(f"Lives remaining: {lives}")

    # game over
    if lives == 0:
        print('You died. The word was', word)
    else:
        print('You guessed the word!')

hangman()
