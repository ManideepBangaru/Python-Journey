#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:35:56 2020

@author: manideepbangaru
"""

#------------------------------------------ Tuples, Lists, and Dictionaries ------------------------------------------
"""
A data structure models a collection of data, such as a list of numbers, a row in a spreadsheet, or a record in a 
database. Modeling the data that your program interacts with using the right data structure is often the key to writing 
simple and effective code.
"""
# --------------------------------------------- Tuples ----------------------------------------------
# Tuples are immutable ------------------------
"""
The word tuple comes from mathematics, where it is used to describe
a finite ordered sequence of values."""

a = (1,2,3)
type(a)

a = (1,)
type(a)

a = 'PYTHON'
type(a)
a

a = tuple(a)
type(a)
a

"""
tuple() only accepts a single parameter, so you can’t just list the values you want in the tuple as individual 
arguments. If you do, Python raises a TypeError
"""
b = tuple(1,2,3)

"""
You will also get a TypeError if the argument passed to tuple() can’t be interpreted as a list of values: """

b = 1
c = tuple(b)

"""
The word iterable in the error message indicates that a single integer can’t be iterated, which is to say that the 
integer data type doesn’t contain multiple values that can be accessed one-by-one.
"""

"""
The single parameter of tuple() is optional, though, and leaving it out produces an empty tuple:
"""
tuple()

()

# Tuples Have a Length --------------------------------------------------------
numbers = (1,2,3)
len(numbers)

# Tuples Support Indexing and Slicing -----------------------------------------

# This is in Strings
name = 'David'
name[1]

# Tuples also support index operations ----------------------------------------
values = (1, 3, 5, 7, 9)
values[4]
values[2:4]

# Tuples Are Immutable --------------------------------------------------------
"""
Like strings, tuples are immutable. This means you can’t change the value of an element of a tuple 
once it has been created.
"""
values[0] = 4

# Tuples Are Iterable ---------------------------------------------------------
vowels = ('a','e','i','o','u')

for n in range(0,len(vowels)):
    if (vowels[n] == 'e') or (vowels[n] == 'o'):
        print(vowels[n].upper())
    else:
        print(vowels[n])


# Tuple Packing and Unpacking -------------------------------------------------

# 3 ways of creating
a = (1,2,3)
a = tuple((1,2,3))
a = 1,2,3

var1,var2,var3 = 1,2,3

name, age, occupation = "David", 34, "programmer"

var = "David", 34, "programmer"

# No of variables on bothsides of '=' should be equal else it will throw an error
a,b,c,d,e = 1,2,3
a,b,c = 1,2,3,4,5

# Checking Existence of Values With 'in' --------------------------------------
vowels = ('a','e','i','o','u')
'n' in vowels
'e' in vowels

# Returning Multiple Values From a Function -----------------------------------
def addProd(x,y):
    return x+y,x*y

summ,Prodd = addProd(10,20)

# --------------------------------------------- Lists ----------------------------------------------
# List are mutable ----------------------------
"""
The list data structure is another sequence type in Python. Just like strings and tuples, 
lists contain items that are indexed by integers, starting with 0.
"""

"""
Unlike tuples, however, lists are mutable, meaning you can change the value at an index even
after the list has been created.
"""

# Creating Lists --------------------------------------------------------------
Names = ['Manideep','Vanaja','Baccha','Mounish','Manaswi']
type(Names)

data = ["one", 2, 3.0]
type(data)

Names = list(('Manideep','Vanaja','Baccha','Mounish','Manaswi'))
type(Names)


a = 'strings'
b = tuple(a)
c = list(b)

text = 'Here are the names, Manideep, Vanaja, Mounesh, bacha'
textList = text.split(',')
textList[1:]

# Split string on semi-colons
"a;b;c".split(";")

# Split string on spaces
"The quick brown fox".split(" ")

# Split string on multiple characters 
"abbaabba ".split("ba")

"abbaabba".split("c")

# Basic List Operations -------------------------------------------------------
"""
Indexing and slicing operations work on lists the same way they do on tuples."""

numbers = [1,2,3,4,5,6]
numbers[1]

# find length of a list
len(numbers)

# Create a new list slicing a list
newList = numbers[1:3]

# You can check for the existence of list elements using the 'in' operator
3 in numbers

# Because lists are iterable, you can iterate over them with a for loop
for i in range(len(numbers)):
    if (numbers[i]%2 == 0) :
        print('%s is a even number'%numbers[i])

# Changing Elements in a List -------------------------------------------------

# Replacing value in Tuple (immutability)
colors = ('Red','Yellow','Green','Blue')
colors[0] = 'White'
colors
  
# Replacing value in List (mutability)
colors = ['Red','Yellow','Green','Blue']
colors[0] = 'White'
colors

# slicing a list
colors = ['Red','Yellow','Green','Blue']
colors[1:3] = ['white','Black','Pink']
colors

colors = ['Red','Yellow','Green','Blue']
colors[1:3] = ['white']
colors

# adding and removing elements from the list
colors = ['Red','Yellow','Green','Blue']

# adding elements to the list
colors.insert(1,'white')
colors
colors.insert(101,'Pink')
colors
colors.insert(-1,'Burgundy')

# removing elements from the list
colors.pop(1)
colors
colors.pop(125)
colors
colors.pop(-1)
colors

# appending elements to the list
colors
colors.append('white')
colors

# inserting element in the last position when you don't know the index
colors.insert(len(colors),'black')
colors

# extend keyword
colors.extend(['purple','violet'])
colors

# example of what extend keword does internally
def extd(LisObj,elements):
    for i in elements:
        LisObj.append(i)
    return LisObj

extd(colors,['brown,cream color'])

# Lists of Numbers
nums = [1,2,3,4,5,6,7,8,9]

# General way
summ = 0
for i in nums:
    summ = summ + i
summ

# pythonic way
sum(nums)

nums = [1,2,3,"four",5]
sum(nums)

nums = [1,2,3,4,5,6,7,8,9]

# min function
min(nums)

# max function
max(nums)

# List Comprehensions ---------------------------------------------------------
numbers = (1,2,3,4,5)
numbers1 = [1,2,3,4,5]
# squares using list comprehension
squares = [i**2 for i in numbers1]
squares

# squares using basic method
squares = []
for i in numbers:
    squares.append(i**2)
squares

# cubes using list comprehension
cubes = [i**3 for i in numbers1]
cubes

# suppose you want to convert float numbers which are in string format
floatNums = ['1.22','4.879','3.33','5.22']
floatNumsRes = [float(i) for i in floatNums]

# Nesting, Copying, and Sorting Tuples and Lists ------------------------------

# Nesting a list
lis1 = [1,2,3,4]
lis2 = [[1,2],[3,4]]

lis1[1]
lis2[1][0]

# Copying a list
animals = ["lion", "tiger", "frumious Bandersnatch"]
large_cats = animals

large_cats.append('Tigger')
large_cats
animals

animals = ["lion", "tiger", "frumious Bandersnatch"]
large_cats = animals[:]

large_cats.append('Tigger')
large_cats
animals


matrix1 = [[1, 2], [3, 4]] 
matrix2 = matrix1[:]
matrix2[0] = [5, 6]
matrix2
matrix1

matrix2[1][0] = 1
matrix2
matrix1

"""
This happens because a list does not really contain objects themselves,
but references to those objects in memory. When you make a copy
of the list using the [:] notation, a new list is returned containing 
the same references as the original list. In programming jargon, 
this method of copying a list is called a shallow copy.

