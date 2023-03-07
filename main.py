#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo, goodbye
from os import system
import random

print(logo)


def difficulty_level_selector():
    x = input(
        "\nSelect a difficulty level: Type 'h' for hard, 'e' for easy(by default it'll be easy): "
    ).lower()
    if x == 'h':
        y = 5
    else:
        y = 10
    return y


def random_number_selector():
    random_num = random.randint(1, 100)
    return random_num


def compare(n, nr):
    if n > 100:
        return False, "Above range! (range = [1, 100].)"
    elif n < 1:
        return False, "Below range! (range = [1, 100].)"
    elif n == nr:
        return True, "You got it!"
    elif n > nr:
        return False, "Too High!"
    elif n < nr:
        return False, "Too Low!"
    else:
        return True, "There's a bug!"


def play_higher_lower():
    print(
        "Welcome, Welcome, Welcome.\nThis is the game of Higher-Lower, and I'm your dost: Shashank Sharma.\nI'm selecting a random number between 1 and 100 that you've to guess."
    )
    y = difficulty_level_selector()
    print(f"You've {y} number of attempts.")
    nr = random_number_selector()
    print(f"Psst! The answer is: {nr}.")

    while (y > 0):
        n = int(input("\nGuess a number: "))
        is_over, result = compare(n, nr)
        print(result)
        y -= 1
        print(f"Remaining attempts: {y}.")
        if is_over:
            print("\nYou WIN!")
            break

    if not is_over:
        print(f"\nYou Lose, The secret number was: {nr}.\n")


while input(
        "Wanna play a game of Higher-Lower? Type 'y' to play, 'n' to stop: "
).lower() == 'y':
    system('clear')
    play_higher_lower()
system('clear')
print(goodbye)
