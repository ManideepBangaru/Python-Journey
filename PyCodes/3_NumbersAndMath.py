# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:43:52 2020

@author: Vanaja

"""

"""
integer An integer is a whole number with no decimal places

A floating-point number, or сoat for short, is a number with a
decimal place

"""

# we can see the data type using type()

type(1)

# we can convert string to int using int function

int("25")
25

""" we can also write integers as 1000000 or 1_000_000

An integer literal is an integer value that is written explicitly in your
code,

we can also write integers as 1000000.0 or 1_000_000.0 or 1e6

So 1e6 is equivalent to 1×10⁶. Python uses E-notation to display large floating point numbers:

For really large numbers, you can use E-notation. The third method
in the previous example uses E-notation to create a float literal

"""
# we can convert string to float using float function

float("10")
10.0


200000000000000000.0

2e+17
print(2e+400)

# we can also write 1/1000 as 

1e-4
0.0001

""" A floating-point literal is a floating-point value that is written ex￾plicitly
in your code. 1A сoating-point literal is a floating-point value that is written ex
Explicitly in your code. 1A сoating-point literal is a floating-point value that
is written ex￾plicitly in your code. 1
"""

""" Arithmetic Operators and Expressions  =================== """

# Addition: Addition is performed with the + operator

1+2

# The two numbers on either side of the + operator are called operands.

# we can add int and float

1.0 + 2

# Subtraction: To subtract two numbers, just put a - in between them:

1-1

5.0 - 4

5.0 - 1.0

# Whenever one of the operands is a float, the result is also a float.

1--5

3 -- 6

5 - (-1)

# Multiplication: To multiply two numbers, use the * operator:


3 * 3

2 * 8.0     # float * int retuns float 16.0

# Division: The / operator is used to divide two numbers

9 / 3       # output is 3.0

5.0 / 2     # output is 2.5 

""" Unlike addition, subtraction, and multiplication, division with the /
operator always returns a float

If you want to make sure that you get
an integer after dividing two numbers, you can use int() to convert
the result:
"""

int(9 / 3)

int(5.0 / 2)


""" Integer Division ===============

If writing int(5.0 / 2) seems a little long-winded to you, Python pro￾vides a
second division operator, //, called the integer division op￾erator:
    
"""

9 // 3

5.0 // 2   # 2.0 // returns a floating-point number if one of the operands is a float.

-3 // 2    # 2.0

""" 
The // operator first divides the number on the left by the number on
the right and then rounds down to an integer.

"""

1/0        # Python gives you a ZeroDivisionError 

# Exponents: You can raise a number to a power using the ** operator

2 ** 2
4

2 ** 3
8

2 ** 4
16

3 ** 1.5
5.196152422706632

9 ** 0.5
3.0

"""
For positive operands, the ** operator returns an integer if both
operands are integers, and a float if any one of the operands is a
floating-point number.
"""

# You can also raise numbers to negative powers:

2 ** -1           # nothing but 1/(2 ** 1)
0.5

2 ** -2           # nothing but 1/(2**2) 
0.25


""" The Modulus Operator =============================

The % operator, or the modulus, returns the remainder of dividing
the left operand by the right operand:

