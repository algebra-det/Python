game = [[0]*3 for _ in range(3)]

def win(current_game):  # This is not ideal, what if we want a game that is 4X4
    for row in game:
        print(row)
        col1 = row[0]
        col2 = row[1]
        col3 = row[2]

        if col1==col2==col3:
            print("SO we have a winner!!!")
            break

win(game)
print()

def win1(curren_game):      # this one will work but that's lot of code
    for row in game:
        print(row)
        all_match = True
        for item in row:
            if item != row[0]:
                all_match = False
        if all_match:
            print("Winner")
            break

win1(game)
print()

def horizontal_win(current_game):
    for row in game:
        print(row)
        if row.count(row[0]) == len(row):   # line 19-24 can be written in a single line
            print("In horizontal Winner")
            break

horizontal_win(game)
print()

game1 = [[2,0,2],
         [1,2,0],
         [2,1,0]]

def  vertical_win(current_game):
    for col in range(len(game1)):
        check = []

        for row in game1:
            check.append(row[col])
        print(check)
        if check.count(check[0]) == len(check) and check[0] != 0:
            print("In vertical Winnder")

vertical_win(game1)
print()

def diagonal_win(current_game):    # as this one is hardcode because what if the size of game is 4X4
    if game1[0][0]==game1[1][1]==game1==[2][2]:
        print("winner in diagonal")
    elif game1[2][0]==game1[1][1]==game1[0][2]:
        print("winner in diagonal")

diagonal_win(game1)
print()

def diagonal_win1(curren_game):
    check = []
    for number,row in enumerate(game1):     # right to left i.e. [00] [11] [22]
        check.append(row[number])
    print(check)
    if check.count(check[0]) == len(check) and check[0] != 0:
        print("In diagonal Winnder")

    check1 = []
    x = len(game1)          # x = 3
    for row in game1:       # left to right i.e. [02] [11] [20]
        x -= 1
        check1.append(row[x])
    #OR CHECK DIA_LR()

    print(check)
    if check1.count(check1[0]) == len(check1) and check1[0] != 0:
        print("In diagonal Winnder")

diagonal_win1(game1)
print()

def dia(game1):     # for right to left  [02] [11] [20]
    check = []
    colu = list(reversed(range(len(game1))))
    row = range(len(game1))
    for col , rows in zip(colu,row):        # check zip() built-in function
        check.append(game1[col][rows])
    print("in dia",check)

dia(game1)
print()

def dia_lr(game1):
    check = []
    for col, row in enumerate(reversed(range(len(game1)))):
        check.append(game1[col][row])
    print("in dia_lr",check)

dia_lr(game1)














