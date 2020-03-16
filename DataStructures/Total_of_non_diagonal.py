# Here we are making lists for each diagonal
# One list for the top-left to right-bottom diagonal
# Second list for bottom-left to top-right diagonal
# Than Iterating through each row and column and checking if the (row number, column number) is in the diagonal list
# If it's in the diagonal list than "PASS" otherwise ADD to the TOTAL


def non_diagonals(arr):		# To get zipped list of both diagonals

	first_row = []
	second_column = []

	backward_first_row = []
	backward_second_column = []

	for i in range(len(arr)):		# top-left to right-bottom diagonal
		first_row.append(i)
		second_column.append(i)

	for j,k in enumerate(range((len(arr)-1),-1,-1)):		# bottom-left to top-right diagonal
		backward_first_row.append(j)
		backward_second_column.append(k)

	mello = list(zip(first_row,second_column))			# # top-left to right-bottom diagonal

	bello = list(zip(backward_first_row,backward_second_column))		# bottom-left to top-right diagonal
	
	return mello, bello

arr=[[1, 2, 3, 4], [5, 6, 7, 8],[9, 10, 11, 12], [13, 14, 15, 16]]


# Getting the diagonals list
first_zip, second_zip = non_diagonals(arr)

total = 0		# Having a variable to hold the total

for i in range(len(arr)):			# 0,1,2,3,...
	for j in range(len(arr)):		# 0,1,2,3,...
		for k in first_zip:							# Checking for the first_zip(diagonal)
			if i==k[0] and j==k[1]:							# if (i,j) are in first_zip(diagonal) than break here and don't go further
				break
		else:									# If (i,j) are NOT in first_zip(diagonal) than Go to check for second_zip(diagonal) 
			for l in second_zip:					# Checking for second_zip(diagonal)
				if i==l[0] and j==l[1]:	# If (i,j) are in second_zip(diagonal) than break here and don't go further
					break
			else:						# If not in second_zip(diagonal) than add the value of this certain index [i][j]
				total += arr[i][j]

print(total)