"""

5 % 3          # 3 divides 5 once with a remainder of 2
2

20 % 7         # Similarly, 7 divides 20 twice with a remainder of 6.
6

16 % 8
0

5 % -3
-1

-5 % 3
1

-5 % -3
-2


"""
These potentially shocking results are really quite well defined. To cal￾culate
the remainder r of dividing a number x by a number y, Python
uses the equation r = x - (y * (x // y)).
For example, to find 5 % -3, first find (5 // -3). Since 5 / -3 is about
-1.67, 5 // -3 is -2. Now multiply that by -3 to get 6. Finally, subtract
6 from 5 to get -1.

"""

"""
Arithmetic Expressions =========================
You can combine operators to form complex expressions. An expression is a
combination of numbers, operators, and parentheses that Python can compute, or
evaluate, to return a value.
"""

# Here are some examples of arithmetic expressions:

2*3 - 1
5

4/2 + 2**3
10.0

-1 + (-3*2 + 4)
-3

""" Math Functions and Number Methods =============================== """

# round(), for rounding numbers to some number of decimal places

# The round() function
# You can use round() to round a number to the nearest integer:

round(2.3)
2

round(2.7)
3

# round() has some unexpected behavior when the number ends in .5:

round(2.5)
2

round(3.5)    
4
# Python 3 rounds numbers according to a strategy called rounding ties to even

# You can round a number to a given number of decimal places by passing a
# second argument to round():

round(3.14159, 3)
3.142

round(2.71828, 2)
2.72

""" The abs() Function ========================

abs() always returns a positive number of the same type as its argu￾ment. 
That is, the absolute value of an integer is always a positive
integer, and the absolute value of a float is always a positive float.

"""

# To get the absolute value of a number in Python, you use the abs() function:

abs(3)
3

abs(-5)



""" The pow() Function ====================

pow() takes two
arguments. The first is the base, that is the number to be raised to a
power, and the second argument is the exponent.

"""

pow(2, 3)
8

# Just like **, the exponent in pow() can be negative:

pow(2, -2)
0.25


pow(2, 3, 2)       # pow(x, y, z) is equivalent to (x ** y) % z
0

#  First, 2 is raised to the power 3 to get 8. Then 8 % 2 is calculated, which
#  is 0 because 2 divides 8 with no remainder.


""" Check if a Float Is Integral ========================

Integers and floating-point numbers also have methods

Number methods aren’t used very often, but there is one that can be useful. 
Floating-point numbers have an .is_integer() method that re￾turns True
if the number is integral—meaning it has no fractional
part—and returns False otherwise:

"""

num = 2.5
num.is_integer()
False

num = 2.0
num.is_integer()
True

""" Exercise ================"""

"""
#  Write a script that asks the user to input a number and then displays
that number rounded to two decimal places. When run, your program should look like this:

    Enter    a    number:    5.432 
5.432 rounded to 2 decimal places is 5.43 """
    

num1 = input("Enter a number ")
# fnum = float(num1)
num = round( float(num1) , 2 )
print (str(num1) + " rounded to 2 decimal places is " + str (num))

"""
# Write a script that asks the user to input a number and then displays
the absolute value of that number. When run, your program should look like this 
Enter a number = -10
the absolute value of -10 is 10.0
"""

num = input("Enter a number ")
num1 = abs(float(num))
print( " The absoute value of that number is " + str( num1))

"""
# Write a script that asks the user to input two numbers by using the
input() function twice, then display whether or not the difference
between those two number is an integer. When run, your program
should look like this:
Enter a number: 1.5
Enter another number: .5
The difference between 1.5 and .5 is an integer? True!
If the user inputs two numbers whose difference is not integral,
the output should look like this:
Enter a number: 1.5
Enter another number: 1.0
The difference between 1.5 and 1.0 is an integer? False!
"""

a1 = input(" Enter first number : ")
a2 = input (" Enter second number : ")
a3 = (float(a1) - float(a2)).is_integer()
print(" The difference between " + str(a1) + " and " + str(a2) + " is an integer? " + str(a3))


# Print Numbers in Style

# to format the value of n in the above example to two decimal places

n = 7.125
print( f"The value of n is {n:.2f}")

"""
The colon (:) after the variable n indicates that everything after it is
part of the formatting specification. In this example, the formatting
specification is .2f.
"""

# When you format a number as fixed-point, it’s always displayed with
# the precise number of decimal places specified:

n = 1
print(f"The value of n is {n:.2f}")
print( f"The value of n is {n:.3f}")

# You can insert commas to group the integer part of large numbers by
# the thousands with the , option:

n = 1234567890
print( f"The value of n is {n:,}")     # The value of n is 1,234,567,890


n = 1234.56289
print(f"The value of n is {n:,.2f}")

'The value of n is 1,234.56'


"""
Another useful option is %, which is used to display percentages. The %
option multiplies a number by 100 and displays it in fixed-point format,
followed by a percentage sign.

"""

ratio = 0.9
print(f"Over {ratio:.1%} of Pythonistas say 'Real Python rocks!'")

"Over 90.0% of Pythonistas say 'Real Python rocks!'"


"""    Complex Numbers   ===============================


complex number is a number with two dis￾tinct components: a real component and 
an imaginary component.

For example, 1i + 2j is the complex
number with real part 1 and imaginary part 2

"""

n = 1 + 2j

n.real
1.0

n.imag
2.0

"""

Complex numbers also have a .conjugate() method that returns the
complex conjugate of the number:

"""

n.conjugate()
(1-2j)
    
"""

For any complex number, its conjugate is the complex number with
the same real part and an imaginary part that is the same in absolute
value but with the opposite sign. So in this case, the complex conju￾gate of 1 + 2j is 1 - 2j.


The .real and .imag properties don’t need parentheses after
them like the method .conjugate() does.


"""    

a = 1 + 2j
b = 3 - 4j

a + b
(4-2j)


a - b
(-2+6j)


a * b
(11+2j)

a ** b
(932.1391946432212+95.9465336603419j)

a / b
(-0.2+0.4j)


y = 3.14

y.real
3.14

y.imag
0.0

y.conjugate()
3.14

