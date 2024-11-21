class Special_char():
    def countspecialcharacters(self):
        print('Here are valid special characters to include in your password: !, @, #, $, %, ^, &, *, (, ), _, -, .')
        user_password = input('Enter Password:') #user inputs password
        sp_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '.'] #list of special characters that will be counted
        count = 0 #how many special characters counted

        for char in user_password: #iterate each character in password
            if char in sp_char_list: #checks if the character matches the list of special characters
                count +=1 #increments each match

        print(f"Number of Special Characters:", count) #prints the count

special_char_counter = Special_char()
special_char_counter.countspecialcharacters() #calls method
