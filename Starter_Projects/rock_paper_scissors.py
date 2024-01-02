import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Choose [r}ock, [p]aper or [s]cissors : ")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

computer_random_number = random.randint(1, 3)


if computer_random_number == 1:
    computer_random_number = rock
elif computer_random_number == 2:
    computer_random_number = paper
elif computer_random_number == 3:
    computer_random_number = scissors

print(f"The computer chosse {computer_random_number}")

if player_move == rock and computer_random_number == scissors or\
    player_move == scissors and computer_random_number == paper or\
    player_move == paper and computer_random_number == rock:
    print("You win!")
elif player_move == computer_random_number:
    print("Draw!")
else:
    print("You lose!")

