import wordHandler

#Add possible word lists:
difficultyOptions = ["standard", "hard"]

while True:
    valid = False
    #Set difficulty
    while not valid:
        print("Choose a difficulty:")
        for i in difficultyOptions:
            print(i)
        userVal = input("> ")
        if userVal in difficultyOptions:
            difficulty = userVal
            valid = True
        else:
            print("Invalid input, please try again.")
            print()
    #Generate new word
    word = wordHandler.chooseWord(difficulty)
    print(word)




    #Ask to exit when done
    valid = False
    while not valid:
        print("Try again? (y/n)")
        userVal = input("> ")
        if userVal == "n" or userVal == "y":
            valid = True
        else:
            print("Invalid input, please try again.")
            print()
    if userVal == "n":
        break
