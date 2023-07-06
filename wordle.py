"""
Create Wordle

* Load a txt file containing 5 letter words | Complete
* Pick one of those words                   | Complete
* Set up board in Console                   
* Allow the player to guess a word
* System shall verify that the guessed word is 5 letters long
*       If not, ask the user to guess another word
* Letters turn orange if the correct word contains that letter but it is not in the right spot
* Letters turn green if the correct word contains that letter and it is in the right spot
* Letter remain white if the correct word does not contain that letter.

* The Player will only have 6 chances to guess the word
*       If the Player guesses the word correctly, all letters will turn green and the game will end
*       If the Player does not guess the correct word within 6 guesses, the correct word will be displayed

List of words taken from : https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93#file-valid-wordle-words-txt
"""
import random
from rich import print


print("Game is starting")
 #create a function to get a random word
def random_word(fName):
    words=open(fName).read().splitlines()
    return random.choice(words)
#Create a class to store players guess
class Wordle:
    def __init__(self):
        self.word=random_word("words.txt")
        self.num_guesses=0
        self.guess_dict={ #This stores each guess as a character array
            0:[" "]*5,
            1:[" "]*5,
            2:[" "]*5,
            3:[" "]*5,
            4:[" "]*5,
            5:[" "]*5
        }

    def draw_board(self):
        for guess in self.guess_dict.values(): #We want to access the strings inside of the guess array
            print(" | ".join(guess)) #this puts the | in between each value
            print("==================")

    def get_user_input(self): #Get the user to input their guess for a max of 6 guesses
        user_guess=input("Enter a five letter word: ")
        while len(user_guess) != 5:
            user_guess=input("NOT VALID! Enter a five letter word: ")

        #lowercase guess
        user_guess=user_guess.lower()

        for idx, char in enumerate(user_guess): #enumerate gives index and value
            if(char in self.word):
                if(char==self.word[idx]): #char in guess is in the word at the correct position
                    char=f"[green]{char}[/]" #green
                else: #char in guess is in the word at the wrong position
                    char=f"[yellow]{char}[/]" #yellow

            #insert the guess into the dictionary 
            self.guess_dict[self.num_guesses][idx]=char
        self.num_guesses += 1
    def play(self): #Play the game
        while(True):
            self.draw_board()
            user_guess=self.get_user_input()

            if(user_guess==self.word):
                self.draw_board()
                print(f"You Won! The word was {self.word}.")
                break
            if(self.num_guesses>5):
                self.draw_board()
                print(f"You Lost. The word was {self.word}.")
                break

game=Wordle()
game.play()