import random

def rock_paper_scissors_game():
    """
    Plays a Rock-Paper-Scissors game between the user and the computer.
    
    The user is prompted to enter 'rock', 'paper', or 'scissors'.
    The computer randomly chooses one of the three options.
    The winner is determined based on the standard rules of the game.
    The game continues until the user decides to quit by entering 'quit'.
    """
    
    choices = ['rock', 'paper', 'scissors']
    print("Welcome to the Rock-Paper-Scissors game!")
    print("Type 'rock', 'paper', or 'scissors' to play, or type 'quit' to exit.")

    while True:
        # Get user input
        user_choice = input("Enter your choice: ").lower()

        # Check if the user wants to quit
        if user_choice == 'quit':
            print("Thanks for playing! Goodbye!")
            break

        # Validate user input
        if user_choice not in choices:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        # Computer's random choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
        else:
            print("You lose!")

# Run the game
rock_paper_scissors_game()
