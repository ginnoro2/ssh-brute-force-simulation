import string
import itertools
import random

def generate_substitution_key():
    """Generate a random substitution cipher key"""
    alphabet = list(string.ascii_lowercase + string.digits)
    substituted = alphabet.copy()
    random.shuffle(substituted)
    return dict(zip(alphabet, substituted))

def encrypt_text(text: str, key: dict) -> str:
    """Encrypt text using the substitution cipher"""
    encrypted = ""
    for char in text.lower():
        if char in key:
            encrypted += key[char]
        else:
            encrypted += char
    return encrypted

def generate_possible_passwords(target_password="mango"):
    """Generate possible password combinations"""
    chars = string.ascii_lowercase + string.digits
    with open("possible_passwords.txt", "w") as f:
        f.write(f"{target_password}\n")
        for _ in range(100):
            key = generate_substitution_key()
            encrypted = encrypt_text(target_password, key)
            f.write(f"{encrypted}\n")
        for _ in range(900):
            length = len(target_password)
            password = "".join(random.choices(chars, k=length))
            f.write(f"{password}\n")
    print(f"Generated passwords have been saved to possible_passwords.txt")

if __name__ == "__main__":
    generate_possible_passwords()
