# Array should be of same type throughout
# Arrays are not of fixed size means it can be expanded according to the user

d = {'akash': 'POCO', 'Rohan': 'RealME', 'others': 'others'}    #SET
print(d.keys())
print(d.values())
print(d.get('Rohan'))

"""To use array , we have to import array module"""

from array import *
"""
    array is a module, containing the class array. So we can't use 'import array'
    
    You need to do array.array(...) or from array import array  """

x = array('i',[5,3,-2,3,4,3])                 #check out the chart of using bytes in array like we used 'i' for signed int(can have -ve,+ve values ) which is 2 bytes
                                              #we can't put even any float value if the array we used is of integer value
print(x)
""" 
    'b' :   Signed char   :        int        : 1 bytes
    'B' :  Unsigned char  :        int        : 1 bytes
    'u' :    Py_UNICODE   : unicode character : 2 bytes
    'h' :   Signed short  :        int        : 2 bytes
    'H' : unsigned short  :        int        : 2 bytes
    'i' :   Signed int    :        int        : 2 bytes
    'I' :  Unsigned int   :        int        : 2 bytes
    'L' :   Signed long   :        int        : 4 bytes
    'L' :  Unsigned long  :        int        : 4 bytes
    'f' :       Float     :       float       : 4 bytes
    'd' :      Double     :       float       : 8 bytes     """


y = array('i',[4,8,6,0,-2,7],)
print(y.buffer_info())                  #buffer_info gives the address,size of the array
print(y)                                #for example ,
                                        #               (19132616, 6)

print(y.reverse())                      #reverse will reverse the numbers
print(y)
print(y.reverse())


print(y[0])
print(y[1])
print()

for z in y:
    print(z)
print()

#OR

for i in range(6):                      #however by this method we have to specify exactly and not exceeding the array nummbers
    print(y[i])
print()
#To overcome this range issue we can use 'len(y)'

for j in range(len(y)):
    print(y[j])

print()

c = array('u',['a','g','b','f','h'])
print(c)

for b in c:
    print(b)
print()


newarray = y                                        # Copying array but without any modification in data or values
print(newarray)
print()
for o in newarray:
    print(o,end=',')
print()


newarray1 = array(c.typecode, (a for a in c))          #used to copy anyother array in a long way
print(newarray1)                                       #the above can be used if we want to assign values with some modifications like square, adding,etc
for k in newarray1:
    print(k)
print()

newarray2 = array(x.typecode, (a*a for a in x))        #ASSIGNING  values by squaring the original values in x
print(newarray2)
#using while insted of for loop
v=0                                                    # initialization
while v<len(newarray2):                                # condition
    print(newarray2[v])                                # statement
    v+=1                                               # increment/decrement


