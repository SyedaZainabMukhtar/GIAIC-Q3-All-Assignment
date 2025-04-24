import random

def main():
    # Secret number between 1 and 99
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")

    # Get user's first guess
    guess = int(input("Enter a guess: "))

    # Keep asking until the guess is correct
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        print()  # Empty line for better formatting
        guess = int(input("Enter a new guess: "))  # Ask for a new guess
    
    print(f"Congrats! The number was: {secret_number}")

if __name__ == '__main__':
    main()
