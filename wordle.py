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
print("Game is starting")

#create a function to get a random word
import random
def random_word(fName):
    words=open(fName).read().splitlines()
    return random.choice(words)

#Create a function to print the board to console
def print_board(guessWord, correctWord):
    line="-----------"
    empty="| | | | | |"
    wordLine=list(empty)

    guessArray=list(guessWord)
    correctArray=list(correctWord)
    if (guessWord == ""):
        #Print the empty board | This should only be called at the start of the game
        for x in range(6):
            print(line)
            print(empty)
        print(line)
    else:
        print()
        """
        * First, check if the guessed word is the correct word
        *       If the words are equal turn the guessed word green, add it to the board, end the game
        * Second, check each letter of the guessed word against the correct word
        *       If the letter is in the word but in the wrong spot, turn it orange
        *       If the letter is in the word and in the correct spot, turn the letter green
        *       If the letter is not in the word, leave it as whie
        """

        #guess=correct
        if (guessWord == correctWord):
            index=1
            for x in range(5):
                wordLine[index]=guessArray[x]
                index=index+2
        print("".join(wordLine))
    return

print(random_word("words.txt"))   
print_board("","hello")
print_board("hello","hello")
