import random

def guess_n():
    print("  ###  Welcome to Guess the Number  ### ")
    print("       Give a number between 0-15    ", end='\n')

    # Set the num to guess
    secret_n = random.randint(0, 15)
    print(secret_n)

    # Set the num of guess
    try_n = 5

    # Loop until chance run out
    for i in range(1, try_n + 1):

        ans = int(input("What is your guess"))
        
        if secret_n == ans:
            print(f"Congrats, the answer was {secret_n}")
            break
    

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
