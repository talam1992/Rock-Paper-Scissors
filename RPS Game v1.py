__author__ = 'Timothy Lam'
print("Version 1.0")
print("Made by Timothy Lam")
loose = ("The computer wins")
win = ("You win")
lives = 5
score = 0
drew = 0
computer_lives = 7

while True:
    print("To begin fill in the below information.")
    username = input("Please enter your username:  ")
    password = input("Please enter your password:  ")
    searchfile = open("account.csv", "r")
    for line in searchfile:
        if username and password in line:
            print("Access Granted")
            print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("     ___                  ______________     ______________     _______________     ____      ___")
            print("    ¦   ¦                ¦              ¦   ¦              ¦   ¦               ¦   ¦    ¦    /   /")
            print(" /------------------     ¦     ___      ¦   ¦  __________  ¦   ¦  _____________¦   ¦    ¦   /   /")
            print("/            \     ¦     ¦    ¦   ¦     ¦   ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦  /   /")
            print("¦       ------------     ¦    ¦___¦   __¦   ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦_/   /")
            print("¦       ------------     ¦           \      ¦ ¦          ¦ ¦   ¦ ¦                 ¦         /")
            print("¦            \     ¦     ¦    ¦\      \     ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦\   \  ")
            print("¦       ------------     ¦    ¦ \      \    ¦ ¦__________¦ ¦   ¦ ¦_____________    ¦    ¦ \   \ ")
            print("¦       ------------     ¦    ¦  \      \   ¦              ¦   ¦               ¦   ¦    ¦  \   \                   ___  ___  ___  ___")
            print("¦            \     ¦     ¦____¦   \______\  ¦______________¦   ¦_______________¦   ¦____¦   \___\                 ¦   ¦¦   ¦¦   ¦¦   ¦")
            print("¦       ------------                                                                                          ___ ¦   ¦¦   ¦¦   ¦¦   ¦")
            print("\       ------------ ___________     _______________     ___________     ___________     _____________       ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦")
            print(" \           \     /¦   _____   ¦   ¦     _____     ¦   ¦   _____   ¦   ¦           ¦   ¦             ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦")
            print("  \---------------/ ¦  ¦     ¦  ¦   ¦    ¦_____¦    ¦   ¦  ¦     ¦  ¦   ¦    _______¦   ¦     ___     ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦")
            print("                    ¦  ¦_____¦  ¦   ¦     _____     ¦   ¦  ¦_____¦  ¦   ¦   ¦           ¦    ¦   ¦    ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦")
            print("                    ¦    _______¦   ¦    ¦     ¦    ¦   ¦    _______¦   ¦   ¦_____      ¦    ¦___¦   _¦      \                       /")
            print("                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦    _____¦     ¦           \         \                     /")
            print("                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦   ¦_______    ¦    ¦\      \         \                   /")
            print("                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦           ¦   ¦    ¦ \      \         \                 /                                _____")
            print("                    ¦___¦           ¦____¦     ¦____¦   ¦___¦           ¦___________¦   ¦____¦  \______\         \_______________/                                /     /")
            print("                                                                                                                                                          /     /")
            print(" ______________     _______________     ____     ______________     ______________     ______________     _____________     ______________               /     /")
            print("¦   ___________¦   ¦               ¦   ¦    ¦   ¦   ___________¦   ¦   ___________¦   ¦              ¦   ¦             ¦   ¦   ___________¦    ________ /     /")
            print("¦  ¦               ¦  _____________¦   ¦    ¦   ¦  ¦               ¦  ¦               ¦  __________  ¦   ¦     ___     ¦   ¦  ¦               /        /     /")
            print("¦  ¦___________    ¦ ¦                 ¦    ¦   ¦  ¦___________    ¦  ¦___________    ¦ ¦          ¦ ¦   ¦    ¦   ¦    ¦   ¦  ¦___________   ¦        /     /")
            print("¦____________  ¦   ¦ ¦                 ¦    ¦   ¦____________  ¦   ¦____________  ¦   ¦ ¦          ¦ ¦   ¦    ¦___¦   _¦   ¦____________  ¦  ¦       /     /")
            print("             ¦ ¦   ¦ ¦                 ¦    ¦                ¦ ¦                ¦ ¦   ¦ ¦          ¦ ¦   ¦           \                  ¦ ¦  ¦               __________________")
            print("             ¦ ¦   ¦ ¦_____________    ¦    ¦                ¦ ¦                ¦ ¦   ¦ ¦__________¦ ¦   ¦    ¦\      \                 ¦ ¦  ¦                                 ¦")
            print(" ____________¦ ¦   ¦               ¦   ¦    ¦    ____________¦ ¦    ____________¦ ¦   ¦              ¦   ¦    ¦ \      \    ____________¦ ¦  ¦               __________________¦")
            print("¦______________¦   ¦_______________¦   ¦____¦   ¦______________¦   ¦______________¦   ¦______________¦   ¦____¦  \______\  ¦______________¦  ¦______________¦")

            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
            print("Live Rules")
            print("You start with 5 lives.")
            print("If you win you get a extra live.")
            print("If you loose you loose a live.")
            print("If you draw the lives stay the same.")
            print("-----------------------------------------")
            print("To see a list of rules type rules.")
            print("-----------------------------------------")
            print("At any point type exit to leave the game.")
            print("-----------------------------------------")
            print("The computer has lives aswell.")
            print("Can you beat the computer?")
            print("Good Luck!!")
            print("-----------------------------------------")
            while True:
                rps = input("Rock, Paper, Scissors?   ")
                import random
                computer = ("rock", "paper", "scissors")
                computer = random.choice(computer)
                #rock if statements
                if rps == "rock" and computer == "paper":
                    print("The computer choose", computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives = -1
                if rps == "rock" and computer == "scissors":
                    print("The computer choose", computer)
                    print("")
                    print(win)
                    print("")
                    print("")
                    score += 1
                #paper if statements
                if rps == "paper" and computer == "rock":
                    print("The computer choose", computer)
                    print("")
                    print(win)
                    print("")
                    print("")
                    score += 1
                if rps == "paper" and computer == "scissors":
                    print("The computer choose", computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives = -1
                #scissors if statements
                if rps == "scissors" and computer == "paper":
                    print("The computer choose", computer)
                    print("")
                    print(win)
                    print("")
                    print("")
                    score += 1
                if rps == "scissors" and computer == "rock":
                    print("The computer choose", computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives = -1
                #duplicate
                if rps == "rock" and computer == "rock":
                    print("The computer choose", computer)
                    print("")
                    print("You Drew")
                    print("")
                    print("")
                    drew += 1
                if rps == "paper" and computer == "paper":
                    print("The computer choose", computer)
                    print("")
                    print("You Drew")
                    print("")
                    print("")
                    drew += 1
                if rps == "scissors" and computer == "scissors":
                    print("The computer choose", computer)
                    print("")
                    print("You Drew")
                    print("")
                    print("")
                    drew += 1
                #system
                if rps == "rules":
                    print("**********************************************")
                    print("Rules")
                    print("**********************************************")
                    print("-Rock looses against Paper")
                    print("-Rock beats Scissors")
                    print("-Paper beats Rock")
                    print("-Paper looses against Scissors")
                    print("-Scissors beats Paper")
                    print("-Scissors looses against Rock")
                    print("**********************************************")
                if rps == "display lives":
                    print(lives)
                if rps == "display score":
                    print(score)
                if rps == "display drew":
                    print(drew)
                #lives
                if lives == 0 or rps == "test":
                    print("Thanks for playing.")
                    print("You have ran out of lives")
                    print("You got", score, "correct")
                    print("You drew", drew, "times")
                    stop = input("Press enter to exit")
                    import time
                    time.sleep(900)
                if computer_lives == 0:
                    print("Thanks for playing")
                    print("The computer lost all it's lives. You Win.")
                    print("The computer got", score, "correct")
                    print("The computer drew", drew, "times")
                    import time
                    time.sleep(900)
                #exit
                if rps == "exit":
                    break
        else:
            print("Your username or password is incorrect.")
            print("---------------------------------------")