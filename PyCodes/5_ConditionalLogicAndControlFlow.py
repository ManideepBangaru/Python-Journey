#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:48:17 2020

@author: manideepbangaru
"""

# conditional expressions or boolean expressions ------------------------------------------------------

# In python there are boolean values which takes either one of two values 'true' or 'false'
type(True)
type(False)

# The result of evaluating a conditional is always a boolean value:
1 == 1
4 >= 8

"""In Python, strings are ordered lexicographically, which is a fancy way to say they are ordered as
 they would appear in a dictionary. So you can think of "a" < "b" as asking whether or not the letter
 a comes before the letter b in the dictionary."""
 
"a" == "a"
"a" == "b"
"a" <  "b"
"a" >  "b"

"""For each of the following conditional expressions, guess whether they evaluate to True or False. 
Then type them into the interactive window to check your answers :"""

1 <= 1
1 != 1
1 != 2
"good" != "bad" 
"good" != "Good" 
123 == "123"

"""For each of the following expressions,fill in the blank (indicatedby __) with an appropriate 
boolean comparator so that the expression evaluates to True:"""
3 __ 4
10 __ 5
"jack" __ "jill" 
42 __ "42"

# Add Some Logic -----------------------------------------------------------------------------------
"""
In addition to boolean comparators, Python has special keywords called logical operators that can be 
used to combine boolean expressions. There are three logical operators: and, or, and not.
"""
# The 'and' Key word
#---------------------
1<2 and 3<4 #Both are True, True
2<1 and 4<3 #Both are False, False
1<2 and 4<3 #Second statement is False, False
#1 < 2 is True, but 4 < 3 is False, so their combination is False.
2<1 and 3<4 #FirststatementisFalse

# The 'or' Key word
#---------------------
1<2 or 3<4 #Both are True, True
2<1 or 4<3 #Both are False, False
1<2 or 4<3 #First statement is True, True
#1 < 2 is True, but 4 < 3 is False, so their combination is True.
2<1 or 3<4 #Second statement is True, True

# The 'not' keyword
#---------------------

not True
not False

not True == False
False == True
False == not True
"""Looking again at the expression False == not True, not has a lower precedence than == in the order 
of operations. This means that when Python evaluates False == not True, it first tries to 
evaluate False == not which is syntactically incorrect.
You can avoid the SyntaxError by surrounding not True with parenthe-ses:"""
False == (not True)

# Building Complex Expressions ----------------------------------------------------------------------
"""
You can combine the and, or and not keywords with True and False to create more complex expressions.
 Here’s an example of a more com- plex expression:"""
 
True and not (1 != 1)
True and not (False)
True and True
("A" != "A") or not (2 >= 3)
(False) or not (False)
False or (not False)
True and False == True and False # should be interpreted as True and (False == True) and False,
                                 # as '==' has higher precedence
(True and False) == (True and False)

# Exercise ----------------------------
(1 <= 1) and (1 != 1) # False
not (1 != 2) # False
("good" != "bad") or False # True
("good" != "Good") and not (1 == 1) # False

# Add parentheses where necessary so that each of the following expressions evaluates to True:
False == (not True)
(True and False) == (True and False)
not(True and "A" == "B")

# Control the Flow of Your Program ------------------------------------------------------------------

# if condition ------------------------
if (2 + 2 == 4):
    print('2 and 2 is 4')

#-----
    
grade = 50

if grade >= 70:
    print("You passed the class!")
    
print('Thank you for attending the class !!!')

# -----

grade = 40

if grade >= 70:
    print('You passed the class!')

if grade < 70:
    print('You screwed with the class :(')

print('Thank you for attending the class !!!')


# else condition -------------------------

grade = 40

if grade >= 70:
    print('You passed the class :)')
else:
    print('You screwed with the class :(')
    
print('Thank you for attending the class !!!')


# elif condition --------------------------
grade = 90 

if (grade >= 70):
    print('you passed in first class')
elif (grade < 70) and (grade >= 50) :
    print('you passed in second class')
elif (grade < 50) and (grade >= 35) :
    print('you just passed for the name sake')
else:
    print('you just ruined your life !!! :(')

print('Thank you for attending the class !!! enjoy maadi :)')
    
# nested if -------------------------------

sport = input('Which sport are the players playing ?\n')
pl1_sc = input('Player 1 Score = ')
pl2_sc = input('Player 2 Score = ')

if sport.lower().replace(' ','') == 'basketball':
    if pl1_sc > pl2_sc :
        print('Player 1 won the match')
    elif pl1_sc < pl2_sc :
        print('Player 2 won the match')
    elif pl1_sc == pl2_sc :
        print('Match Draw !!! Waste of time ...')
elif sport.lower().replace(' ','') == 'golf':
    if pl1_sc < pl2_sc :
        print('Player 1 won the match')
    elif pl1_sc > pl2_sc :
        print('Player 2 won the match')
    elif pl1_sc == pl2_sc :
        print('Match Draw !!! Waste of time ...')
else:
    print('Register the game first !!!')

# Another way
sport = input('Which sport are the players playing ?\n')
pl1_sc = input('Player 1 Score = ')
pl2_sc = input('Player 2 Score = ')

if (sport.lower().replace(' ','') == 'basketball') and (pl1_sc > pl2_sc) :
    print('Player 1 won the match')
elif (sport.lower().replace(' ','') == 'basketball') and  (pl1_sc < pl2_sc):
    print('Player 2 won the match')
elif (sport.lower().replace(' ','') == 'golf') and (pl1_sc < pl2_sc):
    print('Player 1 won the match')
elif (sport.lower().replace(' ','') == 'golf') and (pl1_sc > pl2_sc):
        print('Player 2 won the match')
elif (sport.lower().replace(' ','') == 'basketball') or (sport.lower().replace(' ','') == 'golf') and (pl1_sc == pl2_sc) :
    print('Match Draw !!! Waste of time ...')
else:
    print('please have a look at your face in the mirror !!!')
    
    
# script to input a word and to determine whether the length of that string is less 
# than 5 or greater than 5 or equals to 5 using if, elif
    
word = input('Enter a word\n')
if (len(word) == 5):
    print(' The length of %s is 5 ' %word)
elif (len(word)< 5):
    print(' The length of %s is less than 5 ' %word)
else:
    print(' The length of %s is greater than 5 ' %word)
    

    
# To find the factors of a number

num = int(input('Enter a positive integer:'))
if (num >= 0):
    for n in range(num+1):
        if (n > 0) and (num % n == 0):
            print('%s is a factor of %s' %(n , num))
        elif(n == 0):
            print('Enter value greater than 0')
else:
    print('Please enter a positive integer')           

# Break out of the pattern ----------------------------------------------------------------------
    
"""you’ll learn how to write if statements that are nested in for loops and learn about 
two keywords — break and continue — that allow you to more precisely control the flow of execution 
through a loop."""    

"""
The following example uses a for loop with an if statement to compute and display the sum 
of all even integers less than 100:"""

sum_of_evens = 0
for n in range(1, 100): 
    if n % 2 == 0:
        sum_of_evens = sum_of_evens + n 

print(sum_of_evens)
    
# break
# ------

"""
The break keyword tells Python to literally break out of a loop. That is, the loop stops completely 
and any code after the loop is executed.
For example, the following code loops over the numbers 0 to 100, but stops the loop when the number 75
is encountered:"""
    
for i in range(0,100):
    if i == 75 :
        print('breaking the loop at 75')
        break
    print(i)

# continue
# --------    
"""
The continue keyword is used to skip any remaining code in the loop body and continue on to the next 
iteration.
For example, the following code loops over the numbers 0 to 100, print- ing each number as is goes, 
but skips the number 75:"""

for i in range(0,100):
    if i == 75:
        print('skipping the loop at 75')
        continue
    print(i)

"""
To summarize, the break keyword is used to stop a loop if a certain condition is met, 
and the continue keyword is used to skip an iteration of a loop when a certain condition is met."""

# for...else Loops ---------------------------------------------------------------------
"""
Loops can have their own else clause in Python, although this structure isn’t used very frequently."""

phrase = "it marks the spot"

for character in phrase: 
    if character == "X":
        break 
else:
    print("There was no 'X' in the phrase")

"""
Any code in the else block after a for loop is executed only if the for loop completes without 
encountering a break statement."""

# Example    
""" Here’s a practical example that gives a user three attempts to enter a password:"""

for n in range(3):
    password = input("Password: ") 
    if password == "I<3Bieber":
        break
    print("Password is incorrect.") 

else:
    print("Suspicious activity. The authorities have been alerted.")

# Some more Examples -----------------

"""
1.Using break,write a program that repeatedly asks the user for some input and only quits if the 
user enters "q" or "Q"."""

while True:
    input_val = input('Please enter an alphabet : ')
    if input_val.lower() == 'q':
        break
    

"""
2. Using continue, write a program that loops over the numbers 1 to 50 and prints all numbers 
that are not multiples of 3."""

for n in range(1 , 50):     
    if ((n%3) != 0):         
        print(n)         
        continue

"""
using break or continue, write a program that loops over repeatedly, to check whether a input variable 
'name' is equal to 'manideep', if satisfied continue asking input 'hobby' and print both name and hobby
 else print 'better luck next time' """

while True:
    input_val = input('Enter a name : ')
    if input_val.lower() == 'manideep':
        input_hob = input('Enter a hobby : ')
        print('Name is %s and hobby is %s'%(input_val,input_hob))
        break
    else:
        print('better luck next time')

# Recover From Errors --------------------------------------------------------------------------------

# ValueError :
#--------------
        
int("I'm good")

# TypeError :
#---------------

's' + 2

# NameError :
#-------------
print(ImNotDeclared)

# ZeroDivisionError :
#---------------------

1/0

# OverflowError :
#-----------------

pow(2.0,1_000_000)

# Exception Handling --------------------------------------------------------------------------------
    
try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("That was not an integer")

# -------------------------
def divide(num1, num2):
    try:
        print(num1 / num2)
    except (TypeError, ZeroDivisionError):
        print("encountered a problem")

divide("Manideep",2)
divide(2,0)

# --------------------------
def divide(num1, num2):
    try:
        print(num1 / num2)
    except TypeError:
        print("It is a Data Type error")
    except ZeroDivisionError:
        print('It is a Zero division error')

divide("Manideep",2)
divide(2,0)

# ---------------------------

"""
1. Write a script that repeatedly asks the user to input an integer, displaying a message to “try again”
 by catching the ValueError that is raised if the user did not enter an integer.
