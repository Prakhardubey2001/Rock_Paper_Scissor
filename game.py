# """
# 1 Input from user (rock, paper or scissor)
# 2 Computer will choose one of the three options (rock, paper or scissor) randomly.
# 3 Print Result
# Cases :
# A-ROCK
#  VS ROCK : TIE 
#  ROCK VS PAPER : PAPER WIN
#  ROCK VS SCISSOR : ROCK WIN

# B-PAPER
# VS PAPER : TIE
# PAPER VS ROCK : PAPER WIN
# PAPER VS SCISSOR : SCISSOR WIN

# C-SCISSOR
# VS SCISSOR : TIE
# SCISSOR VS ROCK : ROCK WIN
# SCISSOR VS PAPER : SCISSOR WIN 

# """

import random

item_list = ['rock', 'paper', 'scissor']

while True:
    user_choice = input('Enter your choice: rock, paper, or scissor = ').lower()

    if user_choice not in item_list:
        print("Wrong choice! Please choose between rock, paper, and scissor.")
    else:
        break  

comp_choice = random.choice(item_list)
print(f"You chose {user_choice}, and the computer chose {comp_choice}")

if user_choice == comp_choice:
    print('TIE GAME!!')
elif user_choice == 'rock':
    if comp_choice == 'paper':
        print("Computer won!!")
    else:
        print('You won!!!')
elif user_choice == 'paper':
    if comp_choice == 'scissor':
        print("Computer won!!")
    else:
        print('YOU WIN!!')
elif user_choice == 'scissor':
    if comp_choice == 'rock':
        print("Computer Won!!")
    else:
        print("You won!!")
