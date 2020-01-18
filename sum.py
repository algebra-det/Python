y = int(input("Enter the number"))
x = 'akash chauhan'
z = 0
for i in x:
	if i==' ':
		pass
	else:
		z+=1

print(z)

ones = ['one','two','three','four','five','six','seven','eight','nine']
tens = ['ten','twenty','thirty','fourty','fifty','sixty','senenty','eighty','ninety']
greaterthanten = ['hundred','thousand','million']

a = str(y)
b=len(a)
if a[b-4]=True:
	print(greaterthanten[int(a[b-4])-1])

if a[b-3]==True:
	print(greaterthanten[int(a[b-3])-1])

if a[b-2]==True:
	print(tens[int(a[b-2])-1])

print(ones[int(a[b-1])-1])

