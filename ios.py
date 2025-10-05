import itertools
import time
import os

def brute_force_attack(target_password):
    characters = '0123456789'
    attempts = 0

    for password in itertools.product(characters, repeat=len(target_password)):
        attempts += 1
        current_password = ''.join(password)
        print(f'Trying password: {current_password}')
        
        if current_password == target_password:
            print(f'Password unlocked: {current_password}')
            print(f'Total attempts: {attempts}')
            return current_password
        
        time.sleep(0.1)  # Simulate time delay for each attempt

    print('Password not found.')
    return None

if __name__ == "__main__":
    os.system('figlet Toxic Dev')
    target_password = input("Enter the target password (0-9): ")
    brute_force_attack(target_password)
