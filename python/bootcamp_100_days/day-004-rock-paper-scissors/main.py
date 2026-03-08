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

list_choice = [rock, paper, scissors]

user_choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper, 2 for Scissors"))

if user_choice == 0:
    print()
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)

computer_choice = random.randint(0,2)

print("Computer chose : \n", list_choice[computer_choice])

if computer_choice == 0 and user_choice == 1 :
    print("You win")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice == 1 and user_choice == 2:
    print("You win")
elif computer_choice == 1 and user_choice == 0:
    print("You lose")
elif computer_choice == 2 and user_choice == 0:
    print("You win")
elif computer_choice == 2 and user_choice == 1:
    print("You lose")
elif computer_choice == user_choice:
    print("It's a draw")