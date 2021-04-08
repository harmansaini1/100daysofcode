#Rock, Paper, Scissors Game
rock = ''''
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

import random

chose_by_user = int(input("What do you chose? Type 0 for Rock, 1 for paper, 2 for scissors."))
print("You Choose:\n")
if chose_by_user == 0:
  print(rock)
elif chose_by_user == 1:
  print(paper)
elif chose_by_user == 2:
  print(scissors)
else:
  print("Choose from 0, 1 and 2!")

random_chose_computer = random.randint(0,2)

print("Computer Choose:\n")
if random_chose_computer == 0:
  print(rock)
elif random_chose_computer == 1:
  print(paper)
elif random_chose_computer == 2:
  print(scissors)
else:
  print()

if (chose_by_user == 0 and random_chose_computer == 0) or (chose_by_user == 1 and random_chose_computer == 1) or (chose_by_user == 2 and random_chose_computer == 2):
  print("Tie")
elif (chose_by_user == 0 and random_chose_computer ==1) or (chose_by_user == 1 and random_chose_computer ==2) or (chose_by_user == 2 and random_chose_computer ==0):
  print("You Lost.")
elif (chose_by_user == 0 and random_chose_computer ==2) or (chose_by_user == 1 and random_chose_computer ==0) or (chose_by_user == 2 and random_chose_computer ==1):
  print("You Win.")
