import random

def guess_n():
    while True: # do while loop emulate
        max_range = int(input("Choose the number maximum of your range: "))
        if max_range > 1:
            break

    print("  ###  Welcome to Guess the Number  ### ")
    print("         You only have 5 chances        ")
    print(f"     Give a number between 0 and {max_range}    ", end='\n')

    # Set the num to guess
    secret_n = random.randint(0, max_range)
    print(secret_n)

    # Set the num of max guess
    max_guess = 5

    # Loop until chance runs out
    for try_n in range(1, max_guess + 1):

        user_guess = int(input("Guess: "))
        # while True: # Check range
        #     user_guess = int(input("Guess: "))

        #     if (user_guess < max_range) or (user_guess > 0): 
        #         break
        #     else:
        #         print("Number out of range, choose again")
        #         try_n -= 1

        if secret_n == user_guess:
            print(f"Congrats, the answer was {secret_n}")
            break

        if user_guess > secret_n:
            print("Your guess is bigger than the secret number, try again")
        elif user_guess < secret_n:
            print("Your guess is smaller than the secret number, try again")
        
    if try_n == 5:
        print(f"You lost, the answer was {secret_n}")

guess_n()

# CLI game
# Game with 5 tries
# Goal's to discover the number
    #   random number
    #   range > set up difficulty

# After each try the computer give a statement
    #   Win > we found the number
    #   Bigger > our num is lower
    #   Lower > our num is bigger
    #   Loose > we pass the 5th try

# The number we give can be repeated