To make a copy of both the list and all of the elements it contains, 
you must use what is known as a deep copy

"""
import copy
matrix1 = [[1, 2], [3, 4]] 
matrix2 = copy.deepcopy(matrix1)
matrix2[0] = [5, 6]
matrix2
matrix1

matrix2[1][0] = 1
matrix2
matrix1

# Sorting Lists ---------------------------------------------------------------
# # Lists of numbers are sorted Alphabetically
colors = ["red", "yellow", "green", "blue"] 
colors.sort()
colors

# Lists of numbers are sorted numerically 
numbers = [1, 10, 5, 3]
numbers.sort()
numbers

# sort by len of a string
colors
colors.sort(key=len)
colors

# Challenge: List of lists-------------------------------------------------
"""
Define a function, enrollment_stats(), that takes, as an input, a list of lists 
where each individual list contains three elements: 
    (a) the name of a university, 
    (b) the total number of enrolled students, and 
    (c) the annual tuition fees.
"""
"""
enrollment_stats() should return two lists: the first containing all of the 
student enrollment values and the second containing all of the tuition fees.
"""
"""
Next, define a mean() and a median() function. Both functions should take a 
single list as an argument and return the mean and median of the values in 
each list.
"""

universities = [ ['California Institute of Technology', 2175, 37704],
                 ['Harvard', 19627, 39849],
                 ['Massachusetts Institute of Technology', 10566, 40732],
                 ['Princeton', 7802, 37000],
                 ['Rice', 5879, 35551],
                 ['Stanford', 19535, 40569],
                 ['Yale', 11701, 40500] ] 
#
#def mean():
#    studentMean  = totalStudents / len(universities)
#    tutionMean   = totalTuitionFees / len(universities)
#    print('\nStudent mean : %s\n\nTution mean : $ %s' %(round(studentMean , 2), round(tutionMean,2)))
#
#
#def enrollment_status():
#    totalStudents = 0
#    totalTuitionFees = 0
#    for i in range(len(universities)):
#        enrolledStudents , tutionFees = [universities[i][1] , universities[i][2]]
#        totalStudents = totalStudents + enrolledStudents
#        totalTuitionFees = totalTuitionFees + tutionFees
#    print('\nTotal Students : %s \n\nTotal Tuition Fees : $ %s' %( totalStudents,totalTuitionFees))     


def mean(x):        
    return sum(x)/len(x)

def median(x):
    x.sort()
    if (len(x)%2 == 0):
        return (x[int(len(x)/2)-1] + x[int(len(x)/2)])/2
    else:
        return x[int(len(x)/2)]

def enrollment_status():
    enrolledStudents = [i[1] for i in universities]
    TuitionFees = [i[2] for i in universities]
    SumStudents = sum(enrolledStudents)
    SumTuitionFees = sum(TuitionFees)
    
    MeanStudent = mean(enrolledStudents)
    MeanFees = mean(TuitionFees)
    
    MedianStudent = median(enrolledStudents)
    MedianFees = median(TuitionFees)
    
    print("************************************************************")
    print('\nTotal students : %s'%SumStudents)
    print('Total Fees : $ %s'%SumTuitionFees)
    
    print('\n\nStudent mean : %s'%round(MeanStudent,2))
    print('Student median : %s'%MedianStudent)
    
    print('\n\nTuition mean : $ %s'%round(MeanFees,2))
    print('Tuition median : $ %s'%MedianFees)
    
    print("\n************************************************************")

enrollment_status() 


# Store Relationships in Dictionaries -----------------------------------------
"""
Python dictionaries, like lists and tuples, store a collection of objects. 
However, instead of storing objects in a sequence, dictionaries hold information
in pairs of data called key-value pairs. That is, each object in a dictionary
has two parts: a key and a value.
"""
# Creating Dictionaries -----------------
Colors = {'Vanaja':'White',
           'Manideep' : 'Black',
           'Ravi' : 'Green',
           'baccha' : 'Pink'
        }

# You can also convert tuples into dictionaries using dict()
Colors = (('Vanaja','White'),
           ('Manideep','Black'),
           ('Ravi','Green'),
           ('baccha','Pink'))
type(Colors)

Colors = dict(Colors)        
type(Colors)
        
Colors        
        
# Creating an empty dictonaries using literal and dict keyword
{}
dict()        

# Accessing Dictionary Values -------------
Colors['Manideep']        
Colors['baccha']
        
# Why don't we use lists for this?
Names = ['Vanaja','Manideep','Ravi','baccha']
Colors1 = ['White','Black','Green','Pink']
Colors1[1]

for i in range(len(Names)):
    if Names[i] == 'Manideep':
        print(Colors1[i])

# Using Dictionaries we can directly pull out the color as relation exists
Colors['Manideep']

# Adding and Removing Values in a Dictionary ----------
Colors['Mouneesh'] = 'Purple'

# Sample use case of dictionaries ---------------------
"""
Create the database of people with their salaries ?
"""

SalaryDetails = {}
while True:
    inp = input('Do you want to enter the details (y/n) ?\n')
    if inp == 'y':
        Name = input('Enter the Person name = ')
        salary = input('Enter the Salary = ')
        SalaryDetails[Name] = salary
    else:
        break

SalaryDetails


# To remove an item from a dictionary, use the del keyword with the key for the value you want to delete:
del Colors['Manideep']
Colors

# Checking the Existence of Dictionary Keys
Colors['Mounika']
"""
with dictionaries. Whenever you see it, it means that an attempt was made to access a value using a key 
that doesn’t exist.
"""
'Mounika' in Colors
'Navya' in Colors # this means that the item doesn't match with any of the keys present in Dictionary

"""
With in, you can first check that a key exists before doing something with the value for that key:
"""

if 'Vanaja' in Colors:
    print('Vanaja likes %s colour'%Colors['Vanaja'])

# Iterating Over Dictionaries ------------------------------------------------
"""
Like lists and tuples, dictionaries are iterable. However, looping over a 
dictionary is a bit different than looping over a list or tuple.

