import random
import time
import os

os.system('cls' or 'clear')

class color : 
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'

def show():

    for i in range(3):
        for j in range(3):
            print(Game[i][j],end=(' '))
        print()

char_1 = color.GREEN +'X'

def player():
    # Player 1
    while True:
        while True:
            print('Player 1')
            row = int(input())
            col = int(input())

            if 0 <= row <= 2 and 0 <= col <= 2 :
                if Game[row][col] == '_':
                    Game[row][col] = char_1
                    break
                else:
                    print('This cell is not empety')
            else:
                print('Eror, Index Out Of Range')


        show()
        check()


        while True:
            print('Player 2')
            row = int(input())
            col = int(input())

            if 0 <= row <= 2 and 0 <= col <= 2 :
                if Game[row][col] == '_':
                    Game[row][col] = color.RED +'O'
                    break
                else:
                    print('This cell is not empety')
            else:
                print('Eror, Index Out Of Range')
        show()
        check()

def cpu():
    
    # Player 1
    while True:
        while True:
            print('Player 1')
            row = int(input())
            col = int(input())

            if 0 <= row <= 2 and 0 <= col <= 2 :
                if Game[row][col] == '_':
                    Game[row][col] = 'X'
                    break
                else:
                    print('This cell is not empety')
            else:
                print('Eror, Index Out Of Range')


        show()
        check()


        while True:
            print('Player 2 cpu')
            row = random.randint(0,2)
            col = random.randint(0,2)

            if 0 <= row <= 2 and 0 <= col <= 2 :
                if Game[row][col] == '_':
                    Game[row][col] = 'O'
                    break
                else:
                    print('This cell is not empety')
            else:
                print('Eror, Index Out Of Range')
        show()
        check()

def check():
    for i in range(3):
        for j in range(3):

            if Game[i][0] == 'X' and Game[i][1] == 'X' and Game[i][2] == 'X':
                print('Player 1 win')
                exit()
            if Game[0][j] == 'X' and Game[1][j] == 'X' and Game[2][j] == 'X':
                print('Player 1 win')
                exit()
            if Game[0][0] == 'X' and Game[1][1] == 'X' and Game[2][2] == 'X':
                print('Player 1 win')
                exit()
            if Game[0][2] == 'X' and Game[1][1] == 'X' and Game[2][0] == 'X':
                print('Player 1 win')
                exit()

            if Game[i][0] == 'O' and Game[i][1] == 'O' and Game[i][2] == 'O':
                print('Player 2 win')
                exit()
            if Game[0][j] == 'O' and Game[1][j] == 'O' and Game[2][j] == 'O':
                print('Player 2 win')
                exit()
            if Game[0][0] == 'O' and Game[1][1] == 'O' and Game[2][2] == 'O':
                print('Player 2 win')
                exit()
            if Game[0][2] == 'O' and Game[1][1] == 'O' and Game[2][0] == 'O':
                print('Player 2 win')
                exit()
    if all(cell != '_' for row in Game for cell in row):
        print('Draw')
        exit()


Game = [['_','_','_'],
        ['_','_','_'],
        ['_','_','_']]
show()

print('Please choose your starting game')
print('1-Player or 2-Cpu')
menu = int(input('inser your choose number :'))

if menu == 1 :
    player()

if menu == 2 :
    cpu()

