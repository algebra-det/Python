"""
    When we code or make a program, there are gonna be bugs, and if the program has thousands of line of code
    It becomes very haptic and hard to debug it
    So we break down the program into modules,
    for example,
        Suppose we have a program that do 4 things -  ABCD
        Instead of writing the whole code into a single page
            we break it down into -
                                    module A
                                    module B
                                    module c
                                    module D
        a module can also be said as a file
    SO that if some error occurs in any module than it won't effect the other modules
    And hence easy for dubugging
    As we have seperated these modules, we can REUSE them in other programs too

We have just created Calc module at Myproject
"""

# In order to use that calc module we use simple import terms just as we used to import arrays
import Calc

a = 8
b = 9

c = Calc.add(a,b)
print(c)
print(Calc.div(6,2))
print()
"""
    In order to not use Calc. again and again
    we can import everyting from Calc by
        
        from Calc import *
"""
from Calc import *

d = add(7,4)
print(d)

print(sub(9,4))
print(multi(56,9))

import Smallest_Multiple                    #This will call multiple() two time once from the next line'50' and other from the Smallest_multiple module
Smallest_Multiple.multiple()                # importing executes all the statements from the module if we are not using __name__

from fibonacci_function import *           # Here we used __name__ in this fibonacci_function module and hence it will not execute the whole code of module
fibonacci()
