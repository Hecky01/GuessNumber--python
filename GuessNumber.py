import random

print("Hello! Please enter a number 1-100 so computer will try to guess it!")
Usernumber = input("\nMy number is: ")
print(f"\nSirously you gave computer a number and except that I will guess it? It's {Usernumber}")
print("\nNow you will guess my number!")


def ComputerTurn():
    ComputerNumber = random.randint(1,100) 
    guessCount = 0
    UserGuess = 0
    while UserGuess != ComputerNumber:
        guessCount += 1
        UserGuess = int(input("\nWhat is your guess?"))
        print("\nIt was incorrect, try again")
        if (ComputerNumber > UserGuess):
            print("\nMy number is higher")
        else:
            print("\nMy number is lower")
    
    print(f"\nCongrats! My number was {ComputerNumber}")
    print(f"\nYour guess number: {guessCount}")
    input("Please hit Enter to close app...")
ComputerTurn()


