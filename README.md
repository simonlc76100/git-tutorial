Welcome, my name is Simon Lellouche, I'm a Digital Engineering student at ESILV and the owner of this repository.

Here, you will find different files we were required to add, commit and push from a remote terminal to this online platform in a git learning context. You will also find a bonus file named "guessing_game.py". At first, it was a simple number guessing script given by our teacher and we were asked to add features to it, that's what the following steps will be about.

Cloning the repository to your linux system:

You can clone the repo wherever you want in your system with the command : git clone https://github.com/simonlc76100/git-tutorial

Running the script: 

Make sure that you are in the correct repository "/git-tutorial" and then use this command : ./guessing_game.py

You will be prompted to choose a difficulty that will determine how hard the game will be. You need to enter an integer in between 1 and 5 that matches the correct difficulty:

Enter 1 for Novice, you will have 20 guesses available
Enter 2 for Normal, you will have 10 guesses available
Enter 3 for Expert, you will have 5 guesses available
Enter 4 for Hardcore, you will have 3 guesses available
Enter 5 for Only 1 shot !, beware, you will have only 1 guess available

You will notice that if you enter an incorrect input like a character, it will print a warning message and ask the user to choose again.
Same scenario if you enter an integer that isn't in between 1 and 5.

the guess number it takes for the user to find the correct number is of course saved and displayed in the endgame message.

When entering a number to guess, the user can hit his/her keyboard too fast and make a mistake like typing 533 instead of 53.
If that's the case, a warning message will be printed and the user will be asked to enter an integer in between 1 and 100 again. 
It will have no consequences on the user's available guesses.

If the guess number reaches the limit imposed by the difficulty and the user hasn't found the number yet, he/she will lose and the game will end.

Last but not least, I made one small change that I think can make the difference : You will notice that messages printed in-game are grammatically correct according to every cases possible.
Since the script has a number of guess counter, the code has lines like:

print("\nYou just found the number, it was indeed", guess ,"and it took you", count ,"guesses to succeed !")

guess is the number entered by the user and count, the guess number it took for the user to find the correct number. If the user found the number (e.g. 53) in only 1 guess, the message would have been: 

You just found the number, it was indeed 53 and it took you 1 guesses to succeed !

As you can see that is quite incorrect so I made sure that it can't happen at all =) !

That's all for this short tutorial, I hope that you will succeed in finding the correct number in only 1 guess, after all you have 1% chance to win on the hardest difficulty,
in certain mmorpgs I looted legendary items that had far lower drop rate (e.g. 0.01%) :p