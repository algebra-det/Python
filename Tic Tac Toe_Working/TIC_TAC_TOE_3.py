
def board(game):
    for i in game:
        print(i)

def winner(row):
    if row.count(row[0]) == len(row) and row[0] != 0:  # line 19-24 can be written in a single line
        board(game)
        return True

def horizontal_win(current_game):
    for row in game:
        if row.count(row[0]) == len(row) and row[0]!=0:   # line 19-24 can be written in a single line
            if winner(game):
                print("In horizontal Winner")
            return True
    return False

def  vertical_win(current_game):
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])
        if winner(check):
            print("In vertical Winner")
            return True
    return False

def diagonal_win1(curren_game):
    check = []
    for number,row in enumerate(game):     # left to Right i.e. [00] [11] [22]
        check.append(row[number])
    if winner(check):
        print("In diagonal Winnder")
        return True

    check1 = []
    x = len(game)          # x = 3
    for row in game:       # Right to Left i.e. [02] [11] [20]
        x -= 1
        check1.append(row[x])
    #OR CHECK DIA_LR()

    if winner(check1):
        print("In diagonal Winnder")
        return True
    return False

def if_won():
    if horizontal_win(game) or vertical_win(game) or diagonal_win1(game):
        print("So we have a winner")
        return True
    return False

def game_board(game_map, player = 0, row = 0, column = 0, just_display=False):
    try:    # to try the code if it's requirements are met, like the variables passed by function calling
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count,row)
        return  game_map
    except IndexError as e:     # to do something if there is an error in the variables passed by function calling
        print("Error: did you input row/column as 0,1 or 2? - ",e)
    except Exception as e:      # Every error
        print('Something went very wrong ! - ',e)
    finally:        # this will be printed at the end of the program function calling
        print("End of calling")


play = True
player = [1,2]
while play:
    game = [[0]*3 for _ in range(3)]
    game_won = False
    game = game_board(game,just_display=True)
    while not game_won:
        current_player = 1














