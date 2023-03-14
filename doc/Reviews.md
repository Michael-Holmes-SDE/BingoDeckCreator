# C++ Team Software Plan Review

## What are your overall impressions about the C++ team's design?
I think the C++ team’s design is pretty good. All the modules are properly named, have attributes and operations, and it even shows which attributes and operations should be public and private.

## What did you learn from the C++ team's UML Class Diagram?
From the C++ team’s UML Class Diagram I learned that the Card class will be a child class of the Deck class, and both classes will be dependent on the RandNumberSet class. The TtyColors class extends the UserInterface, Menu, and MenuOption classes. The UserInterface class uses the Menu class, and the MenuOption class is a child class of the Menu class.

## Did the class diagram help you understand/navigate the source code?
The diagram helped me understand and navigate the source code much more than if it wasn’t there, though I am still a little confused about how to use it and what everything means, like how to actually implement the operations.

## What did you learn from the C++ team's Software Development Plan?
From the C++ team’s Software Development Plan I learned that there will be two menus: the ‘Main’ menu and the ‘Deck’ menu, and both are case-insensitive. I learned that the biggest number on a card, M, can be as low as 2∗(N^2), or as great as floor(3.9∗(N^2)), with N being the amount of columns on the bingo card. One card or the whole deck can be displayed on the screen, and the entire deck can be saved in a file. The Card class will have a 2-dimensional array that holds onto the numbers to be printed; if there is a FREE square, it will be a negative value in the array and when printed the string “FREE!” will be printed instead.

