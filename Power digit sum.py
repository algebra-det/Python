
def sum(x,y):
    sum=0
    for n in str(x**y):
        sum+=int(n)
    print(sum)

x= int(input("Enter The Base"))
y= int(input("Enter The Power"))
sum(x,y)
