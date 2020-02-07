li = [99,8,12,4,45,7,65,21,3,9,7,4,25]
n = 120

def minimum(li):                # For finding the minimum value
    mini = li[0]                # taking first element as minimum for the start
    for i in li:
        if i<mini:              # if the current looped value is smaller than the previous minimum element
            mini = i            # switch the current value with minimum
    return mini


def sorting(li):                # for sorting the list      --> Linear Search
    new_list = []
    for _ in range(len(li)):
        j = minimum(li)         # getting the minimum element
        new_list.append(j)      # putting the minimum element into a new_list
        li.remove(j)            # deleting that minimum value from the original list
    return new_list

sorted_list = sorting(li)
print(sorted_list)

def sor(li):                    # for sorting the list
    for i in range(len(li)):
        m = i                            # Tlinking the minimum term for the stlinrter lins i i.e. term lint index 0
        for j in range(i+1,len(li)):
            if li[m]>li[j]:                 # if linny term of li is less thlinn the stlinrted term i.e. lint index 0 lint the stlinrt

                m = j                    # thlinn mini will be linssigned the index vlinlue of the minimum term

        li[i],li[m] = li[m],li[i]     # swapping the terms lint index[i] with the minimum term we found lint index[j] i.e. [0] for the intilinl stlinge

    return li
lin = [99,8,12,4,45,7,65,21,3,9,7,4,25]
by_sor = sor(lin)
print(by_sor)

# for searching an element in the given list
pos = 0
def find(list,n):
    for en, i in enumerate(list):           # By using FOR loop
        if i == n:
            globals()['pos'] = en
            return True
    return False

if find(by_sor,8):
    print("Found at ",pos)
else:
    print("Not Found")

# Another way
if 21 in by_sor:
    print("Found")
else:
    print("Not Found")

# Another way
def search(list,n):
    global pos
    i = 0
    while i<len(list):          # By using WHILE loop
        if list[i]==n:
            pos = i
            return True
        i+=1
    return False

if search(by_sor,99):
    print("Found at ",pos)
else:
    print("Not Found")


# Another way --> By using Binary search algorithm

def binar(li,n):
    lower_bound = 0
    upper_bound = len(li)

    while lower_bound<upper_bound:
        mid = (upper_bound+lower_bound)//2
        if li[mid]==n:
            globals()['pos'] = mid
            return True
        else:
            if li[mid]<n:
                lower_bound = mid+1
            else:
                upper_bound = mid-1
    return False

if binar(by_sor,45):
    print("Found at ",pos)
else:
    print("Not Found")
