import random #import random

words = ('lemon', 'kiwi', 'apple', 'cherry', 'date') #5 random word
random_word = random.choice(words)

guess = input("Choose from the following: 'lemon', 'kiwi', 'apple', 'cherry', 'date'. \n")

if random_word == guess:
    print("You won! The random word was: ", random_word)
else:
    print("Sorry, you'r guess is wrong. The random word was: ", random_word)