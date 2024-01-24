import random
import string

def generate_password(length=12, include_special=True, include_uppercase=True, include_numbers=True):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_numbers else ''
    punctuation = string.punctuation if include_special else ''
    
    characters = lowercase_letters + uppercase_letters + digits + punctuation
    
    if not characters:
        characters = string.ascii_letters + string.digits
    
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def generate_and_save_passwords(num_passwords=100000, length=14, include_special=True, include_uppercase=True, include_numbers=True, filename="passwords.txt"):
    with open(filename, 'w') as file:
        for _ in range(num_passwords):
            password = generate_password(length, include_special, include_uppercase, include_numbers)
            file.write(password + '\n')

# Example: Generate 50 passwords and store them in "passwords.txt"
generate_and_save_passwords(num_passwords=100000, length=16, include_special=True, include_uppercase=True, include_numbers=True, filename="passwords.txt")
print("Passwords generated and saved to 'passwords.txt'")
