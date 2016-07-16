#Python-RockPaperScissorsGame

Rock Paper Scissors game created on Python. 

##Instruction

This python program will ask the user if they want to play the game of Rock Paper Scissors game with a computer or display their winning, losing and drawing percentage. The program will only terminate if the user inputs the command to close it. 

##About

Programmed by Bentley Kang

In this program, I practiced how to use Lists function in Python. Addition to it, this game will not accept any invalid inputs. Like the real Rock Paper Scissors game, once the user selects what they want to shoot, the countdown will start and the program will tell if the user has won, lost or drew. 

First, I started off with a function called computer to make lists that contain character "Rock, Scissors, Paper". By using the random modules and importing randint function, the program is able to pick 1 word randomly from the lists. 

On entry function, it will also have lists that contain choices. To reduce errors such as a typo, the program asks the user to type an integer for their entry. Also used while function with error and exception to accept only valid input. 

The compare function will compare the user's choice with the random pick. This function will return characters according to the Rock Paper Scissors game. The returned value will be used to calculate the ratio.

The ratio function will calculate the winning, losing, and drawing ratio for the user. Used error and except function to prevent zero division. This can occur when the user asks for the result when they initially start the program. 

The function count does simple counting down, starting from the given number. When the number reaches 0, it will print "Rock Paper, Scissors Shoot!" to imitate the actual game. 

Lastly, the function run contains variables for a win, lose and tie. First, it will print a welcome message and will ask the user if the user wants to play the game, see the ratio or terminate the game. The if, elif and else statements are used, also while loop with error and exception is used again to accept only valid input. 

