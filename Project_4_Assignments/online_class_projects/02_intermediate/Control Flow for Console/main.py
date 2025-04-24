import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    score = 0

    for round_num in range(NUM_ROUNDS):
        print(f"Round {round_num + 1}")
        your_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print("Your number is", your_number)
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

        # Extension 1: validate input
        while guess not in ["higher", "lower"]:
            guess = input("Please enter either higher or lower: ").lower()

        if (guess == "higher" and your_number > computer_number) or \
           (guess == "lower" and your_number < computer_number):
            print("You were right! The computer's number was", computer_number)
            score += 1
        else:
            print("Aww, that's incorrect. The computer's number was", computer_number)

        print("Your score is now", score)
        print()

    print("Thanks for playing!")
    print("Your final score is", score)

    # Extension 2: final performance message
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
