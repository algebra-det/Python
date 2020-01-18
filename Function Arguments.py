
# See how the address change

def update(x):
    print(id(x))
    x = 8
    print(x)
    print(id(x))

update(19)
print()

def updater(x):
    print(id(x))
    x = 0
    print(x)
    print(id(x))

a = 10
print(id(a))
updater(a)
print(id(a))
print("a is : ",a)

"""
    SO if the question is ' Do Python use PASS BY VALUE or PASS BY REFERENCE
    The answer is ' None of them ' 
        
"""

print()
print()

def updator(x):
    print(id(x))
    x[1] = 77
    print(x)
    print(id(x))

b = [10,4,6,34,9]
print(b)
print(id(b))
updator(b)
print(id(b))
print("b is : ",b)

"""
    you can see and examamine the address
    variables with int,float,bool,tuple,str,frozenset are immutable so that they will change the address while changing the values
    lists,set amd dict are mutable so they will have the same address while changing the values    
    
    Immutable:              Mutable:
      bool                    list
      int                     set
      float                   dict
      tuple
      str
      frozenset
    
    Immutable will change the address for new assignment such as integer values
    Mutable will not change the address for new assignment values such as in list,
        where the values will change at addresses
"""