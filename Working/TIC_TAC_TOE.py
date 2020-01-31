from itertools import *
from time import *

class player:

    def winning(row):
        if row.count(row[0]) == len(row) and row[0] != 0:  # line 19-24 can be written in a single line
            player.board()
            print("Game won!")
            return True

    @staticmethod
    def board():
        print("  0  1  2")
        for row, i in enumerate(game):
            print(row, i)
        print("__________")

    def move(self,z,j):
        term = []
        for i in z:
            term.append(int(i))
        game[term[0]][term[1]] = j
        player.board()
        player.main()

    @staticmethod
    def horizontal_win():
        for row in game:
            if player.winning(row):
                print("Game won! - Horizontally")
                return True
        return False

    @staticmethod
    def vertical_win():
        check = []
        for i in range(3):
            for row in game:
                check.append(row[0])
            if player.winning(check):
                print("Game won! - Vertically")
                return True
        return False

    @staticmethod
    def diagonal_win():
        check = []
        for i, row in enumerate(game):
            check.append(row[i])

        check1 = []
        x = 3
        for row in game:
            x-=1
            check1.append(row[x])

        if player.winning(check) or player.winning(check1):
            print("Game won! - Diagonally By Player ",check[0]+check1[0])
            return True
        return False

    @staticmethod
    def main():
        global sipping
        player.horizontal_win()
        player.vertical_win()
        player.diagonal_win()
        if player.horizontal_win() or player.vertical_win() or player.diagonal_win():
            sipping = True
            return True
        return False

game = [[0] * 3 for _ in range(3)]

x = player()
y = player()
print("Let's play Tic Tac Toe\nIt's gonna be a two player game")
sleep(3)
print("First Player will be assigned number-1\nSecond player will be number-2")
sleep(4)
player.board()
print('This will be the board we are gonna play, ROW is ---<horizonaatal> and COLUMN is | <vertical>')
sleep(2)
var = 1
sipping = False
while not sipping :
    sleep(1)
    var = 1-var
    if var==0:
        z = input("Enter Your move , player 1, first row than column btwn [0-2] - ")
        x.move(z,1)
    else:
        z = input("Enter Your move , player 2, first row than column btwn [0-2] - ")
        y.move(z,2)