When you loop over a dictionary with a for loop, you iterate over the dictionary’s keys
"""
for i in Colors:
    print('%s likes %s colour'%(i,Colors[i]))

"""
However, there is a slightly more succinct way to do this using the .items()
dictionary method. .items() returns a list-like object contain-ing tuples of 
key-value pairs. 

For example, Colors.items() returns a list of tuples of Names and their 
corresponding Colors
"""
Colors.items()

"""The object returned by .items() isn’t really a list. It has a special type 
called a dict_items"""

type(Colors.items())

SalaryDetails.items()

for name,color in Colors.items():
    print('%s likes %s colour'%(name,color))

# Dictionary Keys and Immutability --------------------------------------------
"""
There is no rule that says dic- tionary keys must all be of the same type
"""
Colors[0] = 'black'
Colors

# following is not allowed
"""
A key of the dictionary should be immutable"""
Colors[[1, 2, 3]] = "Bad"

# Valid Dictionary Key Types
# integers floats strings booleans tuples

# Nested Dictionaries ---------------------------------------------------------
Colors = {'Vanaja':{'col':'White','state':'Karnataka'},
           'Manideep' : {'col':'Black','state':'Telangana'},
           'Ravi' : {'col':'Green','state':'Karnataka'},
           'baccha' : {'col':'Pink','state':'Telangana'}
        }

Colors.items()

# The Value of Each key is a dictionary
Colors['Manideep']['col']
Colors['baccha']['state']

# ---------------------------- Review Exercises -------------------------------
"""
1. Create an empty dictionary named captains.