Once the user enters an integer, the program should display the number back to the user and end without
crashing."""

while True:
    try:
        num = int(float(input('Enter an integer : ')))
        print(num)
        break
    except:
        print('Please enter an integer :x !!!')


"""
2. Write a program that asks the user to input a string and an integer n. Then display the character at 
index n in the string.

Use error handling to make sure the program doesn’t crash if the user does not enter an integer or the 
index is out of bounds. The program should display a different message depending on what error occurs."""

# solution at beginner level, using complex conditions
while True:     
    word = input('Enter a string : ')      
    if word != "":         
        try:             
            num = int(float(input('Enter the index : ')))             
            if (num <= len(word)) and (num != "") and (num > 0):                 
                result = word[num-1]                 
                print(result)                 
                break             
            else:                
                print('Enter a valid index number')                         
        except:             
            print("type error")     
    else:           
        print("Please enter a string")


# solution at intermediate level, leaving burden on user
while True:
    word = input('Enter a string : ')
    if len(word)>0:
        while True:
            try:
                num = int(input('Enter a index : '))
                result = word[num-1]
                print('Result is %s'%result)
                break
            except:
                print('bad index, please enter an integer within length of string')
        break
    else:
        print('Enter a string with atleast greater than 0 length')


"""
define a function, to take input of two numbers as parameters and reverse these two
numbers and return the output of the sum"""

def RevSum(num1,num2):
    num1 = str(num1)
    num2 = str(num2)
    nnum1 = ''
    nnum2 = ''
    for i in range(len(num1)):
        nnum1 = nnum1 + num1[len(num1)-(i+1)]
    for i in range(len(num2)):
        nnum2 = nnum2 + num2[len(num2)-(i+1)]
    nnum1=int(nnum1)
    nnum2=int(nnum2)
    return nnum1+nnum2

RevSum(123,456)

def RevSum(num1,num2):
    num1 = str(num1)
    num2 = str(num2)
    nnum1 = int(num1[::-1])
    nnum2 = int(num2[::-1])
    return nnum1+nnum2

RevSum(123,456)

################################################################################
word = 'Manideep'
# Manideep
# 01234567

#word[:]        # Print all elements
#word[2:4]      # Prints index 2 to index 4 of the given string
#word[2:-2]     # Prints index 2 to second element from last
#word[::]       # Print all elements
#word[::-1]     # Reverse of the string
#word[:2:]      # Picks only first two elements
#word[:2:-1]    # First 2 excluded (0,1 places) - from last condsider every -1 counting (-1 to -1, i.e, every element)
#word[:2:-2]    # First 2 excluded (0,1 places) - from last condsider every -1 counting (-1 to -2)
#word[:2:-3]    # First 2 excluded (0,1 places) - from last condsider every -1 counting (-1 to -3)
#word[:4:3]     # 012012012 - Every zero element is taken
#word[:4:2]     # 010101010 - Every zero element is taken
#word[:4:1]     # 000000000 - Every zero element is taken
#word[1:5]      # anid
#word[1:5:2]    # every second element, so ai is the answer
#word[1:6]      # anide
#word[1:6:-2]   # will not work
#word[1:6][::-2]# from last every second element, so eia is the answer 
#word[1:6][::2]

word[::1]    
word[::-1]
word[1:6][::2]
word[1:6][::-2]   
word[1:5][::2] 
word[1:5][::-2]
################################################################################

# The random module

# loading a package
import random

# if package doesn' exist, install
# !pip install random

# if i want to get a random number between 1 to 10
num = random.randint(1,10)
num = random.random()

# whenever you don't know what a function does, execute as below
random.randint?
random.randrange(1,100)