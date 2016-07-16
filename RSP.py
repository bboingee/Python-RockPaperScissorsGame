# Made by Bentley Kang
# github.com/bboingee
from random import randint


def computer():  # Computer will pick Rock, Scissors or Paper.
    t = ["Rock", "Scissors", "Paper"]
    choice = t[randint(0, 2)]
    print(choice)
    return choice


def entry():  # Accepts only valid user input.
    t = ["Rock", "Scissors", "Paper"]
    while True:
        try:
            user = int(input("Type 1 for Rock \nType 2 for Scissors\nType 3 for Paper\nWhat is your choice: "))
            if user in range(0, 4):
                user -= 1
                choice = t[user]
                return choice
            elif user > 3:
                raise IOError
            else:
                raise ValueError
        except ValueError:
            print("You did not enter an integer.")
        except IOError:
            print("You are out of range.")


def compare(a, b):  # a = computer() b = user
    if a == b:
        print("It's a Tie!")
        return "tie"
    elif a == "Rock":
        if b == "Scissors":
            print("You Lost!")
            return "lose"
        else:
            print("You Win!")
            return "win"
    elif a == "Scissors":
        if b == "Rock":
            print("You Win!")
            return "win"
        else:
            print("You Lost!")
            return "lose"
    elif a == "Paper":
        if b == "Rock":
            print("You Lost!")
            return "lose"
        else:
            print("You Win!")
            return "win"


def ratio(x, y, z):  # Calculates the ratio
    win = x
    lose = y
    tie = z
    total = x + y + z
    try:
        if total == 0:
            raise ZeroDivisionError
        else:
            rate = win / total * 100
            loser = lose / total * 100
            tier = z / total * 100
            print("You have won", win, " times out of ", total,
                  "and the chance of winning is ", format(rate, '.0f'), "%")
            print("You have lost", lose, "times out of ", total,
                  "and the chance of losing is ", format(loser, '.0f'), "%")
            print("You have drew", tie, "times out of ", total,
                  "and the chance of drawing is ", format(tier, '.0f'), "%")
    except ZeroDivisionError:
        print("Please play the game at least once.")


def count(n):  # Count down
    while n > 0:
        print(n)
        n -= 1
    print("Rock, Paper, Scissors, Shoot!")


def run():  # Loop to make the game repeat until the user wants to quit.
    print("Let's play! Rock! Scissors! Paper!")
    win = 0
    lose = 0
    tie = 0
    game = True
    while game:
        try:

            choice = int(input("Type 1 to play the game.\n"
                               "Type 2 to check your ratio.\n"
                               "Type 3 to quit the game.\n"
                               "Please enter your choice: "))
            if choice == 1:
                answer = computer()
                choice = entry()
                count(3)
                abc = compare(answer, choice)
                if abc == "win":
                    win += 1
                elif abc == "lose":
                    lose += 1
                else:
                    tie += 1
            elif choice == 2:
                ratio(win, lose, tie)
            elif choice == 3:
                exit("Bye Bye!")
            elif choice not in range(1, 4):
                raise IOError
            else:
                raise ValueError
        except IOError:
            print("Error! You are out of range.")
        except ValueError:
            print("Error! Please enter numerical input only.")


def main():  # Main function
    run()


# Only main() after this line
main()
