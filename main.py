import random

def openingScreen():
        print("Welcome to the game Hangman")
        print("""      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/""")
        amount_of_lives = random.randint(5,10)
        print(amount_of_lives)

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
