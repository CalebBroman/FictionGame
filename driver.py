import random
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
        print()
        userVal = input("> ")
        if userVal in difficultyOptions:
            difficulty = userVal
            valid = True
        else:
            print("Invalid input, please try again.")
            print()
    #Get random word
    word = wordHandler.chooseWord(difficulty)
    #Give random letter
    rVal = random.random()
    print("Included letter: " + word[int(rVal * 5)])

    #User guesses and clues back
    guesses = []
    usedWords = []
    while True:
        userVal = ""
        #Get the user's guess
        valid = False
        while not valid:
            print("Please enter a 5 letter word as a guess:")
            print()
            userVal = input("> ")
            print()
            if not (len(userVal) == 5 and userVal.isalpha()):
                print("Invalid input, please try again.")
                print()
            elif userVal.casefold() in usedWords:
                print("Word already guessed, please enter a different word.")
                print()
            else:
                valid = True
        userGuess = userVal.casefold()
        #check if user is correct
        if userGuess != word:
            #get correct set of clues:
            trueClues = wordHandler.trueClues(word, userGuess)
            actualClues = wordHandler.clueStrategy(trueClues)
            guesses.append((userGuess, actualClues[0], actualClues[1]))
            usedWords.append(userGuess)
            print("Your Guess: " + userGuess)
            print("Clues:      " + actualClues[0])
            print()
            print()
        else:
            print("Correct!")
            print()
            break
    print("Guess overview:")
    print("Total guesses: " + str(len(guesses) + 1))
    print()
    for i in range(len(guesses)):
        truthStr = "TTTTT"
        truthStr = truthStr[:guesses[i][2]] + 'F' + truthStr[guesses[i][2]+1:]
        print()
        print("Guess: " + guesses[i][0])
        print("Clues: " + guesses[i][1])
        print("Truth: " + truthStr)

    #Ask to exit when done
    valid = False
    print()
    while not valid:
        print("Play again? (y/n)")
        userVal = input("> ")
        if userVal == "n" or userVal == "y":
            valid = True
        else:
            print("Invalid input, please try again.")
            print()
    if userVal == "n":
        break
