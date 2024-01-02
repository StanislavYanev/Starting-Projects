import random

computer_number = random.randint(1, 100)

while True:
    player_number = input("Guess the number(1 - 100) :")
    if player_number.isdigit():
        if int(player_number) == computer_number:
            print("You guess it !")
            break
        elif int(player_number) < computer_number:
            print("Too Low !")
        elif int(player_number) > computer_number:
            print("Too High")
    else:
        print("Invalid input. Try again")