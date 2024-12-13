import random

def play_rock_paper_scissors():
    print("\nWelcome to Rock, Paper, Scissors!")
    options = ['rock', 'paper', 'scissors']
    
    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()
        if user_choice == 'quit':
            print("Exiting Rock, Paper, Scissors.")
            break
        if user_choice not in options:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
        else:
            print("You lose!")

def play_number_guessing_game():
    print("\nWelcome to Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = input("Guess a number between 1 and 100 (or 'quit' to exit): ")
            if user_guess.lower() == 'quit':
                print("Exiting Number Guessing Game.")
                break

            user_guess = int(user_guess)
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number or 'quit' to exit.")

def main():
    while True:
        print("\nSelect a game:")
        print("1. Rock, Paper, Scissors")
        print("2. Number Guessing Game")
        print("3. Quit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            play_rock_paper_scissors()
        elif choice == '2':
            play_number_guessing_game()
        elif choice == '3':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
