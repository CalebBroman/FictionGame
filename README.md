This is a little personal project where I'm just building a game based on the board game Fiction.
Same as in fiction, the game is basically the same as wordle, except in each set of clues, there is always one that is false.
For now, the computer is going to choose the word, and do all of the clues randomly. At some point, I may try to implement different 
strategies for the computer to make the game more interesting.
I may also maake it so the player chooses the word/clues, and the computer makes guesses at the word, but that's probably much further off.
\
\
For now, I have some basic functionality implemented. 
The player gets to choose whether they want a standard or hard game.
\
Standard -> No repeat letters in the word
\
Hard -> Repeat letters are allowed, but not guarunteed.
\
The computer then chooses a word, gives the player one letter from it, and then prompts the player to start making guesses.
For each of the guesses the player makes, the computer will return clues for letter, exactly one of them always being a lie.
\
X -> The letter is not included in the word.
\
~ -> The letter is included in the word, but in a different position.
\
V -> The letter is in the correct position.
\
As of now, the player can keep making guesses forever until they get the word. The only restriction right now is that you have to enter 5 letters.
I haven't yet implemented anything keeping the player from repeating words or just a non-word. 
At the end, all of the players guesses will be presented with the given sets of clues and a string showing which clue was a lie.
\
T -> Correct clue
\
F -> Incorrect clue
\
\
\
I'll probably keep working on this every now and then.
