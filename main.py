import random

HANGMAN_PHOTOS = {0: "    x-------x", 1: """    x-------x
    |
    |
    |
    |
    |""", 2: """    x-------x
    |       |
    |       0
    |
    |
    |""", 3: """    x-------x
    |       |
    |       0
    |       |
    |
    |""", 4: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", 5: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""", 6: """    x-------x
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
    """Shows the opening screen with the max number of tries.
    :return: None.
    :rtype: None.
    """
    print(HANGMAN_ASCII_ART,"\n",MAX_TRIES)

def guess_a_letter():
    """Asks from the user to guess a character and lowers it.
    :return: The character after lowering it.
    :rtype: char.
    """
    chosen_letter = input("guess a character: ")
    chosen_letter = chosen_letter.lower()
    return chosen_letter

def is_valid_letter(guessed_letter, old_letters_list):
    """Checks if the given character by the user is valid for the game.
    :param guessed_letter: The given character from the user.
    :param old_letters_list: The list of the letters the user already guessed.
    :type guessed_letter: char.
    :type old_letters_list: list.
    :return: True if the character is valid, otherwise False.
    :rtype: bool.
    """
    if len(guessed_letter) > 1 or not guessed_letter.isalpha() or guessed_letter in old_letters_list:
        return False
    return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Try to add the given character (if it's valid) to the user's guessed letters list.
    :param letter_guessed: The given character from the user.
    :param old_letters_guessed: The list of the letters the user already guessed.
    :type letter_guessed: char.
    :type old_letters_guessed: list.
    :return: True if the function succedded, otherwise False.
    :rtype: bool.
    """
    if is_valid_letter(letter_guessed,old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    return False

def show_hidden_word(secret_word, old_letters_guessed):
    """Prints the current board with '_' and the guessed letters according to the secret word.
    :param secret_word: The word the user need to guess.
    :param old_letters_guessed: The list of the letters the user already guessed.
    :type secret_word: str.
    :type old_letters_guessed: list.
    :return: None.
    :rtype: None.
    """
    result = ""
    for word in secret_word:
        if word in old_letters_guessed:
            result += word + " "
        else:
            result += '_ '
    print (result)

def check_win(secret_word, old_letters_guessed):
    """Checks if the user won according to the guessed letters and the secret word.
    :param secret_word: The word the user need to guess.
    :param old_letters_guessed: The list of the letters the user already guessed.
    :type secret_word: str.
    :type old_letters_guessed: list.
    :return: True if the user has guessed all of the letters, otherwise False.
    :rtype: bool.
    """
    for word in secret_word:
        if word not in old_letters_guessed:
            return False
    return True

def print_hangman(num_of_tries):
    """Prints the current state of the hangman drawing based on the user's tries.
    :param num_of_tries: The amount of failed tries the user used.
    :type num_of_tries: int.
    :return: None.
    :rtype: None.
    """
    print(HANGMAN_PHOTOS[num_of_tries])

def make_a_move(old_letters_guessed, current_tries, chosen_word):
    """Makes a move with a given character and prints the result of the move.
    :param old_letters_guessed: The list of the letters the user already guessed.
    :param current_tries: The current amount of tries the user used.
    :param chosen_word: The word which the user need to guess.
    :type old_letters_guessed: list.
    :type current_tries: int.
    :type chosen_word: str.
    :return: None.
    :rtype: None.
    """
    letter_guessed = guess_a_letter()

    # valid input
    if try_update_letter_guessed(letter_guessed,old_letters_guessed):

        # a correct guess
        if letter_guessed in chosen_word:
            print_state(chosen_word,old_letters_guessed,current_tries)
            if (check_win(chosen_word,old_letters_guessed)):
                print("WIN")
                play_again()
            else:
                make_a_move(old_letters_guessed,current_tries,chosen_word)

        # a wrong guess
        else:
            print("):")
            current_tries += 1
            print_state(chosen_word,old_letters_guessed,current_tries)
            if (current_tries == MAX_TRIES):
                print(f"LOSE \nthe word was: {chosen_word}")
                play_again()
            else:
                make_a_move(old_letters_guessed,current_tries,chosen_word)

    # invalid input
    else:
        print("X")
        if old_letters_guessed:
            old_letters_guessed.sort()
            words_with_arrow = ''.join(char + '>' for char in old_letters_guessed)
            print(words_with_arrow)
        print("please try again")
        make_a_move(old_letters_guessed,current_tries,chosen_word)
def play_again():
    """Gives the user an option to play again.
    :return: None.
    :rtype: None.
    """
    while True:
        try:
            play_again = int(input("Do you wish to play again? (1 for yes and 0 for no): "))
            if play_again != 1 and play_again != 0:
                print("invalid input, please try again")
                continue
            # input is 1, the game is starting all over again
            elif play_again == 1:
                start_game()

            # input is 0, the game is over
            break
        except ValueError:
            print("invalid input, please try again")

def choose_word(file_path, index):
    """Reads a given file (if exists) and return a word from the file based on a given index.
    :param file_path: The file path to the words file.
    :param index: The location of the specific word.
    :type file_path: str.
    :type index: int.
    :return: The word which located in the file in the given index.
    :rtype: str.
    """
    try:
        with open(file_path,"r") as fp:
            data = fp.read()
            words = data.split()
            # correct the index if needed
            while index >= len(words):
                index = index - len(words)
            chosen_word = words[index - 1]

    except FileNotFoundError:
        print("file was not found, please try again\n")
        chosen_word = get_word_from_file_path_and_index()
    return chosen_word

def print_state(chosen_word,old_letters_guessed,current_tries):
    """Prints the hangman's current state and the board's current state.
    :param chosen_word: The word which the user need to guess.
    :param old_letters_guessed: The list of the letters the user already guessed.
    :param current_tries: The current amount of tries the user used.
    :type chosen_word: str.
    :type old_letters_guessed: list.
    :type current_tries: int.
    :return: None.
    :rtype: None.
    """
    print_hangman(current_tries)
    show_hidden_word(chosen_word,old_letters_guessed)

def get_word_from_file_path_and_index():
    """Gets a file path and an index from the user and returns a specific word.
    :return: The word located in the specific index in the given file.
    :rtype: str.
    """
    words_file_path = input("enter the file path to the file that contains the words: ")
    words_file_path = words_file_path.replace("\"","")
    while True:
        try:
            word_index = int(input("\nenter the index for the word (starting at 1): "))
            break
        except ValueError:
            print("invalid input, please try again")
    return choose_word(words_file_path,word_index)

def start_game():
    """Initializes the game by showing the opening screen, getting input and stating the first move.
    :return: None.
    :rtype: None.
    """
    opening_screen()
    chosen_word = get_word_from_file_path_and_index()
    old_letters_guessed = list()
    current_tries = 0
    print_state(chosen_word,old_letters_guessed,current_tries)
    make_a_move(old_letters_guessed, current_tries,chosen_word)

if __name__ == '__main__':
    start_game()


