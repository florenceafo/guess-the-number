# Number guessing game

import random
print("Let's play a guessing game!\n")
r = random.randint(1, 9)


x = 1

while x < 3:
    guess = int(input("Guess a number between 1 and 9:\n"))
    if guess == r:
        print("Correct!\n")
        break
    elif guess > r:
        print("oops, too high!\nHave another guess:\n")
    elif guess < r:
        print("oops, too low!\nHave another guess:\n")
    x = x+1

while x >= 3:
    guess = int(input("One more chance:\n"))
    if guess == r:
        print("Correct!\n")
        break
    if guess != r:
        print("Bad luck, the correct number was", r)
        break
