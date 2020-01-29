lst = [[0]*3 for _ in range(3)]
#OR
game = [[0,0,0,],
        [0,0,0],
        [0,0,0]]

print("   0  1  2")
count = 0
for i in lst:
    print(count,i)
    count+=1
print("_____________")
# OR

def board():
    print("   0  1  2")
    for count,row in enumerate(lst):
        print(count,row)
    print("_____________")

"""ERROR HANDLING"""
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
    else:
        print("hello")
    finally:        # this will be printed at the end of the program function calling
        print("End of calling")

""" We have many errors which are available , so above we used the indexError and took a variable that posseses the IndexError 'e' , and printed in the except"""



game = game_board(game, just_display=True)
game = game_board(game, player=1, row=2, column=1)
game_board(game, just_display=True)
game_board(game, player=1, row=2, column=6)     # as the row=3 is out of range, it will return an error
# for such scenarios we use try: and except: method ,

game_board(game_board, player=1, row=3 , column=1)






