import random

def guess_number_computer():
    print("Think of a number between 1 and 100, and I'll try to guess it!")
    low = 1
    high = 100
    guesses = 0
    
    while True:
        guess = random.randint(low, high)
        guesses += 1
        response = input(f"Is {guess} too high (h), too low (l), or correct (c)? ").lower()
        
        if response == 'c':
            print(f"Yay! I guessed it in {guesses} tries!")
            break
        elif response == 'h':
            high = guess - 1
        elif response == 'l':
            low = guess + 1

if __name__ == "__main__":
    guess_number_computer()