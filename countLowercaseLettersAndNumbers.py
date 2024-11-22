# See if password has at least one lowercase letter and count lowercase letters in password
# See if password has at least one number and count numbers in password

lowercaseLetters = 0
numbers = 0

password = input("Please enter the password you wish to analyze:")

for x in password:
    if x.islower():
        lowercaseLetters += 1
    if x.isnumeric():
        numbers += 1

if(lowercaseLetters == 1):
    print("Your pasword contains ", lowercaseLetters, " lowercase letter.")
else:
    print("Your pasword contains ", lowercaseLetters, " lowercase letters.")

if lowercaseLetters > 0:
    print("Your password contains at least one lowercase letter.")
else:
    print("You should add lowercase letters to your password.")

# I counted a number as a digit 0-9, so for example if the password is 25 it would contain 2 numbers
if(numbers == 1):
    print("Your password contains ", numbers, " number.")
else:
    print("Your password contains ", numbers, " numbers.") 

if numbers > 0:
    print("Your password contains at least one number.")
else:
    print("You should add numbers to your password.")