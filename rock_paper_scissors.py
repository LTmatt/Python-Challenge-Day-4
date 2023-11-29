# Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game_list = [rock,paper,scissors]

players_choice = int(input("Choose 0 for Rock, 1 for Paper, 2 for Scissors\n"))
if players_choice >= 3 or players_choice < 0:
    print("Invalid choice, you Lose!")
else:
    print(game_list[players_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose: ")
    print(game_list[computer_choice])

    
    if players_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and players_choice == 2:
        print("You Lose!")
    elif computer_choice > players_choice:
        print("You Lose!")
    elif players_choice > computer_choice:
        print("You Win!")
    elif players_choice == computer_choice:
        print("It's a draw")


