import random

def generate_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock-Paper-Scissors!")

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors) or 'exit' to quit: ").lower()

        if user_choice == "exit":
            print("Thanks for playing!")
            break
        elif user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose again.")
            continue

        computer_choice = generate_computer_choice()
        print(f"Computer chooses: {computer_choice}")

        print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    main()
