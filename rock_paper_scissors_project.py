import random

print("Rock, Paper, Scissors !!!")

action = ["rock", "paper", "scissors"]


def computer_choice():
    return random.choice(action)


while True:
    user_choice = input("Enter rock, paper, scissors (or 'q' to quit): ")

    computer_c = computer_choice()

    print(f"User choose {user_choice}, computer choose {computer_c}")

    if user_choice == computer_c:
        print("Draw")
    elif (
        user_choice == "rock"
        and computer_c == "paper"
        or user_choice == "scissors"
        and computer_c == "rock"
        or user_choice == "paper"
        and computer_c == "scissors"
    ):
        print("Computer win")
    elif user_choice == "q":
        print("Exit game, Goodbye !!!")
        break
    elif user_choice not in action:
        print("Invalid choice")
    else:
        print("User win")
