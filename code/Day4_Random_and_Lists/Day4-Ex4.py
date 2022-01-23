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

#Write your code below this line 👇
import random
game_images = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
computer_coice = random.randint(0, 2)

winners = ["02", "21", "10"]

if choice < len(game_images):
    print(game_images[choice])
else:
    print("Invalid number.")
    quit()

print("Computer chose:")
print(game_images[computer_coice])

game = choice + computer_coice
if game in winners:
    print("You Win!")
elif choice == computer_coice:
    print("Its a draw.")
    print("Remember: Rock wins againts Scissors, Scissors wins againts Paper and Paper wins againts Rock")
else:
    print("You lose")
    print("Remember: Rock wins againts Scissors, Scissors wins againts Paper and Paper wins againts Rock")
