def findTriplets(arr, n, sum):
    arr.sort()
    for i in range(0, n-1):

        l = i + 1
        r = n-1
        x = arr[i]
        while (l < r) :
            if (x + arr[l] + arr[r] == sum) :
                print(x, arr[l], arr[r])
                l = l + 1
                r = r-1

            elif (x + arr[l] + arr[r] < sum):
                l = l + 1

            else:
                r = r-1

arr = [ 0, -1, 2, -3, 1 ]
sum = -2
n = len(arr)
findTriplets(arr, n, sum)