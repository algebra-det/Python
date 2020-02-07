# In Bubble_Sort we consume to much cpu power and memeory and time because
# we have to iterate through every element upto last value and then iterate again
# upto last second value and so on

# In SELECTION SORTING, we take the max or min value from the list and then swap it with the first
# then second than so one which do not use such extensive cpu power or memory and time

A = [64, 25, 12, 22, 11, 65, 23, 27, 63, 85]

# Traverse through all array elements
for i in range(len(A)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

            # Swap the found minimum element with
    # the first element
    A[i], A[min_idx] = A[min_idx], A[i]

# Driver code to test above
print("Sorted array")
print(A)