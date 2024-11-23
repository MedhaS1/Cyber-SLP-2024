def password_analyzer(password):
    length = len(password)
    min_length = length >= 12
    capital_letters = sum(1 for char in password if char.isupper())
    has_capital_letter = capital_letters > 0

    report = f"Password length: {length} characters\n"
    report += f"Contains capital letters: {capital_letters}\n"
    report += "Password is strong enough" if min_length and has_capital_letter else "Password is weak"

    return report

password = input("Enter your password: ")
print(password_analyzer(password))