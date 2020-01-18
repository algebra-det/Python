"""Palindrome for Integers"""
palindrome = []
for a in range(100,1000):
    for b in range(a,1000):                             # To save memory as firstly 100 will be * 101,101,102
        x = a*b                                         # so when a will be 101 its will not start with b with 100 but with 101 or higher
        temp = x                                        # as higher with lower will alredy be done
        rev = 0
        while x>0:
            rev = rev*10+x%10
            x = x //10                                  #OR x = int(x/10) , they both return only integer value
        if temp == rev:
            print(temp,"with multiple %d*%d"%(a,b))
            palindrome.append(temp)                     #storing all palindromes
        else:
            pass

x = sorted(palindrome)                                  #sorting palindromes in ascending order
#print("sorted ",x)
print("largest palindrome = ",x[x.__len__()-1])         #after sorting the largest value of palindrome will be residing at the end of list
                                                        #so we take the length of the list and then
                                                        # decreasing the total length by 1 as list addresses starts with [0:]
                                                        # we get the last palindrome number from the list which is highest




"""Palindrome for strings"""

"""z = int(input("Do you want to test a string , if yes than press 1 :- "))
if z==1:
    stri= input("enter the string")
    if stri==stri[::-1]:
        print("its a palindrome")
    else:
        "Its not a palindrome"
else:
    pass

"""