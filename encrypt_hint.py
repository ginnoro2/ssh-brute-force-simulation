import string
import random
import json

def create_substitution_key():
    """Create a substitution cipher key mapping"""
    alphabet = list(string.ascii_uppercase)
    shuffled = alphabet.copy()
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))

def encrypt_message(message: str, key: dict) -> str:
    """Encrypt a message using the substitution cipher"""
    encrypted = ""
    for char in message.upper():
        if char in key:
            encrypted += key[char]
        else:
            encrypted += char
    return encrypted

def main():
    # The password we want to encrypt
    password = "MANGO"
    
    # Create the substitution key
    key = create_substitution_key()
    
    # Encrypt the password
    encrypted = encrypt_message(password, key)
    
    # Save the key for verification (in real scenario, this would be kept secret)
    with open("original_key.json", "w") as f:
        json.dump(key, f, indent=4)
    
    # Save the encrypted hint
    with open("encrypted_hint.txt", "w") as f:
        f.write(encrypted)
    
    print(f"Original password: {password}")
    print(f"Encrypted hint: {encrypted}")
    print("Substitution key saved to 'original_key.json'")
    print("Encrypted hint saved to 'encrypted_hint.txt'")

if __name__ == "__main__":
    main() 