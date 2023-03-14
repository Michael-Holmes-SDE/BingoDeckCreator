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

*   [ ] Function signatures that include:
	* os system thing in UML Diagram is an operator overload, usually in the string class
	* m_ means it is a private attribute of the class
	* To open a file for writing and append to the end of the file, use 'open(<FILE>, mode='a')'
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain its purpose and types of inputs and outputs.
*   [ ] Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
*   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occur to you, and use them later when testing
*   [ ] Tag the last commit in this phase `designed`
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*


## Phase 2: Implementation (tag name `implemented`)
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] More or less working code.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan
*   [ ] Tag the last commit in this phase `implemented`


## Phase 3: Testing and Debugging (tag name `tested`)
*(30% of your effort)*

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
*   [ ] Tag the last commit in this phase `tested`


## Phase 4: Deployment (tag name `deployed`)
*(5% of your effort)*

Deliver:

*   [ ] Tag the last commit in this phase `deployed`
*   [ ] Your repository is pushed to GitLab.
*   [ ] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [ ] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 5: Maintenance

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [ ] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Assignment Reflection Survey** on Canvas.
