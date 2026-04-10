import random

options = ("lady", "tiger", "hunter")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (lady, tiger, hunter): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "hunter" and computer == "tiger":
        print("You win!")
    elif player == "lady" and computer == "hunter":
        print("You win!")
    elif player == "tiger" and computer == "lady":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")