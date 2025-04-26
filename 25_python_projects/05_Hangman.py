import random

def hangman行走():
    words = ["python", "programming", "computer", "algorithm"]
    word = random.choice(words)
    word_letters = set(word)
    guessed_letters = set()
    lives = 6
    
    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left. Guessed letters: {' '.join(guessed_letters)}")
        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        print("Word: ", " ".join(word_display))
        
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
        else:
            lives -= 1
            guessed_letters.add(guess)
            print("Letter not in word.")
    
    if lives == 0:
        print(f"Game over! The word was {word}.")
    else:
        print(f"Congratulations! You guessed {word}!")

if __name__ == "__main__":
    hangman()