2. Using the square bracket notation, enter the following data into the 
   dictionary, one item at a time:

       'Enterprise': 'Picard'
       'Voyager': 'Janeway'
       'Defiant': 'Sisko'

3. Write two if statements that check if "Enterprise" and "Discovery" exist 
   as keys in the dictionary. Set their values to "unknown" if the key does 
   not exist.

4. Write a for loop to display the ship and captain names contained in the 
   dictionary. For example, the output should look something like this:
      "  The Enterprise is captained by Picard "

5. Delete "Discovery" from the dictionary.

6. Bonus: Make the same dictionary by using dict() and passing in the initial 
   values when you first create the dictionary.
"""

# 1)
captains = {}

# 2)
captains['Enterprise'] = 'Picard'
captains['Voyager'] = 'Janeway'
captains['Defiant'] = 'Sisko'
captains

# 3)
if "Enterprise" in captains:
    print('key present')
else:
    captains['Enterprise'] = 'unknown'

if "Discovery" in captains:
    print('key present')
else:
    captains['Discovery'] = 'unknown'
    print('Discovery added to the dictionary')

# 4)
for ship,captain in captains.items():
    print('The %s is captained by %s'%(ship,captain))

# 5)
del captains['Discovery']
captains

# 6)
captains = dict((('Enterprise','picard'),('Voyager','Janeway'),('Defiant','Sisko')))
captains


# -----------------------------------------------------------------------------

# Challenge: Capital City loop ------------------------------------------------
"""
Review your state capitals along with dictionaries and while loops! First, finish 
filling out the following dictionary with the remaining states and their 
associated capitals

