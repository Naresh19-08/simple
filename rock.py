import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def main():
    user_wins = 0
    computer_wins = 0

    while True:
        user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

        if user_input == "q":
            break
        
        if user_input not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please type Rock, Paper, Scissors, or Q to quit.")
            continue

        computer_choice = get_computer_choice()
        print("Computer picked", computer_choice + ".")

        if user_input == computer_choice:
            print("It's a draw!")
        elif user_input == "rock":
            if computer_choice == "scissors":
                print("You won!")
                user_wins += 1
            else:
                print("You lost!")
                computer_wins += 1
        elif user_input == "paper":
            if computer_choice == "rock":
                print("You won!")
                user_wins += 1
            else:
                print("You lost!")
                computer_wins += 1
        elif user_input == "scissors":
            if computer_choice == "paper":
                print("You won!")
                user_wins += 1
            else:
                print("You lost!")
                computer_wins += 1

    print("You won", user_wins, "times.")
    print("The computer won", computer_wins, "times.")
    print("Goodbye!")

if __name__ == "__main__":
    main()
