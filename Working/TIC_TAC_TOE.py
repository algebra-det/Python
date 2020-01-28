lst = [[0]*3 for _ in range(3)]
#OR
lst2 = [[0,0,0,],
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

def move(x):
    term = []
    for j in x:
        term.append(int(j))
    lst[term[0]][term[1]] = 1
    board()

board()

x = input("Enter your move")
move(x)












