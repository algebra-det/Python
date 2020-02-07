
def bubble_sort(num_list):                  # by last to first
    for i in range(len(num_list)-1,0,-1):
        for j in range(i):
            if num_list[j]>num_list[j+1]:
                #Swapping
                temp = num_list[j]
                num_list[j] = num_list[j+1]
                num_list[j+1] = temp
                # or we have used python swapping technique i.e. a,b = b,a

num_list = [5,3,8,6,7,2]
bubble_sort(num_list)
print(num_list)

def binar(li):                                  # by first to last
    for i in range(len(li)):
        for j in range(len(li)-1,i,-1):
            if li[j]<li[j-1]:
                li[j],li[j-1] = li[j-1],li[j]

hello = [5,4,6,3,2,9,8,5,2,1,7,9]
binar(hello)
print(hello)