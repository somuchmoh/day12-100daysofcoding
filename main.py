#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from replit import clear
import art

def counter_level():
    player_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    return player_level

def guess_number():
    number = random.randint(1,100)
    level = counter_level()
    if level == 'easy':
        counter = 10 
    elif level == 'hard':
        counter = 5
        
    while counter != 0: 
        guess = int(input("Make a guess: "))
        counter -= 1
        if guess < number:
            print("Too low.")
            print("Guess again.")
            print(f"You have {counter} guesses left.")
        elif guess > number:
            print("Too high.")
            print("Guess again.")
            print(f"You have {counter} guesses left.")
        else:
            print("You guessed the number right!")
            counter = 0 
            play_again = input("Play again? Type 'yes' to restart: ")
            if play_again == 'yes':
                clear()
                guess_number()
    else:
        print(f"You have run out of guesses. The number was {number}")
        play_again = input("Play again? Type 'yes' to restart: ")
        if play_again == 'yes':
            clear()
            guess_number()

print(art.logo)
print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100.")
guess_number()