import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = rock, paper, scissors

userChoice = int(input("Type 0 for rock, 1 for paper, 2 for scissors: "))
print(choices[userChoice])

print("Computer Chooses:\n")
compChoice = random.randint(-1, len(choices))
print(choices[compChoice])

# loosing conditions
if userChoice == 0 and compChoice == 1:           # rock vs paper
    print("You loose!")
elif userChoice == 1 and compChoice == 2:         # paper vs scissors
    print("You loose!")
elif userChoice == 2 and compChoice == 0:         # scissors vs rock
    print("You loose!")

# checking if its a draw
elif userChoice == 0 and compChoice == 0:
    print("Its a draw!")
elif userChoice == 1 and compChoice == 1:
    print("Its a draw!")
elif userChoice == 2 and compChoice == 2:
    print("Its a draw!")

else:
    print("You win!")