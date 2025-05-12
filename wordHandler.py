import random

def chooseWord(listName):
    with open(listName + ".txt") as fp:
        wordList = fp.readlines()
    rval = random.random()
    word = wordList[int(rval * len(wordList))]
    return word
