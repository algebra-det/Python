""" we use open() to open a file, although we have to specify what we want to do with the file
    which is called 'mode'.
    for example, we use
                            r = read
                            w = write
                            a = appending
                            rb = read in binary
                            wb = write in binary
                            ab = append in binary
    by default if we donot specify the mode ,it will automaticaly take 'r' i.e. reading ."""

f = open('data.txt','r')
print(f)
print(f.read())
print()

g = open('data.txt','r')
print(g.readline())         #1
print(g.readline())         #2
print(g.readline(5))        #3 , it will print 5 characters from line #3

toWrite = open('abc','w')
toWrite.write("Hi Guys , My name is Akash Chauhan\n")

toAppend = open('abc','a')
toAppend.write("\nHello")

h = open('data.txt','r')

for data in h:
    toWrite.write(data)

i = open('MultiThreading.png','r')      # here we are using a image file
#for j in i:
#    print(j)
""" the i with open('MultiThreading.png','r') will not work with r mode, as there is no string value
    in a image file, we have to use 'rb' , here b is used to define binary"""

j = open("MultiThreading.jpg",'rb')
for k in j:                         # it will give you a large binary code of this image file
    print(k)

# Lets create a file in which we will copy the binary data of the image file
j1  = open("CopyOfImage.JPG",'wb')
for k in j:
    j1.write(k)





m = list(map(str,open('data.txt')))
print(m)

"""
To open a text file, use:
fh = open("hello.txt", "r")

To read a text file, use:
fh = open("hello.txt","r")
print fh.read()

To read one line at a time, use:
fh = open("hello".txt", "r")
print fh.readline()

To read a list of lines use:
fh = open("hello.txt.", "r")
print fh.readlines()

To write to a file, use:
fh = open("hello.txt","w")
write("Hello World")
fh.close()

To write to a file, use:
fh = open("hello.txt", "w")
lines_of_text = ["a line of text", "another line of text", "a third line"]
fh.writelines(lines_of_text)
fh.close()

To append to file, use:
fh = open("Hello.txt", "a")
write("Hello World again")
fh.close()

To close a file, use
fh = open("hello.txt", "r")
print fh.read()
fh.close()
"""