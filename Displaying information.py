import random
import time

numbers = list(range(1, 7))

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
    if pos_int <= 2:
        row1[pos_int] = 'X'
    elif 2 < pos_int <= 5:
        row2[(pos_int - 3)] = 'X'
    elif 5 < pos_int <= 8:
        row3[(pos_int - 6)] = 'X'
    else:
        print("Please enter number between 0 and 8")
    display(row1, row2, row3)


def choice2():
    pos_random = random.randint(0, 8)
    if pos_random <= 2:
        row1[pos_random] = 'O'
    elif 2 < pos_random <= 5:
        row2[(pos_random - 3)] = 'O'
    elif 5 < pos_random <= 8:
        row3[(pos_random - 6)] = 'O'
    else:
        print("Please enter number between 0 and 8")
    display(row1, row2, row3)

def player1():
    print("\nYour turn\n")
    choice()
    time.sleep(1.5)

def player2():
    print("\nEnemy turn\n")
    time.sleep(1.5)
    choice2()

display(row1, row2, row3)

player1()
player2()
player1()
player2()
player1()
player2()