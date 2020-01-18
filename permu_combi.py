def permutation(n, r):
    nu = 1
    ru = 1
    for i in range(1, n + 1):
        nu *= i
    for j in range(1, (n - r) + 1):
        ru *= j
    print(nu // ru)

def combination(n,r):
    nu = 1
    ru = 1
    cu = 1
    for i in range(1, n + 1):
        nu *= i
    for j in range(1, (n - r) + 1):
        ru *= j
    for k in range(1,r+1):
        cu*=k
    print(nu // (ru*cu))


def main():
    n = int(input("Enter N - "))
    r = int(input("Enter R - "))
    x = int(input("For Permutation press 1\nFor Combination press 2 - "))
    if x==1:
        permutation(n,r)
    else:
        combination(n,r)

if __name__=="__main__":
    main()