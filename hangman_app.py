"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""


def get_word_so_far(word):
    word_so_far = '-' * len(word)
    return word_so_far


def generate_random_word():
   return "cat"


def play_hangman():
   """ this is the python script version of the game """
   print("The hangman app is under construction. Try again later!")


if __name__ == '__main__':
    play_hangman()
