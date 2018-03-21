'''
    Hangman Game, now it a persistent leaderboard
'''
# standard lib module imports
import json
import os
import random
import time

# the hangman images list
HANGMANPICS = [
    '''
+---+
|   |
    |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

+---+
|   |
O   |
/|  |
    |
    |
=========''', '''

+---+
|   |
O   |
/|\ |
    |
    | 
=========''', '''

+---+
|   |
O   |
/|\ |
/   |
    |
=========''', '''

+---+
|   |
O   |
/|\ |
/ \ |
    |
========='''
]

# creating list of potential choices by splitting on a space.
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split(' ')


def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()  # hack: print('\n')
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def display_highscores():
    global game_stats    
    if os.path.exists('./high_scores.txt'):
        game_stats = json.load(open('high_scores.txt'))
    print('---- HIGH SCORES ----')
    for stat in game_stats:
        print('---- **** ----')
        for key, value in stat.items():    
            print('{}  {}'.format(key, value))
        print('---- **** ----')
    print('---- ---------- ----\n\n')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

game_stats = []
display_highscores()
name = input("Who is playing: ")
start_time = time.time()
while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(
                'Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters,
                         secretWord)
            print('You have run out of guesses!\nAfter ' +
                  str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) +
                  ' correct guesses, the word was "' + str(len(correctLetters)) + '"')
            gameIsDone = True

    elapsed_time = time.time() - start_time
    percentage_correct = len(correctLetters)/len(secretWord)     
    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        stat = {}  # create a dictionary to contain the game stats
        stat['name'] = name
        stat['time_taken'] = elapsed_time
        stat['percentage'] = percentage_correct
        game_stats.append(stat)
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
            # save game_stats in high_scores.txt
            with open('high_scores.txt', 'w') as outfile:
                json.dump(game_stats, outfile)
            display_highscores()
        else:
            # save game_stats in high_scores.txt
            with open('high_scores.txt', 'w') as outfile:
                json.dump(game_stats, outfile)
            display_highscores()
            break
