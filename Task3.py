import random
import string

def generate_random_password(length):
    characters = string.ascii_uppercase + string.digits + '@_!#$%^&*'
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_strong_password(length):
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    choice = input("Enter 'r' for random password or 's' for strong password: ").lower()
    length = int(input("Enter the desired length of the password: "))
    
    if choice == 'r':
        password = generate_random_password(length)
    elif choice == 's':
        password = generate_strong_password(length)
    else:
        print("Invalid choice! Please enter 'r' or 's'.")

    print("Generated Password:", password)

if __name__ == "__main__":
    main()


