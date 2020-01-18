from calc_for_Special_variable__name__ import add
""" See here we are only importing only add function so it will only print 'from add'
    But it will also execute the main() from the calc_for_Special_variable__name__ 
    hence both add() and sub() will be executed"""

def fun1():
    print("from Fun1")

def fun2():
    print("from Fun2")

def main():
    fun1()
    fun2()

main()

""" in order to stop that from happening we will use __name__'=="__main" 
    which basically means that the main will only be executed if the calc_module is being executed as standalone file
    and not be used as a module"""
import calc_for_Special_variable__name__2       # Here, there will be no execution of the whole code of this module as we have already declared if
calc_for_Special_variable__name__2.add()        # the if statement for main function