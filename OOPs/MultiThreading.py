class hello:
    def run(self):
        for i in range(5):
            print("hello - Hello")



class hi:
    def run(self):
        for i in range(5):
            print("hi - Hi")


t1 = hello()
t2 = hi()

# Here this execution is being done by main-thread
t1.run()
t2.run()
print("__________for hello hi________________")

""" As our cpu is a 4 core cpu , but we are using only a single core for this program/code
    lets execute the t1.run() and t2.run() simultaneously """
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello - Hello")

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi - Hi")

h1 = Hello()
h2 = Hi()

# Here , we are using multi-threading , h1 will be thread-1 and h2 will be thread-2
h1.run()
h2.run()
""" The above code will run the same as without thread because they are not actually making two 
    threads , to make the threads to work we hava to use h1.start() instead of h1.run() """
print("____________for thread____________________")
h1.start()      # When we use start that's when there's a new therad created to work parallely
h2.start()
""" Here above , you may ask why are we using start instead of our defined run
    that is because, there is a built-in run() function in threading module which 
    initiates when we use start()
    
    you will see that the above will still feel like we are not making use of threads
    that is because we are printing the statement only 5 times , try to make the for loop
    for like 100 times , than you will see that sometimes there will be Hello and other times
    there will be Hi"""
print("___________for start___________________")

class Bello(Thread):
    def run(self):
        for i in range(100):
            print("Bello - Hello")

class Bi(Thread):
    def run(self):
        for i in range(100):
            print("Bi - Hi")

print("________for Read Bello starts here")
b1 = Bello()
b2 = Bi()

# Here , we are using multi-threading , h1 will be thread-1 and h2 will be thread-2
b1.start()
b2.start()
print("__________for 100 Times Bello____________")
""" You can see that there will be parallely printing of Bello_Hello and Bi_Hi as
    there will be mixing up of these statements in order
    Hence , they are being executed in parallel (to say) MULTI-THREADING
    You can say that our system is so fast for doing such multiThreading task that we can see
    the mixing or order, collisions
    
    TO make it go like in an order we have SCHEDULERS,
    We can also see the working of multi-Threading by implementing a sleep() time between statements"""

print("________for Read Nello starts here")
from time import *

class Nello(Thread):
    def run(self):
        for i in range(20):
            print("Nello - Hello")
            sleep(0.5)

class Ni(Thread):
    def run(self):
        for i in range(20):
            print("Ni - Hi")
            sleep(0.5)


n1 = Nello()
n2 = Ni()

# So now there will be printing of one statement at a time while also multi-threading being in working in shodows
n1.start()
n2.start()
print("Bye")
""" we will see that Bye will be printed in between the execution the the n1 and n2 threads
    that is because currently there are 3 threads in total that are working right now
    n1 thread , n2 thread and main-thread
    and this Bye is in the main-Thread , hence main thread will execute Bye irrespective of the completion
    of the n1 and n2 thread , so that it will be printed in between"""
""" You will see the first printing statement (Nello - Hello) than printing of (Ni - HI) as 
    there is a time gap of 0.5 sec so while the one is having sleep time the other's printing will be done
    and then it will go to sleep and the first printing will take place again
    
    There will also be Collisions , what that means basically is that , there will be times when
    the execution of both printing statements will be at the same time and hence a collision will occur
    
    To even make sure that this thing doesn't happen we can include a sleep() between the n1.start() and n2.start()"""

""" Multi-Threading works like wonders when gaming as when we play games, there are many objects
    for example, we , enemy , cars , helicoptors, etc. So when one is being executed we can use multithreading
    so that all the enemy , cars helicoptors will be moving at the same time
    and that's what happens in games
    In games, there is no necessary requirement that if the user has to input command to make something
    move on the screen , even if the user haven't throwed any input the enemies, cars ,grass will still be moving
    on the screen """

""" There is a way through which we can make THe BYE statement to be printed at the end i.e.
    after the n1 and n2 has finished their execution
    which is by using join()"""

print("Here we will see how the execution of the Bye will work at the end")
class Pello(Thread):
    def run(self):
        for i in range(20):
            print("Pello - Hello")
            sleep(0.5)

class Pi(Thread):
    def run(self):
        for i in range(20):
            print("Pi - Hi")
            sleep(0.5)


p1 = Nello()
p2 = Ni()

p1.start()
p2.start()

p1.join()       # this join() will make sure to execute the below code after p1 has joined the main-thread
p2.join()       # same goes for p2 thread

print("Bye")

""" Here I have made a mess of this MultiThreading file and see how many classes and threades
    I have made , which is why it will be executing like hell
    
    Try to learn its way be taking and executing only one class at a time and deleting or commenting
    the rest.
"""