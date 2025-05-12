import random

def chooseWord(listName):
    #Read word list
    with open(listName + ".txt") as fp:
        wordList = fp.readlines()
    #Choose random word
    rval = random.random()
    word = wordList[int(rval * len(wordList))]
    return word[:-1]


def trueClues(word, guess):
    #Find correct set of clues
    #Clue values:
    #'X' -> letter not in word
    #'~' -> letter in word, but wrong position
    #'V' -> letter in correct position
    clueSet = ""
    for i in range(5):
        if word[i] == guess[i]:
            clueSet += 'V'
        elif word.count(guess[i]) > guess[:i-1].count(guess[i]):
            clueSet += '~'
        else:
            clueSet += 'X'
    return clueSet


def clueStrategy(trueClues):
    #Choose random index
    rval = random.random()
    idx = int(rval * 5)
    #Get the correct clue at that index, convert to number
    if trueClues[idx] == 'X':
        tVal = 0
    elif trueClues[idx] == '~':
        tVal = 1
    else:
        tVal = 2
    #change that value
    rval = random.random()
    tVal = (tVal + int(rval * 2) + 1) % 3
    #Rebuild clue string
    if tVal == 0:
        actualClues = trueClues[:idx] + 'X' + trueClues[idx+1:]
    elif tVal == 1:
        actualClues = trueClues[:idx] + '~' + trueClues[idx+1:]
    else:
        actualClues = trueClues[:idx] + 'V' + trueClues[idx+1:]

    #return the clues and the index that was changed
    return (actualClues, idx)
