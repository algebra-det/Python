li = [99,8,12,4,45,7,65,21,3,9,7,4,25]
n = 120
li = sorted(li)
print(li)
pos = 0

def search(li,n):
    l = 0
    u = len(li)-1

    while l <= u:
        mid = (l+u)//2

        if li[mid]==n:
            globals()['pos'] = mid
            return True
        else:
            if li[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False


if search(li,n):
    print("Found at ",pos+1)
else:
    print("Not Found")