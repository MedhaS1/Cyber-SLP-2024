from flask import Flask, render_template, request
import random
import string
from cryptography.fernet import Fernet

app = Flask(__name__)

# Val's
def countUpperCase(password):
    length = len(password)
    min_length = length >= 12
    capital_letters = sum(1 for char in password if char.isupper())
    has_capital_letter = capital_letters > 0

    countUpperCaseReport = []

    countUpperCaseReport.append(f"Password length: {length} characters")
    countUpperCaseReport.append(f"Contains capital letters: {capital_letters}")
    if min_length and has_capital_letter:
        countUpperCaseReport.append("Your password is strong enough when compared to our requirements.")
    else:
        countUpperCaseReport.append("Your password is weak when compared to our requirements.")

    return countUpperCaseReport

# Sara's
def countLowerCase(password):
    lowercaseLetters = 0
    numbers = 0

    for x in password:
        if x.islower():
            lowercaseLetters += 1
        if x.isnumeric():
            numbers += 1

    lowercaseLettersReport = []

    if(lowercaseLetters == 1):
        lowercaseLettersReport.append(f"Your password contains {lowercaseLetters} lowercase letter.")
    else:
        lowercaseLettersReport.append(f"Your password contains {lowercaseLetters} lowercase letters.")

    if lowercaseLetters > 0:
        lowercaseLettersReport.append("Your password contains at least one lowercase letter.")
    else:
        lowercaseLettersReport.append("You should add lowercase letters to your password.")

    # I counted a number as a digit 0-9, so for example if the password is 25 it would contain 2 numbers
    if(numbers == 1):
        lowercaseLettersReport.append(f"Your password contains {numbers} number.")
    else:
        lowercaseLettersReport.append(f"Your password contains {numbers} numbers.") 

    if numbers > 0:
        lowercaseLettersReport.append("Your password contains at least one number.")
    else:
        lowercaseLettersReport.append("You should add numbers to your password.")

    return lowercaseLettersReport

# Ashley's
# passwordEncryption
#TASK 6
# function to generate a strong password of a given length
def generate_password(length=15):
    # make string of all possible characters for a password
    ascii_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + "@" + '!'+ '@'+ '#'+ '$'+ '%'+ '^'+ '&'+ '*'+ '('+ ')'+ '_'+ '-'+ '.'
    
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


def passwordEncryption(password):
    # generate a password of length 15
    password = generate_password(15)
    print("Generated Password: ", password)

    # generate and save key
    key = generate_key()
    save_key(key)

    # get key again (for show purposes)
    key = load_key()
    
    # encrypt and decrypt password and print out result
    encrypted_password = encrypt_password(password, key)
    decrypted_password = decrypt_password(encrypted_password, key)
    encryption = []
    encryption.append(encrypted_password)
    encryption.append(decrypted_password)

    return encryption
    # print(f"Encrypted password: {encrypted_password}")
    # print(f"Decrypted password: {decrypted_password}")

# Josie's
def countspecialcharacters(user_password):
    sp_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '.'] #list of special characters that will be counted
    count = 0 #how many special characters counted

    for char in user_password: #iterate each character in password
        if char in sp_char_list: #checks if the character matches the list of special characters
            count +=1 #increments each match

    return count

def questions(user_input_1, user_input_2, user_input_3, report):
    if user_input_1 == 'N':
        report.append("Pick a password unique from your other passwords.")
    if user_input_2 == 'N':
        report.append("Pick a password that is harder for others to guess.")
    if user_input_3 == 'Y':
        report.append("Pick a different password that does not include your name, date of birth, or personal info.")
    return report

def sameChar(password, report):
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            report.append("Your password uses repeated characters in a row. Pick a stronger password.")
            return True
    return False

@app.route("/", methods=["GET", "POST"])
def analyze():
    report = []
    if request.method == "POST":
        # get the inputs
        password = request.form["password"]
        user_input_1 = request.form["unique"]
        user_input_2 = request.form["guessable"]
        user_input_3 = request.form["personal"]

        # analyze password
        same = sameChar(password, report)
        report = questions(user_input_1, user_input_2, user_input_3, report)

        count = countspecialcharacters(password)

        encryption_list = passwordEncryption(password)
        encrypted_password = encryption_list[0]
        decrypted_password = encryption_list[1]

        lowercaseLetters_report = countLowerCase(password)

        uppercaseLetters_report = countUpperCase(password)
        
        # create a dictionary
        report_dict = {
            "Password uses unique characters in a row": "Pass" if not same else "Fail",
            "Unique password": "Pass" if user_input_1.upper() == 'Y' else "Fail",
            "Password is difficult to guess": "Pass" if user_input_2.upper() == 'Y' else "Fail",
            "Password does not include personal information": "Pass" if user_input_3.upper() == 'N' else "Fail"
        }

        return render_template("report.html", report_dict=report_dict, recommendations=report, count=count, encrypted_password=encrypted_password, decrypted_password=decrypted_password, lowercaseLetters_report=lowercaseLetters_report, uppercaseLetters_report=uppercaseLetters_report)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)