import random

HANGMAN_PHOTOS = {1: "    x-------x", 2: """    x-------x
    |
    |
    |
    |
    |""", 3: """    x-------x
    |       |
    |       0
    |
    |
    |""", 4: """    x-------x
    |       |
    |       0
    |       |
    |
    |""", 5: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", 6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""", 7: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}

HANGMAN_ASCII_ART = """
Welcome to the game Hangman
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/"""
MAX_TRIES = 6

def opening_screen():
    print(HANGMAN_ASCII_ART,"\n",MAX_TRIES)

def guess_a_letter():
    chosen_letter = input("guess a character: ")
    chosen_letter = chosen_letter.lower()
    print(is_valid_letter(chosen_letter))

def is_valid_letter(guessed_letter, old_letters_list):
    if len(guessed_letter) > 1 or not guessed_letter.isalpha() or guessed_letter in old_letters_list:
        return False
    return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if is_valid_letter(letter_guessed,old_letters_guessed):
        old_letters_guessed.append(letter_guessed)

def show_hidden_word(secret_word, old_letters_guessed):
    result = ""
    for word in secret_word:
        if word in old_letters_guessed:
            result += word + " "
        else:
            result += '_ '
    return result

def check_win(secret_word, old_letters_guessed):
    for word in secret_word:
        if word not in old_letters_guessed:
            return False
    return True

def show_board():
    chosen_word = input("please enter a word: ")
    word_count = len(chosen_word)
    print("_ " * word_count)

def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[state_index])

if __name__ == '__main__':
    secret_word = "yes"
    old_letters_guessed = old_letters_guessed = ['d', 'g', 'e', 'i', 'k', 'y']
    print(show_hidden_word(secret_word, old_letters_guessed))
    print(check_win(secret_word,old_letters_guessed))
