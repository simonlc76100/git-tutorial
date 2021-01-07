#! /usr/bin/python3

# The random package is needed to choose a random number
import random
 
# Define the game in a function
def guess_loop():
    # This is the number the user will have to guess, chosen randomly in between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    print("Welcome to the guessing game, please enter a number that matches the difficulty:\n1: Novice\n2: Normal\n3: Expert\n4: Hardcore\n5: only 1 shot!\n")
    
    # loop with try, except, else to manage invalid input
    while True:
        try:
            # difficulty settings
            difficulty = int(input())
            count = 1
            limit = 0
            if difficulty == 1:
                limit = 20
            elif difficulty == 2:
                limit = 10
            elif difficulty == 3:
                limit = 5
            elif difficulty == 4:
                limit = 3
            else:
                limit = 1
            
            # condition to check if user enter a valid difficulty number
            if 1 <= difficulty <= 5:
                break
            else:
                print("Please, choose a valid number !")
                continue
            
        except ValueError as err:
            print("Invalid input, please enter an integer")
        else:
            break
        
    if difficulty==5:
        print("\nI have in mind a number in between 1 and 100, can you find it?\nYou only have 1 guess available")
    else:
        print("\nI have in mind a number in between 1 and 100, can you find it?\nYou have", limit ,"guesses available")
 
    # Replay the question until the user finds the correct number or reaches the limit
    while True:
        try:
            # Read the number the user inputs
            guess = int(input())
            
            # condition to check if user enter a number between 1 and 100
            if 1 <= guess <= 100:
                # condition in case difficulty is set to 5, the user has only 1 guess available so there is no point of telling him/her if the number is higher/lower 
                if difficulty==5:
                    count=0
                    # if the user find the correct number, exit the game
                    if guess==number_to_guess:
                        print("\nYou just found the number, it was indeed", guess ,"and it took you 1 guess to succeed!")
                        return
                    else:
                        # if the user reaches the limit, warn him/her of his/her failure and exit the game
                        print("\nNoob ! You failed to find the number ! It was", number_to_guess ,"!")
                        return
                else:
                    if count==limit and guess != number_to_guess:
                        print("\nNoob ! You failed to find the number ! It was", number_to_guess ,"!")
                        return
                    if guess > number_to_guess:
                        print("The number to guess is lower")
                    elif guess < number_to_guess:
                        print("The number to guess is higher")
                    else:
                        # condition in case the user find the number in only one guess when he/she has multiple guesses
                        if count==1:
                            print("\nYou just found the number, it was indeed", guess ,"and it took you 1 guess to succeed!")
                            return
                        # condition in case the user uses more than one guess to find the correct number
                        else:
                            print("\nYou just found the number, it was indeed", guess ,"and it took you", count ,"guesses to succeed!")
                            return
                        
                # increase counter by 1 at the end of each loop iteration    
                count=count+1
            # in case the user didn't chose a number between 1 and 100, warn him/her and go at the beginning of the loop
            else:
                print("Please, choose a valid number !")
                continue
        # A ValueError is raised by the int() function if the user inputs something else than a number
        except ValueError as err:
            print("Invalid input, please enter an integer")
 
# Launch the game
guess_loop()
