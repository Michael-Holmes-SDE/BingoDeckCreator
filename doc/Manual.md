# Bingo! User Manual  	         	  

**TODO: Write instructions that a non-technical end-user can understand and follow without going into detail about the inner workings of the program.**


## Running The Program
1. Open a new command prompt window
2. Type in 'cd cs1440-assn4', or 'cd ' and whatever folder the program is in, and press [ENTER]
3. Type in 'python src/bingo.py' and press [ENTER] to start the program

## Menu And Functionality
1. All inputs are case-insensitive. You can use upper or lower case, depending on your preference.
2. If at any time you want to exit the program, type in 'X' and press [ENTER] until the program closes
3. On the Main Menu there should be two options to choose from. Select which option you want to do by typing in the letter that comes before the closing paranthese on the same line as the option you want (for example, you see 'C) Create a new deck' and if you want to create a new deck, type in 'C' and press [ENTER]).
4. There should be a prompt asking you to enter how big you want the Bingo card to be. Enter a whole number between and including 3 & 16, then press [ENTER].
5. A new prompt should show up asking you to enter the maximum number you want your Bingo cards to be able to have. Enter a whole number between the values shown to you and press [ENTER].
6. A prompt asking how many cards you want in your deck should come up. Enter a whole number of how many cards you want between and including 2 and 8192, then press [ENTER].
7. You should see a Deck menu with 4 options to choose from. You can display a card on the screen by entering 'P', display every card in the deck to the screen by entering 'D', save the deck of Bingo cards to a file of your choice by entering 'S', or go back to the Main menu by entering 'X'. 
8. When saving the deck of Bingo cards to a file, simply enter the name of the file you want it to be saved to, without quotation marks. If the file already exists, the deck will be added to the end of the file. If the file doesn't already exist, it will create a file with that name and save the deck to the file.
9. If at any time you make a mistake, like entering a different number of bingo cards than you want, follow the prompts until the Deck menu comes up, then press 'X' and hit [ENTER] to return to the Main menu.

## Common Errors and How to Fix Them
1. If the program says that your input is invalid, check the prompt it gives you to see what input is valid.
2. If Step 2 in 'Running The Program' fails, the program is in a different folder. If this is the case, navigate to your file explorer and search for the folder the program is in and use 'cd {Name of Folder}' and press [ENTER].
 

