import random as ran

def roll_dice():
    while True:
        die1 = ran.randint(1,6)
        die2 = ran.randint(1,6)
        total = die1 + die2


        print("Die 1:",die1)
        print("Die 2:",die2)
        print("Dice Total:",total)
        print()
        
        if total != 7 and total != 11:
            print("You win!")
            input("Press Enter to roll again.....")
        else:
            print("Sorry, you rolled craps!")
            return
        

def main():
    print("Let's play some craps!")
    print("------------------------")
    print()
    input("Hit Enter to play!")

    choice = "y"

    while choice == "y":
        roll_dice()
        choice = input("Do you want to play again? y/n ")

        if choice != "y":
            break
    print("Thanks for donating!!!")

if __name__ == "__main__":
    main()
