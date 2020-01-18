from time import *

a =  input("Press ENTER to start")
seconds = 0
t = time()
while seconds< 100:
    print(seconds)
    sleep(1)
    seconds+=1

print(time()-t)