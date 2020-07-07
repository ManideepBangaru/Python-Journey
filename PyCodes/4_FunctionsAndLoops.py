# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Challenge: Track Your Investments -------------------------------------------------------------------

# My investment at the beginning is $ 100
# After 1 year with 5% of increase in my investment
FirstYearReturn  = 100 + 100 * 0.05
FirstYearReturn

# After 2 year with 5% increase in my investment from my First year is 
SecondYearReturn = 105 + 105 * 0.05
SecondYearReturn 

# defining a function for the above operation
# 1) principal amount
# 2) Rate of Interest
# 3) No.of.Years

# short cut to comment a line is (ctrl + 1)

def Invest(principal,Roi,yrs):
    for i in range(yrs):
        Return = principal + (principal * Roi)
        print('Returns for %s year = %s'%((i+1),round(Return,2)))
        principal = Return
    print("I'm happy")
        
Invest(100,0.05,4)
Invest(500,0.10,5)

# Understanding Scope in Python -----------------------------------------------------------------------
""" When you assign a value to a variable, you are giving that value a name. 
Names are unique. For example, you can’t assign the same name to two different numbers.
"""
x = 2
x = 4

x = "Hello World"

# example for local variable
def func(): 
    x=2
    print('Inside func, x value is %s'%x)

func()

# example for global variable
print('outside func, x value is %s'%x)

# Scope Resolution -------------------------------------------------------------------------------------
x = 5

def outer_func(): 
    y=3
    def inner_func(): 
        z=x+y
        return z
    return inner_func()

outer_func()

# ------------------- Another example

# here we are declaring total with global scope
total = 0

def add_to_total(n):
#   Here the total variable is assigned to right side operation
    """
    First, while total + n is being calculated, it will search for total value in local scope and clashes
    as the 'total' is referenced before assignment, hence it won't go to the global scope and hence,
    throws out error
    """
    total = total + n

add_to_total(5)

print(total)





