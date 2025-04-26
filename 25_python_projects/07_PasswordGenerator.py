import random
import string

def password_generator():
    num_passwords = int(input("How many passwords do you want? "))
    length = int(input("Enter password length: "))
    
    characters = string.ascii_letters + string.digits + string.punctuation
    passwords = []
    
    for _ in range(num_passwords):
        password = ''.join(random.choice(characters) for _ in range(length))
        passwords.append(password)
    
    print("\nGenerated Passwords:")
    for i, pwd in enumerate(passwords, 1):
        print(f"Password {i}: {pwd}")

if __name__ == "__main__":
    password_generator()