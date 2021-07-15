import random

choices = ["rock", "paper", "scissors"]
computer = None
player = None
playing = True


def make_choice():
    global computer, player
    computer = None
    player = None
    computer = random.choice(choices)
    while player not in choices:
        player = input("rock, paper or scissors? ").lower()


while True:
    playing = True
    while playing:
        make_choice()
        print(f"computer: {computer}")
        print(f"player: {player}")

        if computer == "rock":
            if player == "rock":
                print("rechoice")
                # make_choice()
            elif player == "paper":
                print("player wins")
                playing = False
            else:
                print("computer wins")
                playing = False
        elif computer == "paper":
            if player == "rock":
                print("computer wins")
                playing = False
            elif player == "paper":
                print("rechoice")
                # make_choice()
            else:
                print("player wins")
                playing = False
        else:
            if player == "rock":
                print("player wins")
                playing = False
            elif player == "paper":
                print("computer wins")
                playing = False
            else:
                print("rechoice")
                # make_choice()
    play_again = input("Retry (y/n) ? ").lower()
    if play_again != 'y':
        break
