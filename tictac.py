import random
import time

player1_choices = []
player2_choices = []

win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [1, 4, 7], [1, 3, 6], [2, 5, 8]]

win1 = [0, 1, 2]
win2 = [3, 4, 5]
win3 = [6, 7, 8]
win4 = [0, 4, 8]
win5 = [2, 4, 6]
win6 = [1, 4, 7]
win7 = [1, 3, 6]
win8 = [2, 5, 8]


def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']


def choice():
    pos_index = input("Please enter an index position: ")
    pos_int = int(pos_index)
    if pos_int in player1_choices:
        print("This point is already taken")
        choice()
    elif pos_int in player2_choices:
        print("This point is already taken")
        choice()
    else:
        if pos_int <= 2:
            row1[pos_int] = 'X'
        elif 2 < pos_int <= 5:
            row2[(pos_int - 3)] = 'X'
        elif 5 < pos_int <= 8:
            row3[(pos_int - 6)] = 'X'
        else:
            print("Please enter number between 0 and 8")
        player1_choices.append(pos_int)
        display(row1, row2, row3)


def choice2():
    pos_random = random.randint(0, 8)
    if pos_random in player1_choices:
        choice2()
    elif pos_random in player2_choices:
        choice2()
    else:
        if pos_random <= 2:
            row1[pos_random] = 'O'
        elif 2 < pos_random <= 5:
            row2[(pos_random - 3)] = 'O'
        elif 5 < pos_random <= 8:
            row3[(pos_random - 6)] = 'O'
        else:
            print("Please enter number between 0 and 8")
        player2_choices.append(pos_random)
        display(row1, row2, row3)


def player1():
    print("\nYour turn\n")
    choice()
    time.sleep(1)


def player2():
    print("\nEnemy turn\n")
    time.sleep(1)
    choice2()


display(row1, row2, row3)


def tictac():
    i = 1
    while i < 6:
        player1()
        if i < 5:
            player2()
        i += 1
        result1 = all(elem in player1_choices for elem in win1)
        if result1:
            print("You won")
            break
        result2 = all(elem in player1_choices for elem in win2)
        if result2:
            print("You won")
            break
        result3 = all(elem in player1_choices for elem in win3)
        if result3:
            print("You won")
            break
        result4 = all(elem in player1_choices for elem in win4)
        if result4:
            print("You won")
            break
        result5 = all(elem in player1_choices for elem in win5)
        if result5:
            print("You won")
            break
        result6 = all(elem in player1_choices for elem in win6)
        if result6:
            print("You won")
            break
        result7 = all(elem in player1_choices for elem in win7)
        if result7:
            print("You won")
            break
        result8 = all(elem in player1_choices for elem in win8)
        if result8:
            print("You won")
            break
        result21 = all(elem in player2_choices for elem in win1)
        if result21:
            print("You lost")
            break
        result22 = all(elem in player2_choices for elem in win2)
        if result22:
            print("You lost")
            break
        result23 = all(elem in player2_choices for elem in win3)
        if result23:
            print("You lost")
            break
        result24 = all(elem in player2_choices for elem in win4)
        if result24:
            print("You lost")
            break
        result25 = all(elem in player2_choices for elem in win5)
        if result25:
            print("You lost")
            break
        result26 = all(elem in player2_choices for elem in win6)
        if result26:
            print("You lost")
            break
        result27 = all(elem in player2_choices for elem in win7)
        if result27:
            print("You lost")
            break
        result28 = all(elem in player2_choices for elem in win8)
        if result28:
            print("You lost")
            break
    print("\n")
    print(player1_choices)
    print(player2_choices)


tictac()
