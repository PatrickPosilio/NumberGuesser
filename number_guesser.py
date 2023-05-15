# pylint: disable = missing-module-docstring
import random

print("Welcome to the Number guesser!")
print("The purpose is to guess a formulated number until you get it right.")
print("Firstly, you must choose the highest possible number")

top_of_range = input("The highest possible number will be:   ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()


random_number = random.randint(0, top_of_range)
GUESSES = 0


while True:
    GUESSES += 1
    user_guess = input("Take a guess:  ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess <= -1:
            print("Please type a number larger than 0 next time.")
    else:
        print("Please type a number larger than 0 next time.")
        continue
    if user_guess == random_number:
        print("You got it!")
        break
    else:
        if user_guess >= random_number:
            print("Lower!")
        else:
            print("Higher!")

print("You got it in",GUESSES, "guesses")
        