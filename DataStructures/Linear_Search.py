li = [5,7,9,3,4]
n = 9
pos = 0 

def search(li,n):
    global pos          #OR globals()['pos'] = i at line 10
    i = 0
    while i<len(li):
        if li[i]==n:
            pos = i
            return True
        i+=1
    return False

if search(li,n):
    print("Found at ",pos)
else:
    print("Not Found")

#OR

def sea(li,n):
    for i in range(len(li)):
        if li[i]==n:
            globals()['pos'] = i
            return True
    return False

if sea(li,n):
    print("Found at ",pos)
else:
    print("Not Found")


#Or

def searching(l,m):
    if m in l:
        print(l.index(m))
    else:
        print("Not in list")

searching(li,n)