Next, pick a random state name from the dictionary, and assign both the state 
and it’s capital to two variables. You’ll need to import the random module at 
the top of your program.

Then display the name of the state to the user and ask them to enter the capital. 
If the user answers, incorrectly, repeatedly ask them for the capital name until 
they either enter the correct answer or type the word “exit”.

If the user answers correctly, display "Correct" and end the program.

However, if the user exits without guessing correctly, display the correct 
answer and the word "Goodbye".

"""


import random

capitals_dict = {
'Alabama': 'Montgomery', 
'Alaska': 'Juneau', 
'Arizona': 'Phoenix', 
'Arkansas': 'Little Rock', 
'California': 'Sacramento', 
'Colorado': 'Denver', 
'Connecticut': 'Hartford', 
'Delaware': 'Dover', 
'Florida': 'Tallahassee', 
'Georgia': 'Atlanta',
}

while True:
    user_choice = input('Do you want to play the game again (y/n) ?\n')
    if user_choice == 'y':
        state = random.choice(list(capitals_dict.keys()))
        capital = capitals_dict[state]
        
        while True:
            user_answer = input('Capital of %s state is ?\n'%state)
        
            if user_answer.lower() == capital.lower():
                print('\nYour Answer is Correct !!!')
                break
            else:
                print('\nPlease try again\n')
            
    else:
        print('\nThanks for Playing !!!')
        break

# -----------------------------------------------------------------------------

# Sample exercise 1 -----------------------------------------------------------
import random
main_tick_value = {} 
while True:     
    choice = input("Do you want to raise a ticket (y/n) : ")     
    if choice == 'y':         
        name = input("Enter passenger name : ")         
        age = input("Enter passenger age : ")         
        tick_value = {'name' : name , 'age': age}         
        resultnum = ""         
        for n in range(10):             
            resultnum = resultnum + str(random.randint(0, 9))         
        main_tick_value[resultnum] = tick_value      
    else:         
        break

Tick_lis = []
Name_lis = []
age_lis = []

for i,j in main_tick_value.items():
    Tick_lis.append(i)
    Name_lis.append(j['name'])
    age_lis.append(j['age'])
    
# To create a table out of this data and export it to 
import pandas as pd
ReservationChart = pd.DataFrame({'Ticket Number':Tick_lis,
                                 'Passenger Name':Name_lis,
                                 'Passenger Age':age_lis})

ReservationChart.to_csv('/Users/manideepbangaru/Desktop/ReservChart.csv',index=False)


# Sample exercise 2 -----------------------------------------------------------
import random
Tick_lis = []
Name_lis = []
age_lis = []
while True:     
    choice = input("Do you want to raise a ticket (y/n) : ")     
    if choice == 'y':         
        name = input("Enter passenger name : ")
        Name_lis.append(name)
        age = input("Enter passenger age : ")
        age_lis.append(age)
        resultnum = ""         
        for n in range(10):             
            resultnum = resultnum + str(random.randint(0, 9))
        Tick_lis.append(resultnum)
    else:         
        break

Passenger_list = {}
for i,j,k in zip(Tick_lis,Name_lis,age_lis):
    Passenger_list[i] = {'name':j,'age':k}

# To create a table out of this data and export it to 
import pandas as pd
ReservationChart = pd.DataFrame({'Ticket Number':Tick_lis,
                                 'Passenger Name':Name_lis,
                                 'Passenger Age':age_lis})

ReservationChart.to_excel('/Users/manideepbangaru/Desktop/ReservChart.xlsx',index=False)

# -----------------------------------------------------------------------------