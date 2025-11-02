import random

def show_instructions():
    print("=" * 40)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess number in as few attempts as possible.")
    print("=" * 40)

def get_difficulty():
    while True:
        choice = input("Choose difficulty (easy/medium/hard): ").lower()
        if choice == "easy":
            return 10
        elif choice == "medium":
            return 7
        elif choice == "hard":
            return 5
        else:
            print("Invalid choice. Please enter easy, medium, or hard.")

def play_game():
    show_instructions()
    number = random.randint(1, 100)
    attempts = get_difficulty()
    guesses = []

    while attempts > 0:
        print(f"\nAttempts remaining: {attempts}")
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer!")
            continue

        guesses.append(guess)
        if guess == number:
            print(f"🎉 Congratulations! You guessed it in {len(guesses)} tries.")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
        attempts -= 1

        if attempts == 0:
            print(f"😞 Out of attempts! The number was {number}.")

    print("\nYour guesses:", guesses)
    play_again = input("Play again? (y/n): ").lower()
    if play_again == "y":
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
