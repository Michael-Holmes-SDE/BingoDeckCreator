# Software Development Plan

## Phase 0: Requirements Analysis (tag name `analyzed`)
*(20% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Re-write the instructions in your own words.
    *   If you don't do this, you won't know what you're supposed to do!
    *   Don't leave out details!
*   [ ] Explain the problem this program aims to solve.
    *   Describe what a *good* solution looks like.
	1. Has case-insensitive input from prompts to the user(Upper everything inputted)
	2. Crashes when a wrong filename is entered
    	3. Repeats prompts until: for strings, there is a character; for integer, .isdigit() returns true and is within range(prompt should show the range of numbers acceptable)
	4. Show the user what kind of input is expected by the program
	5. Use the number of position in the Deck as an identifier for the card there
	6. With 'N' as the size of the card, the card is NxN
	7. Numbers on cards are from the integers [1 to M], with M being chosen by the user from [2*(N^2) to floor(3.9*(N^2))]
	8. Numbers should only appear on a card once
	9. Each column is named with one letter from 'BINGOLARDYPEZMUX', starting from B
	10. Odd-sized cards have a 'FREE!' square in the center square
	11. Number of bingo cards is chosen by the user from 2 to 8192 inclusive
    *   List what you already know how to do.
	** Accept and validate input from the user
	*** Repeat prompt when invalid input is given
	** Convert strings to ints
	** Print a Bingo card that complies with the customer's format
	** Pick numbers for Bingo cards that are random, don't repeat on a card, and are arranged in columns with increasing value
    *   Point out any challenges that you can foresee.
	** Display colorful menus and prompts
	** Print output to a file instead of screen in Python
	** Write unit tests
*   [ ] List all of the data that is used by the program, making note of where it comes from.
	** Menu entries from user
	*** Single characters
	*** Letters accepted in both upper and lower case
	** Size of Bingo cards
	*** Integers from 3 to 16
	** Range of numbers that can appear on a Bingo card, depending on size of the card N
	*** The smallest number that can appear on a Bingo card is 1
	*** The biggest number M is one in the range of 2 * (N^2) to floor(3.9 * (N^2))
    *   Explain what form the output will take.
	** Menus and Prompts
	*** A cool main menu with an ASCII-art logo
	** Bingo Cards
	*** Numbered by position in the deck
	*** Columns of numbers on the cards have a letter for a name.  Combined with a number, it is easy to see if that number exists on your card
	*** Cells on Bingo cards are printed with dashes (-), plus signs (+), and pipes (|)
	*** Cards can be printed to the screen one at a
*   [ ] List the algorithms that will be used (but don't write them yet).
*   [ ] Tag the last commit in this phase `analyzed`
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*


## Phase 1: Design (tag name `designed`)
*(30% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain its purpose and types of inputs and outputs.
*   [ ] Pseudocode that captures how each function works.
	def function (to get max number on Bingo card)
		pick a number in the range of 2 * (N^2) to floor(3.9 * (N^2))
	def maxNumber(numColumns = N):
		maxNum = randint(range(2 * (N^2), floor(3.9 * (N^2)) + 1))
		return maxNum
		
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
