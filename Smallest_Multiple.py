

def multiple():
    y = int(input("Enter the multiple upto"))
    x=0
    for i in range(2,10000000000000000):
        if x!=0:
            break
        else:
            for j in range(2,y+1):
                if i%j==0:
                    if j>=y:
                        x = i
                        print(x)
                        break
                else:
                    break

multiple()