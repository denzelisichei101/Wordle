
print("Checking your code is named a2.py in the same directory as this file!")
import a2
print("OK")

print("Checking your code contains the WordleWords class!")
from a2 import WordleWords
print("OK")

print("Checking I can instantiate the WordleWords class!")
words = WordleWords(5)
print("OK")

print("Checking I can load the words.txt file!")
words.load_file("words.txt")
print("OK")

print("Checking WordleWords check_word method!")
words.check_word("MOOSE")
print("OK")

print("Checking your code contains the TooShortError class!")
from a2 import TooShortError
print("OK")

print("Checking your code contains the TooLongError class!")
from a2 import TooLongError
print("OK")

print("Checking your code contains the NotLettersError class!")
from a2 import NotLettersError
print("OK")

print("Checking WordleWords check_word rejects short words!")
try:
    words.check_word("MODE")
except TooShortError:
    print("OK")
else:
    assert False

print("Checking WordleWords check_word rejects long words!")
try:
    words.check_word("MODELS")
except TooLongError:
    print("OK")
else:
    assert False

print("Checking WordleWords check_word rejects not letters!")
try:
    words.check_word("M00SE")
except NotLettersError:
    print("OK")
else:
    assert False

print("Checking WordleWords add ...")
words.add("XXXXX")
print("OK")

print("Checking WordleWords contains ...")
assert "XXXXX" in words
assert "MOOSE" in words
assert "NOISE" in words
print("OK")

FIVE_LETTER_WORDS = 15830

print("Checking WordleWords iter ...")
count = 0
for word in words:
    assert word in words
    count += 1
assert count == FIVE_LETTER_WORDS
print("OK")

print("Checking WordleWords len ...")
assert len(words) == FIVE_LETTER_WORDS
print("OK")

print("Checking WordleWords words are unique ...")
found = set()
for word in words:
    assert word not in found
    found.add(word)
assert len(found) == FIVE_LETTER_WORDS
print("OK")

print("Checking WordleWords words are CAPTIALIZED ...")
for word in words:
    for byte in word.encode():
        assert byte >= ord("A") and byte <= ord("Z")
print("OK")

print("Checking WordleWords copy ...")
copy_found = set()
words_copy = words.copy()
for word in words_copy:
    assert word not in copy_found
    copy_found.add(word)
assert found == copy_found
print("OK")

print("Checking WordleWords discard ...")
for word in words:
    words_copy.remove(word)
assert len(words_copy) == 0
assert len(words) == FIVE_LETTER_WORDS
print("OK")

print("Checking WordleWords base class ...")
from collections.abc import MutableSet
assert isinstance(words, MutableSet)
print("OK")

print("Checking your code contains the Guess class!")
from a2 import Guess
print("OK")

print("Checking I can instantiate Guess class!")
guess = Guess("MOOSE", "BONUS")
print("OK")

print("Checking Guess.correct()")
assert Guess("MOOSE", "BONUS").correct() == "_O___"
assert Guess("MOOSE", "BOONS").correct() == "_OO__"
assert Guess("YOYOS", "BOONS").correct() == "_O__S"
assert Guess("YOYOS", "BONUS").correct() == "_O__S"
assert Guess("BONUS", "BONUS").correct() == "BONUS"
print("OK")

print("Checking Guess.misplaced()")
assert Guess("MOOSE", "BONUS").misplaced() == "S"
assert Guess("MOOSE", "BOONS").misplaced() == "S"
assert Guess("YOYOS", "BOONS").misplaced() == "O"
assert Guess("YOYOS", "BONUS").misplaced() == ""
assert Guess("BONUS", "BONUS").misplaced() == ""
print("OK")

print("Checking Guess.wrong()")
assert Guess("MOOSE", "BONUS").wrong() == "EMO"
assert Guess("MOOSE", "BOONS").wrong() == "EM"
assert Guess("YOYOS", "BOONS").wrong() == "YY"
assert Guess("YOYOS", "BONUS").wrong() == "OYY"
assert Guess("BONUS", "BONUS").wrong() == ""
print("OK")


print("Checking Guess.correct()")
assert Guess("MOOSE", "BONUS").correct() == "_O___"
assert Guess("MOOSE", "BOONS").correct() == "_OO__"
assert Guess("YOYOS", "BOONS").correct() == "_O__S"
assert Guess("YOYOS", "BONUS").correct() == "_O__S"
assert Guess("BONUS", "BONUS").correct() == "BONUS"
print("OK")

print("Checking Guess.misplaced()")
assert Guess("MOOSE", "BONUS").misplaced() == "S"
assert Guess("MOOSE", "BOONS").misplaced() == "S"
assert Guess("YOYOS", "BOONS").misplaced() == "O"
assert Guess("YOYOS", "BONUS").misplaced() == ""
assert Guess("BONUS", "BONUS").misplaced() == ""
print("OK")

print("Checking Guess.guess()")
assert Guess("MOOSE", "BONUS").guess() == "MOOSE"
assert Guess("MOOSE", "BOONS").guess() == "MOOSE"
assert Guess("YOYOS", "BOONS").guess() == "YOYOS"
assert Guess("YOYOS", "BONUS").guess() == "YOYOS"
assert Guess("BONUS", "BONUS").guess() == "BONUS"
print("OK")

print("Checking Guess.is_win()")
assert Guess("MOOSE", "BONUS").is_win() == False
assert Guess("MOOSE", "BOONS").is_win() == False
assert Guess("YOYOS", "BOONS").is_win() == False
assert Guess("YOYOS", "BONUS").is_win() == False
assert Guess("BONUS", "BONUS").is_win() == True
print("OK")

print("Checking your code contains the Wordle class!")
from a2 import Wordle
print("OK")

print("Checking I can instantiate Wordle class!")
wordle = Wordle(words)
print("OK")

print("Checking I can Wordle.guess()")
guess = wordle.guess("NOISE")
assert isinstance(guess, Guess)
assert guess.guess() == "NOISE"
print("OK")

print("Checking I can Wordle.guesses()")
assert wordle.guesses() == 1
print("OK")

print("Checking I can Wordle.guess()")
guess = wordle.guess("CRIES")
assert isinstance(guess, Guess)
assert guess.guess() == "CRIES"
print("OK")

print("Checking I can Wordle.guesses()")
assert wordle.guesses() == 2
print("OK")

print("ALL OK")

