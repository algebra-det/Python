game = [[0]*3 for _ in range(3)]


class player:

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


x = player()
y = player()
player.board()
for i in range(1,7):
    if i%2!=0:
        z = input("Enter Your move , player 1, first row than column ")
        x.move(z,1)
    else:
        z = input("Enter Your move , player 2, first row than column ")
        y.move(z,2)













