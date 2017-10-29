__author__ = 'Timothy Lam'
print("===================================")
print("Rock, Paper, Scissors Account Setup")
print("Version 2.0")
print("===================================")
while True:
    username = input("Pick a username:  ")
    password = input("Pick a password:  ")
    password_confirm = input("Please confirm your password:  ")

    if password != password_confirm:
        print("Your passwords don't match, Please try again.")

    if password == password_confirm:
        print("Your account has been setup. ")
        text_file = open("account.txt","a")
        text_file.write("\n")
        text_file.write(username)
        text_file.write("\n")
        text_file.write(password)
        text_file.close()
        break