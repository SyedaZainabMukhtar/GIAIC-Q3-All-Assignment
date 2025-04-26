import random

def guess_number_user():
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    guesses = 0
    
    while True:
        guess = int(input("Enter your guess: "))
        guesses += 1
        
        if guess == number:
            print(f"Correct! You guessed it in {guesses} tries!")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

if __name__ == "__main__":
    guess_number_user()