import random

options = ["rock", "paper", "scissor"]
running = True

while running:
    computer = random.choice(options)
    player = input("Enter a choice: (rock, paper, scissor): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a Tie!!")
    elif player == "scissor" and computer == "paper":
        print("You win!!")
    elif player == "rock" and computer == "scissor":
        print("You win!!")
    elif player == "paper" and computer == "rock":
        print("You win!!")
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")