# Software Development Plan

## Phase 0: Requirements Analysis (tag name `analyzed`)
*(20% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [X] Re-write the instructions in your own words.
    *   If you don't do this, you won't know what you're supposed to do!
    *   Don't leave out details!
	1. Thoroughly read all documentation and analyze it
	2. Read the documentation for open() to learn how to open a file in write mode
	3. Read the design documentation from the C++ team and write 250-300 words about it, committed at the design tag or before
	4. Create a UML Class Diagram with a draft in the designed tag and one in the deployed tag
	5. Create a User's manual, one at the designed tag and one at the deployed tag for the end user
	6. Create pseudocode for the functions and classes
	7. Implement those functions into the program
	8. Thoroughly test the code with the tests created by the C++ team, and create 4 tests for the Card class and 2 tests for the Deck class (or more)
	9. Publish the program
*   [X] Explain the problem this program aims to solve.
    *   This program aims to create Bingo cards for customers
    *   A *good* solution looks like:
	1. Has case-insensitive input from prompts to the user(Upper everything inputted)
	2. Crashes when a wrong filename is entered
    	3. Repeats prompts until: for strings, there is a character; for integer, .isdigit() returns true and is within range(prompt should show the range of numbers acceptable)
	4. Show the user what kind of input is expected by the program, including the range of acceptable values
	5. Error messages show the user how to give good input
	6. Use the number of position in the Deck as an identifier for the card there
	7. With 'N' as the size of the card, the card is NxN (COLxROW)
	8. Numbers on cards are from the integers 1 to M, with M being chosen by the user from 2*(N^2) to floor(3.9*(N^2))
	9. Numbers should only appear on a card once
	10. Each column is named with one letter from 'BINGOLARDYPEZMUX', starting from B
	11. Odd-sized cards have a 'FREE!' square in the center square
	12. Number of bingo cards is chosen by the user from 2 to 8192 inclusive
	13. A card or a whole deck can be printed to the command line
	14. The deck can be saved to a file
    *   List what you already know how to do.
	** Accept and validate input from the user
	*** Repeat prompt when invalid input is given
	** Convert strings to ints
	** Print a Bingo card that complies with the customer's format
	** Pick numbers for Bingo cards that are random, don't repeat on a card, and are arranged in columns with increasing value
    *   Point out any challenges that you can foresee.
	** Displaying colorful menus and prompts
	** Printing output to a file instead of screen in Python
	** Writing unit tests
*   [X] List all of the data that is used by the program, making note of where it comes from.
	** Menu entries from user
	*** Single characters from the user
	*** Letters accepted in both upper and lower case from the user
	** Size of Bingo cards given by the user, an integer from 3 to 16
	** Range of numbers that can appear on a Bingo card, depending on size of the card N from user
	*** The smallest number that can appear on a Bingo card is 1 by default
	*** The biggest number M is one in the range of 2 * (N^2) to floor(3.9 * (N^2)) calculated by the program
    *   Explain what form the output will take.
	** Menus and Prompts
	*** Includes a cool main menu with an ASCII-art logo
	** Bingo Cards
	*** Are numbered by position in the deck
	*** Columns of numbers on the cards have a letter for a name.  Combined with a number, it is easy to see if that number exists on your card
	*** Cells on Bingo cards are printed with dashes (-), plus signs (+), and pipes (|)
	*** Cards can be printed to the screen one at a time or all at once
	*** The whole deck can be saved to a file
*   [X] List the algorithms that will be used (but don't write them yet).
	** Sorting algorithm
	** Shuffling algorithm
	** One to create a list of numbers from 1 to M in order, then randomize it, and pop elements so they can't be reused
	** Give the first column the first 1/N numbers in the above list, second column gets numbers in 2/N, etc.
*   [X] C++ UML Diagram Analysis.
	** There are 7 modules, excluding 'bingo' and 'runTests'.
	** The ‘UserInterface’ module has a private attribute ‘m_deck’, with type ‘Deck’(another module and a class). ‘UserInterface’ has two public operations: UserInterface(), and run(). It also has 7 private operations: logo() which prints the logo, createDeck() which creates a deck, deckMenu() which uses the ‘Menu’ module, getStr(string entered from prompt) which returns that string , printCard() which prints the card, and saveDeck() which saves the deck to a file.
	** The ’Menu’ module has two private attributes, m_szHeader which is a string and m_arrOptions which is an array from the operation MenuOption in the ‘MenuOption’ class. There are six public operations: Menu which uses the szHeader attribute, operator+ which takes an option from ‘MenuOption’, operator[] which takes an integer from nIdx and returns a MenuOption, length which returns an integer, isValidCommand which takes a character given by chCommand and returns a Boolean, and prompt which returns void.
	** The ’MenuOption’ module is a realization of the ‘Menu’ class and has two private attributes, m_chCommand which is a character and m_szDescription which is a string. There are four public operations: MenuOption which takes chCommand and szDescription as arguments, getCommand which returns a character, getDescription returning a string, and an operator overload.
	** ‘TtyColors’ extends ‘UserInterface’, ‘MenuOption’, and ‘Menu’ by providing the colors black, red, green, yellow, blue, magenta, cyan, and white for printing to the console.
	** The ‘Deck’ module/class is made up of between 2 to 8192 cards from the ‘Card’ class. Both use the ‘RandNumberSet’ class. There are 4 private attributes: m_nCardSize, m_nNumCards, and m_nMaxNum return integers and m_arrCards gives an array of the cards. The four public operators are: Deck taking nCardSize, nNumCards, and nMaxNum as arguments, getSize returning an integer, an operator overload of arrays taking nIdx and returning a Card. 
*   [X] Tag the last commit in this phase `analyzed`
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*


## Phase 1: Design (tag name `designed`)
*(30% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [X] Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain its purpose and types of inputs and outputs.
*   [X] Pseudocode that captures how each function works.
	* Unless stated otherwise, all attributes and operators are public
	1. MenuOption class
		import TtyColors class
		define class MenuOption that uses TtyColors
			define class constructor taking self, chCommand, and szDescription as parameters
				create private attribute m_chCommand of class equal to chCommand
				if private attribute m_chCommand is an empty string
					set attribute m_chCommand to '?'
				else if the length of attribute m_chCommand is greater than 1
					set attribute m_chCommand to the first element of m_chCommand
				create private attribute m_szDescription equal to szDescription
				if attribute m_szDescription is an empty string
					set attribute m_szDescription equal to '???'
			define getCommand operation with self as a parameter
				return the private attribute m_chCommand
			define getDescription operation with self as a parameter
				return the private attribute m_szDescription
			define string dunder operator overload with self as a parameter
				return the value of m_chCommand in yellow and the value of m_szDescription in cyan

	2. Menu class
		import TtyColors class
		define class Menu that uses TtyColors
			define class constructor that takes self and szHeader as paramaters
				create private attribute m_szHeader equal to szHeader
				create private attribute m_arrOptions as an empty array
			define iadd dunder operator overload with self and option as parameters
				append the option parameter to m_arrOptions attribute
				return self
			define getitem dunder operator overload with self and nIdx as parameters
				if nIdx is greater than or equal to 0 and the length of self is greater than nIdx
					return the value of m_arrOptions at the nIdx'th element
				else raise an index error
			define len dunder operator overload with self as a parameter
				return the length of m_arrOptions array
			define isValidCommand operator that takes self and chCommand as parameters
				for all elements in the length of the class(which is the length of m_arrOptions)
					if the uppercase value of chCommand is equal to the i'th index of self.getCommand as an uppercase value
						return True
					else return False
			define prompt operator with self as a parameter
				while isValidCommand returns True
					create empty array called options
					create string variable called header which has the value of m_szHeader followed by " menu"
					create string variable called bar which is an "=" repeated length of header times
					print bar on a newline, then header in white on a newline, and then bar again on a newline
					for all elements in self(which is the length of m_arrOptions)
						set option equal to the current element
						if option is not a None type
							print the option
							append to options option.getCommand() in yellow
					print in all white a newline, then "Enter a " + value of m_szHeader + " command"
					create variable called command equal to user input
					if the command is valid
						return the command
					else print the command in magenta and then " is not a valid option"
	3. TtyColors class
		define class TtyColors
			define operator black with self and s (a string) as parameters
				return the string in black
			define operator red with self and s (a string) as parameters
				return the string in red
			define operator green with self and s (a string) as parameters
				return the string in green
			define operator yellow with self and s (a string) as parameters
				return the string in yellow
			define operator blue with self and s (a string) as parameters
				return the string in blue
			define operator magenta with self and s (a string) as parameters
				return the string in magenta
			define operator cyan with self and s (a string) as parameters
				return the string in cyan
			define operator white with self and s (a string) as parameters
				return the string in white
	4. RandNumberSet class
		import random
		define class RandNumberSet
			create int variable MIN_SIZE equal to 3
			create int variable MAX_SIZE equal to 16
			define class constructor with self, nSize, and nMax as parameters
				create private attribute of class m_nRowPos equal to 0
				create private attribute of class m_nSize equal to nSize
				if m_nSize is less than MIN_SIZE(which is 3)
					set m_nSize equal to MIN_SIZE(equal to 3)
				else if m_nSize is greater than MAX_SIZE(which is 16)
					set m_nSize equal to MAX_SIZE(equal to 16)
				create private attribute of class m_nMax equal to nMax
				if m_nMax is less than m_nSize squared
					set m_nMax equal to m_nSize squared
				create private attribute m_arrSegments as an empty array
				create variable segmentSize by integer dividing m_nMax over m_nSize
				create variable remainder equal to the modulo of m_nMax over m_nSize(the remainder left over after the integer division)
				create variable low equal to 1
				for segments in m_nSize
					create variable high equal to low + segmentSize
					if the segment is less than or equal to remainder
						increment high by 1
					append to m_arrSegments a list of range low to high
					set low equal to high
			define shuffle operator with self as a parameter
				for each segment in m_arrSegments
					randomly shuffle the segment
				set m_nRowPos equal to 0
			define getNextRow operator with self as a parameter
				if m_nRowPos is greater than or equal to m_nSize
					return None
				create empty array called row
				for all segments in m_arrSegments
					append to array row the current segment
				increment m_nRowPos by 1
				return row array
			define getSegments operator with self as a parameter
				return m_arrSegments
			define string dunder operator overload with self as a parameter
				create empty array called strs
				for all segments in m_arrSegments
					append to array strs the string of the current segment
				return the strs array with newlines in each element
			define getItem dunder operator overload with self and n as parameters
				if n is greater than or equal to 0 and less than m_nSize
					create empty array called row
					for all segments in m_arrSegments
						append to row the current segments n'th element
					return the row array
				else raise an index error

	5. Card class
		define new class Card
			create a list called COLUMN_NAMES containing the following values in order: BINGOLARDYPEZMUX
			define class constructor with self, nId, and randNumSet as parameters
				create private attribute of class called m_nId equal to nId
				create private attribute of class called m_arrNums as an empty integer array
			define getID operator that takes self as a parameter
				return the integer value of m_nId
			define numberAt operator that takes self, nRow, and nCol as parameters
			        return the value at m_arrNums[nCol + ((nRow - 1) * nCol)] (MAY BE "FREE!")
			define length dunder operator overload that takes self as a parameter
				return the square root of the length of m_arrNums
			define string dunder operator overload that takes self as a parameter
				create string called printDivider that prints a newline, then "+", then "-----+" for how many columns there are
				for all elements in COLUMN_NAMES in range of the length of the class
					print the element with no newline, three spaces before, and two spaces after 
				print printDivider
				for all elements in m_arrNums
					if it is the first element in that row
						print a "|"
					if the element is a positive number
						print the element with center formatting in 5 spaces and then a "|"
					else if the element is negative
						print "FREE!|"
					if it is the last element in that row
						print printDivider
	6. Deck class
		import Card class
		import RandNumberSet class
		define new class Deck
			define class constructor with self, nCardSize, nNumCards, and nMaxNum as parameters
				create private attribute of class m_nCardSize equal to nCardSize
				create private attribute of class m_nNumCards equal to nNumCards
				create private attribute of class m_nMaxNum equal to nMaxNum
				create private attribute of class m_arrCards as an array with all the cards in it
			define length dunder operator overload with self as a parameter
				return the integer m_nNumCards
			define getitem dunder operator overload with self and nIdx as parameters
				return the card in the N'th element of n_arrCards
			define string dunder operator overload with self as a parameter
				for all elements in the array m_arrCards
					print element
	7. UserInterface class
		import Deck class
		import Menu class
		import MenuOption class
		import TtyColors class
		define new class UserInterface that uses TtyColors
			define class constructor with self as a parameter
				create private attribute of class m_deck equal to None
			define run operator with self as a parameter
				while it is True
					print the logo
					create new variable menu equal to Menu("Main")
					append to menu MenuOption("C", "Create a new deck")
					append to menu MenuOption("X", "Exit the program")
					create new variable command equal to input from the user
					if the uppered command input is "C"
						create a new Deck
					else if the uppered command input is "X"
						close the program
			define private logo operator with self as a parameter
				print the logo
			define private createDeck operator with self as a parameter
				create variable size by asking the user to enter the size of the card they want and saving it, showing it must be between 3 and 16 (use get_int)
				create variable maxNum by asking the user to enter it (use get_int)
				create variable numCards by asking the user to enter it, showing it must be between 2 and 8192  (use get_int)
				create the new Deck object by calling Deck(size, numCards, maxNum)
				call __deckMenu()
			define private deckMenu operator with self as a parameter
				create variable menu equal to Menu("Deck")
				append to menu MenuOption("P", "Print a card to the screen")
				append to menu MenuOption("D", "Display the whole deck to the screen")
				append to menu MenuOption("S", "Save the whole deck to a file")
				append to menu MenuOption("X", "Return to the Main menu")
				while True
					create variable command equal to menu.prompt()
					if the upper of command is "P"
						print the Card
					if the upper of command is "D"
						print the deck to the screen
					if the upper of command is "S"
						save the deck
					else if the upper of command is "X"
						exit the program
			define private getStr operator with self and prompt as parameters
				create a string variable inputStr as an empty string
				while inputStr is an empty string
					set inputStr to what is entered by the user when prompted, using the prompt parameter as the prompt to print
				return inputStr
			define private operator getInt with self, prompt, lo, and hi as parameters
				create an integer variable inputInt equal to 0
				while inputInt is not inbetween lo and hi
					set inputInt to what is entered by the user when prompted, using prompt parameter as the prompt to print 
			define private operator printCard with self as a parameter
				create an int variable cardNum by prompting the user for which card to print
				print the cardNum Card in Deck
				return None
			define private operator saveDeck with self as a parameter
				create a str variable fileName by prompting the user for the name of the file to write the Deck into
				open the fileName file in write mode using the format open(fileName, mode='a')
				Use the format:
					org_stdout = sys.stdout
					with open('fileName', 'a') as file
						sys.stdout = f
						print(Deck)
						sys.stdout = org_stdout
				
			
*   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occur to you, and use them later when testing
	1. When an invalid input is given, it should say it is not a valid option and reprint the prompt, including what is valid input just like before
	2. When 'p' or 'P' is inputted in the deck menu, it should print a card to the screen
	3. When 'd' or 'D' is inputted in the deck menu, it should print the whole deck to the screen
	4. When 's' or 'S' is inputted in the deck menu, it should save the whole deck to a file that the user gets to name
	5. When 'x' or 'X' is ever entered it moves back, ie. from the Deck menu to the Main menu, and if in the Main menu it will terminate the program
	6. When a valid size of the card is input, it should save and the card will have that many rows and columns
	7. When a valid deck size is input, there should be that number of cards in the deck
*   [X] Tag the last commit in this phase `designed`
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*


## Phase 2: Implementation (tag name `implemented`)
*(15% of your effort)*

**Finally, you can write code!**

Deliver:
	CREATE A NEW UML DIAGRAM FOR THIS PHASE
*   [X] More or less working code.
*   [X] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan
	1. I added a newline to the print statement on line 63 of Card.py
	2. I didn't use get_int in UserInterface.py, I just made the input an integer
	3. Added the low and high values for the maxNum on a card in UserInterface.py 'using the equations
	4. Changed operators in Card.py to use a 2D list instead of 1D 
	5. Had problems where the objects were being referenced instead of performing the operation
*   [X] Tag the last commit in this phase `implemented`


## Phase 3: Testing and Debugging (tag name `tested`)
*(30% of your effort)*

Deliver:
		CREATE NEW/FINISH INCLUDED TEST CASES (THERE SHOULD BE AT LEAST 16)
*   [X] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
	1. All of the test cases are automated! Simply navigate to the programs main directory and type in 'python src/runTests.py' and press [ENTER].
	2. If everything is working correctly, there should be no error messages, and no tests will say FAIL.
	3. If any test fails, it will show 'FAIL' next to the test. 
		1. The easiest way to fix this is to replace the faulty program with a new download of the original.
		2. Run 'git restore .' to restore the working program.
*   [X] Tag the last commit in this phase `tested`


## Phase 4: Deployment (tag name `deployed`)
*(5% of your effort)*

Deliver:

*   [X] Tag the last commit in this phase `deployed`
*   [X] Your repository is pushed to GitLab.
*   [X] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [X] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 5: Maintenance

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [X] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
	1.  I'm not quite sure how RandNumberSet works.
        *   If a bug is reported in a few months, how long would it take you to find the cause?
	1.  I think it would take me between 15 minutes to an hour, depending on the bug.
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        1.  I think my documentation will make sense to most programmers.
	*   ...yourself in six month's time?
	1.  It will still make sense to me in six months
    *   How easy will it be to add a new feature to this program in a year?
	1.  It should be pretty easy to add a new feature to this program in a year (like a colored Bingo card would be cool)
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
	1.  This program should continue to work regardless of any upgrades.
*   [X] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [X] Respond to the **Assignment Reflection Survey** on Canvas.
