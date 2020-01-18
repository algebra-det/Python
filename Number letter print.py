ones = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
twodigit1 =['Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
tens = ['Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
hundreds = ['Hundred']

def one(i):
    print(ones[i-1])


def ten(a):
    if a[1]=="0":
        b = int(a[0])
        print(tens[b-1])
    elif a[0]=="1":
        b = int(a[1])
        print(twodigit1[b-1])

    else:
        x = int(a[0])
        y = int(a[1])
        print(tens[x-1],ones[y-1])

def hundred(a):
    if a[1]=="0" and a[2]=="0":
        b = int(a[0])
        print(ones[b-1],"Hundred")
    elif a[1]=="0":
        b = int(a[0])
        c = int(a[2])
        print(ones[b - 1], "Hundred and",ones[c-1])

    else:
        b = int(a[0])
        print(ones[b-1],"Hundred and",end=" ")
        c = a[1:]
        ten(c)

for i in range(1,1001):
    a = str(i)
    if len(a)==1:
        one(i)
    elif len(a)==2:
        ten(a)
    elif len(a)==3:
        hundred(a)
    else:
        print("One Thousand")
