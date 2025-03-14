import random  # Importing random module for generating random numbers and choices

def guess_number():
    """Guess the number game where the user tries to guess a randomly chosen number."""
    number_to_guess = random.randint(1, 100)  # Generates a random number between 1 and 100
    attempts = 0  # Counter for attempts
    
    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))  # Taking user input
            attempts += 1
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")  # Hint if the guess is too low
            elif user_guess > number_to_guess:
                print("Too high! Try again.")  # Hint if the guess is too high
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")  # Correct guess
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")  # Handles non-integer inputs

def rock_paper_scissors():
    """Rock Paper Scissors game where user plays against a computer."""
    choices = ["rock", "paper", "scissors"]  # Possible choices
    
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()  # Taking user input
        if user_choice == "exit":
            break  # Exit the game
        
        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")  # Validate input
            continue
        
        computer_choice = random.choice(choices)  # Random choice for computer
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")  # Case when both choose the same
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")  # Winning conditions
        else:
            print("You lose!")  # Losing conditions

def main():
    """Main menu to select and play games."""
    while True:
        print("\nSelect a function (1-3):")
        print("1. Guess Number game")
        print("2. Rock Paper Scissors game")
        print("3. Exit program")
        
        choice = input("Enter your choice: ")  # Taking user choice
        
        if choice == "1":
            guess_number()
        elif choice == "2":
            rock_paper_scissors()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break  # Exit the program
        else:
            print("Invalid choice! Please select 1, 2, or 3.")  # Handles invalid input

if __name__ == "__main__":
    main()  # Run the program
