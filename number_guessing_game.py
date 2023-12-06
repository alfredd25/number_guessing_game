import random

def game():
    print("Welcome to number guessing game")
    print("I'm thinking of a number between 1-100")
    level_difficulty = input("Want to play 'easy' or 'hard:")
    if level_difficulty.lower() == 'easy':
        easy_level()
    elif level_difficulty.lower() == 'hard':
        hard_level()

            

def easy_level():
    ACTUAL_NUMBER = random.randint(1,100)
    lives = 10
    print("You have 10 lives")
    while lives != 0:
        for i in range (0,lives):
            user_guess = int(input("Enter your guess:"))
            if user_guess != ACTUAL_NUMBER and user_guess < ACTUAL_NUMBER:
                print("Incorrect guess")
                print("Guess higher")
                lives-=1
                print(f"You have {lives} lives remaining")
            elif user_guess != ACTUAL_NUMBER and user_guess > ACTUAL_NUMBER:
                print("Incorrect guess")
                print("Guess lower")
                lives-=1
                print(f"You have {lives} lives remaining")
                                
            elif user_guess == ACTUAL_NUMBER:
                print("Correct guess")
                print("YOU WIN")
                return
        else:
            print(f"The actual number was {ACTUAL_NUMBER}")
            print("YOU LOST")



def hard_level():
    ACTUAL_NUMBER = random.randint(1,100)
    lives = 5
    print("You have 5 lives")
    while lives != 0:
        for i in range (0,5):
            user_guess = int(input("Enter your guess:"))
            if user_guess != ACTUAL_NUMBER and user_guess < ACTUAL_NUMBER:
                print("Incorrect guess")
                print("Guess higher")
                lives-=1
                print(f"You have {lives} lives remaining")
            elif user_guess != ACTUAL_NUMBER and user_guess > ACTUAL_NUMBER:
                print("Incorrect guess")
                print("Guess lower")
                lives-=1
                print(f"You have {lives} lives remaining")
                                
            else:
                print("Correct guess")
                print("YOU WIN")
                return
        else:
            print(f"The actual number was {ACTUAL_NUMBER}")
            print("YOU LOST")


choice = input("Do you want to play a number guessing game 'y'/'n':")
if choice.lower() == 'y':
    game()



                        


