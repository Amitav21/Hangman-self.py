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
MAX_TRIES = 7

def opening_screen():
    print(HANGMAN_ASCII_ART,"\n",MAX_TRIES)

def guess_a_letter():
    chosen_letter = input("guess a character: ")
    chosen_letter = chosen_letter.lower()
    return chosen_letter

def is_valid_letter(guessed_letter, old_letters_list):
    if len(guessed_letter) > 1 or not guessed_letter.isalpha() or guessed_letter in old_letters_list:
        return False
    return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if is_valid_letter(letter_guessed,old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    return False

def show_hidden_word(secret_word, old_letters_guessed):
    result = ""
    for word in secret_word:
        if word in old_letters_guessed:
            result += word + " "
        else:
            result += '_ '
    print (result)

def check_win(secret_word, old_letters_guessed):
    for word in secret_word:
        if word not in old_letters_guessed:
            return False
    return True

def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])

def make_a_move(old_letters_guessed, current_tries, chosen_word):
    letter_guessed = guess_a_letter()
    if try_update_letter_guessed(letter_guessed,old_letters_guessed):
        if letter_guessed in chosen_word:
            print_state(chosen_word,old_letters_guessed,current_tries)
            if (check_win(chosen_word,old_letters_guessed)):
                print("WIN")
            else:
                make_a_move(old_letters_guessed,current_tries,chosen_word)
        else:
            print("):")
            current_tries += 1
            print_state(chosen_word,old_letters_guessed,current_tries)
            if (current_tries == MAX_TRIES):
                print(f"LOSE \nthe word was: {chosen_word}")
            else:
                make_a_move(old_letters_guessed,current_tries,chosen_word)

    else:
        print("X")
        if old_letters_guessed:
            old_letters_guessed.sort()
            words_with_arrow = ''.join(char + '>' for char in old_letters_guessed)
            print(words_with_arrow)
        print("please try again")
        make_a_move(old_letters_guessed,current_tries,chosen_word)

def choose_word(file_path, index):
    words_dict = {}
    with open(file_path,"r") as fp:
        data = fp.read()
        words = data.split()

        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1

        count_single_shows = len(words_dict)

        if index >= len(words):
            index = index - len(words)
        chosen_word = words[index - 1]

        return count_single_shows, chosen_word

def print_state(chosen_word,old_letters_guessed,current_tries):
    print_hangman(current_tries)
    show_hidden_word(chosen_word,old_letters_guessed)

def start_game():
    opening_screen()
    words_file_path = input("enter the file path to the file that contains the words: ")
    words_file_path = words_file_path.replace("\"","")
    word_index = int(input("enter the index for the word (starting at 1): "))
    chosen_word = choose_word(words_file_path,word_index)[1]
    old_letters_guessed = list()
    current_tries = 1
    print_state(chosen_word,old_letters_guessed,current_tries)
    make_a_move(old_letters_guessed, current_tries,chosen_word)



if __name__ == '__main__':
    start_game()


