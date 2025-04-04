#----------------------------------------------------
# Assignment 2: Wordle
# Author: Denzel Isichei
# Collaborators/references: None
#----------------------------------------------------
from random import choice
from collections.abc import MutableSet
class TooShortError(ValueError):
    def __init__(self, message="Word is too short."):
        '''Initializes a TooShortError instance.'''
        self.message = message
        super().__init__(self.message)

class TooLongError(ValueError):
    def __init__(self, message="Word is too long."):
        '''Initializes a TooLongError instance.'''
        self.message = message
        super().__init__(self.message)

class NotLettersError(ValueError):
    def __init__(self, message="Word contains non-capital letters."):
        '''Initializes a NotLettersError instance.'''
        self.message = message
        super().__init__(self.message)

class WordleWords(MutableSet):
    def __init__(self, letters):
        '''This function initializes an empty set of words'''
        self._words = set()
        self._letters = letters

    def __contains__(self, word):
        '''This function returns True if the word is in the set, returns False otherwise.'''
        return word in self._words

    def __iter__(self):
        '''This function returns an iterator over all the words in the set.'''
        return iter(self._words)

    def __len__(self):
        '''This function returns the number of words in the set.'''
        return len(self._words)

    def add(self, word):
        '''This function add the word to the set. Raises an error if the word is too short, or too long, or does not contain only capital letters A-Z.'''
        self.check_word(word)
        self._words.add(word)

    def discard(self, word):
        '''This function removes a word from the set.'''
        self._words.discard(word)

    def load_file(self, filename):
        '''This function adds words to the set using the content of the file specified by the filename.'''
        file = open(filename, 'r') 
        # Iterate over each line in the file
        for line in file:
            # Extract the word from the line, remove leading/trailing spaces, and convert to uppercase
            word = line.strip().upper()
            # Check if the length of the word matches the required number of letters
            if len(word) == self.letters():
                # Add the valid word to the set using the add method
                self.add(word)
        file.close()


    def check_word(self, word):
        '''This function takes a word and makes sure that it consists only of the capital letters A-Z (no accents) and is the correct length.'''
        if len(word) < self._letters: # Check if the length of the word is less than the required number of letters
            raise TooShortError(f'The word "{word}" is too short.')
        elif len(word) > self._letters: # Check if the length of the word is greater than the required number of letters
            raise TooLongError(f'The word "{word}" is too long.')
        elif not word.isalpha() or not word.isupper(): # Check if the word contains non-alphabetic or non-uppercase characters
            raise NotLettersError(f'The word "{word}" contains non-capital letters.')

    def letters(self):
        '''This function returns the number of letters in every word.'''
        return self._letters

    def copy(self):
        '''This function returns a second WordleWords instance that contains the same words.'''
        new_instance = WordleWords(self._letters) # Create a new instance of WordleWords with the same number of letters
        new_instance._words = self._words.copy() # Copy the set of words from the current instance to the new instance
        return new_instance

class Guess:
    def __init__(self, guess, answer):
        '''This function initialize the Guess object with the player's guess and the correct answer.'''
        self._guess = guess
        self._answer = answer

    def guess(self):
        '''This function returns the guess that the player made.'''
        return self._guess

    def correct(self):
        '''This function returns a string with underscores for incorrect guesses and correct letters.'''
        result = ''
        for char, correct in zip(self._guess, self._answer): # Iterate over pairs of characters from the guessed word and the correct answer
            result += char if char == correct else '_'
        return result

    def misplaced(self):
        '''This function returns a sorted string containing misplaced letters in the guess.'''
        # Initialize an empty list to store misplaced letters
        misplacedLetters = []

        # Save length of words to loop through guess and answer
        lengthOfWords = len(self._answer)

        # Iterate through each character in the guess and its corresponding position in the answer
        for x in range(lengthOfWords): # Loop through answer letters
            for y in range(lengthOfWords): # Loop through guess letters
                if self._answer[x] == self._guess[y]:
                    if self._answer[x] == self._guess[x]:
                        break
                    else:
                        if x != y:
                            if self._guess[y] not in misplacedLetters:
                                misplacedLetters.append(self._guess[y])

        # Sort the list of misplaced letters and join them into a string
        sortedMisplacedLetters = ''.join(sorted(misplacedLetters))

        # Return the sorted string of misplaced letters
        return sortedMisplacedLetters


    def wrong(self):
        '''This function returns a sorted string containing wrong letters in the guess.'''
        # Create list to store Wrong Letters
        wrongLetters = []

        # Convert guess and answer to lists
        userGuess = list(self._guess)
        answer = list(self._answer)

        # Loop through guess list
        for i in range(len(userGuess)):
            # Loop through answer list
            for j in range(len(answer)):
                if userGuess[i] == answer[j]:
                    answer.pop(j)
                    break
                elif (j == len(answer) - 1):
                    wrongLetters.append(userGuess[i])
                    

        # Sort the list of incorrect letters 
        sortedIncorrectLetters = sorted(wrongLetters)

        # Join the sorted incorrect letters into a string
        sortedIncorrectLettersString = ''.join(sortedIncorrectLetters)

        # Return the sorted string of incorrect letters
        return sortedIncorrectLettersString

    def is_win(self):
        '''This function returns True if the guess is the same as the answer.'''
        return self._guess == self._answer
    
class Wordle:
    def __init__(self, words):
        '''This function should take one parameter, which is a WordleWords instance object. It should choose a random word for the game.'''
        self._wordle_words = words
        self._target_word = choice(list(words))  # Convert the set to a list before using choice
        self._guess_count = 0

    def guesses(self):
        '''This function should return the number of guesses the player has made so far.'''
        return self._guess_count

    def guess(self, guessed):
        '''This fuction should take a string guessed and return a Guess instance object that represents the results of the guess.'''
        self._guess_count += 1      # Increment the guess count
        return Guess(guessed, self._target_word)
