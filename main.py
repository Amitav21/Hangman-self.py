import random

def openingScreen():
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
    print(HANGMAN_ASCII_ART,"\n",MAX_TRIES)

def guessAletter():
    chosen_letter = input("please guess a character: ")
    chosen_letter = chosen_letter.lower()
    if len(chosen_letter) > 1 and not chosen_letter.isalpha():
        print("E3")
    elif len(chosen_letter) > 1:
        print("E1")
    elif not chosen_letter.isalpha():
        print("E2")
    else:
        print(chosen_letter)

def showBoard():
    chosen_word = input("please enter a word: ")
    word_count = len(chosen_word)
    print("_ " * word_count)

def printStates():
    print("first state:")
    print("    x-------x")
    print("second state:")
    print("""    x-------x
    |
    |
    |
    |
    |""")
    print("third state:")
    print("""    x-------x
    |       |
    |       0
    |
    |
    |""")
    print("fourth state:")
    print("""    x-------x
    |       |
    |       0
    |       |
    |
    |""")
    print("fifth state:")
    print("""    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""")
    print("sixth state:")
    print("""    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""")
    print("seventh state:")
    print("""    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |""")
if __name__ == '__main__':
    openingScreen()
    guessAletter()
