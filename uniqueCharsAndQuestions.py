def questions(report):
    # Is the password different from the user’s other passwords?
    user_input_1 = input("Is your password different from your other passwords? Reply with Y/N: ")
    
    while user_input_1.upper() != "Y" and user_input_1.upper() != "N":
        user_input_1 = input("Reply with Y/N: ")

    if user_input_1.upper() == 'N':
        report.append("Pick a password unique from your other passwords.")
        
    # Is the password easy for the user to remember but difficult for others to guess?
    user_input_2 = input("Is your password easy for you to remember and difficult for others to guess? Reply with Y/N: ")
    
    while user_input_2.upper() != "Y" and user_input_2.upper() != "N":
        user_input_2 = input("Reply with Y/N: ")

    if user_input_2.upper() == 'N':
        report.append("Pick a password that is harder for others to guess.")

    # Is the password the user’s last name + year of birth?
    user_input_3 = input("Does your password include your name and/or date of birth? Reply with Y/N: ")
    while user_input_3.upper() != "Y" and user_input_3.upper() != "N":
        user_input_3 = input("Reply with Y/N: ")

    if user_input_3.upper() == 'Y':
        report.append("Pick a different password that does not include your name, date of birth, or any other personal information.")

    user_inputs = [user_input_1.upper(), user_input_2.upper(), user_input_3.upper()]
    return user_inputs, report

# Check if the user uses two or more of the same characters in a row
def sameChar(password, report):
    i = 0
    while i+1 < len(password):
        if password[i] == password[i+1]:
            report.append("Your password uses repeated characters in a row. Pick a stronger password.")
            return True
        else:
            i += 1
    return False

# Print report
def analyzePassword(same, user_inputs, report):
    report_dict = {
        "Password uses unique characters in a row": "Pass" if same == False else "Fail",
        "Unique password": "Pass" if user_inputs[0] == 'Y' else "Fail",
        "Password is difficult to guess": "Pass" if user_inputs[1] == 'Y' else "Fail",
        "Password does not include personal information": "Pass" if user_inputs[2] == 'N' else "Fail"
    }

    print("========================")
    print("Password Analysis Report")
    print("========================")
    for check, result in report_dict.items():
        print(f"{check}: {result}")
    print("========================")

    print("Recommendations")
    print("========================")
    if report:
        for report in report:
            print(report)
    else:
        print("You have a strong password.")
    print("========================")

def main() :
    password = input("Enter password: ")
    report = []
    same = sameChar(password, report)
    analyzePassword(same, *questions(report))

if __name__ == "__main__":
    main()
