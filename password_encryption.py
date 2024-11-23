import random
import string
from cryptography.fernet import Fernet





#TASK 6
# function to generate a strong password of a given length
def generate_password(length=15):
    # make string of all possible characters for a password
    ascii_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + "@"
    
    # generate password using random.choice to chose random ascii characters
    password = ''.join(random.choice(ascii_characters) for _ in range(length))
    
    return password

#TASK 8
# create function to encrypt and decrypt password

# generate a kay for encryption and decryption (should only be done once)
def generate_key():
    return Fernet.generate_key()

# save the key to a file for future use
def save_key(key, filename='secret.key'):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

# retrieve the key
def load_key(filename='secret.key'):
    with open(filename, 'rb') as key_file:
        return key_file.read()

# encrypt the password uusing the fernet and the key
def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

# decrypt the password in the same way but in reverse
def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password



def main():
    # generate a password of length 15
    password = generate_password(15)
    print("Generated Password: ", password)

    
    # generate and save key
    key = generate_key()
    save_key(key)

    # get key again (for show purposes)
    key = load_key()

    # input password
    password = input("Enter a password to encrypt: ")
    
    # encrypt password and print out result
    encrypted_password = encrypt_password(password, key)
    print(f"Encrypted password: {encrypted_password}")

    # decrypt password and print out result
    decrypted_password = decrypt_password(encrypted_password, key)
    print(f"Decrypted password: {decrypted_password}")
    
# Example usage
if __name__ == "__main__":
    main()