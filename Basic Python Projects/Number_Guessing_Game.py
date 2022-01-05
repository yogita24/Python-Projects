import random
import os 
def Number_guessing_game(level):
    actual=random.randint(0,100)
    endgame=False
    fault=0
    if level=="easy":
        turn=10
        print("Level:Easy\nTotal Attempts:10\n")
    elif level=="medium":
        turn=7 
        print("Level:Medium\nTotal Attempts:7\n")
    elif level=="hard":
        turn=5
        print("Level:Hard\nTotal Attempts:5\n")
    else:
        print("Kindly select level as:(Easy/Medium/Hard)")
        return
    while not endgame:
        if fault<turn:
            try:
                guess=int(input("Guess the number"))
                if guess== actual:
                    print(f"\nCongratulations!!You win.\nTotal chances consumed {fault} out of {turn}.")
                    endgame=True
                elif guess>actual:
                    print("Your guess is greater than actual number.\nYou have {} attempts to guess the number\n".format(turn-fault-1))
                    fault+=1
                elif guess<actual:
                    print("Your guess is lower than actual number.\nYou have {} attempts to guess the number\n".format(turn-fault-1))
                    #print("Ypur guess is lower than actual number")
                    fault+=1
            except:
                choice=input("Please type integer values. :(.\n Do want to continue the same game?(Yes/No)")
                if choice=="No":
                    endgame=True
        else:
            endgame=True
            print(f"You lose,No more turns left\nActual Number:{actual}")
Play=True
while Play:
    os.system('cls')
    print("\nWelcome to Number Guessing Game")
    level=input("\nEnter the Difficulty level: (Easy/Medium/Hard)").lower()
    Number_guessing_game(level)
    Play=(input("\nDo you want to play again?(Yes/No)").lower()=="yes")
print("\nThankyou for playing")




