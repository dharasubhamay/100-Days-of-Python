"""
Official Rules:

* Rock wins against scissors.
* Scissors win against paper.
* Paper wins against rock.
"""
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
print("What do you want to choose")
choice = int(input("Type 0 for Rock\nType 1 for Paper\nType 2 for scissirs.. "))

if(choice > 2 or choice < 0):
  print("Wrong input\nGame Over")
else:
  if(choice == 0):
    msg = rock
  elif(choice == 1):
    msg = paper
  elif(choice == 2):
    msg = scissors

  print("Your Choice : " + msg)

  comchoice = random.randint(0, 2)
  print("Computer's Choice : ")
  if(comchoice == 0):
    print(rock)
  elif(comchoice == 1):
    print(paper)
  elif(comchoice == 2):
    print(scissors)

  if(choice == comchoice):
    res = "It's Draw"
  elif(choice == 0 and comchoice == 2):
    res = "You Win!"
  elif(choice == 2 and comchoice == 1):
    res = "You Win!"
  elif(choice == 1 and comchoice == 0):
    res = "You Win!"
  else:
    res = "You Lose!"

  print("Result : " + res)