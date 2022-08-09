print("Welcome to the 'Fine the Treasure'!")
print("Your task is to find a treasure\n")

direction = input("Do you want to go left or right?\n")

if direction == "left":
    lakeAction = input("You come to a lake, you see an island across. Type 'swim' to swim or 'wait' for a boat.\n")

    if lakeAction == "wait":
        doorChoice = input("There are 3 doors: red, blue, and yellow. What door do you want to go through?\n")

        if doorChoice == "yellow":
            print("You win!")
        else:
            print("Wrong door, you loose!")
    else:
        print("You drowned.")
else:
    print("You died.")


