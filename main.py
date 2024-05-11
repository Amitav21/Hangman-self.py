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

if __name__ == '__main__':
    openingScreen()
