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

options = [rock, paper, scissors]

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
# print(type(player_choice))
if player_choice == "0":
    print(options[0])
elif player_choice == "1":
    print(options[1])
elif player_choice == "2":
    print(options[2])
else:
    print("That's not a option.")

print("Computer chose:")

computer_input = random.randint(0,2)
print(options[computer_input])

computer_input = str(computer_input)

if player_choice == computer_input:
    print("It's a Draw.")
elif player_choice == "0" and computer_input =="2":
    print("You Win!")
elif player_choice == "1" and computer_input == "0":
    print("You Win!")
elif player_choice == "2" and computer_input == "1":
    print("You Win!")
else:
    print("You Lose!")