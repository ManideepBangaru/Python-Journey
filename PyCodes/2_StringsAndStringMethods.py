# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:46:51 2020
"""
"""

Collections of text in Python are called strings. Special functions called String Methods

Strings are one of the fundamental Python data types. The term data type refers
to what kind of data a value represents. Strings are used to represent text.

The string data type has a special abbreviated name in Python: str.

"""

# Determine the data type of given value

word = "Hello"
type(word)

# type() is used to determine the data type of given value

# other way

type("Hello")


"""
Whenver we create a string by surrounding text with quotaion marks the sting is 
called string literal

Strings have a length, which is the number of characters contained in string

Characters in a string appear in a sequence, meaning each character has a 
numbered position in the string

"""
# Create a String

string1 = 'Hello'
string2 = "1234"

"""
The quotes surrounding a string are called delimiters because they
tell Python where a string begins and where it ends. When one type
of quotes is used as the delimiter, the other type of quote can be used
inside of the string:
"""

string3 = "We're #1!"
string4 = 'I said, "Put it over by the llama."'


# Determine the length of the string

len("abc")

# other way

word = "Manideep"
len(word)

# len() is used to find the length of the string

"""
To deal with long strings, you can break the string up across multiple
lines into a multiline string

"""


""" we can also write multiline strings using backslash method"""

paragraph = "Notice that you don’t have to close each line with a quotation mark\
             you can just use backslash "
print(paragraph)

 
# Multiline strings can also be created using triple quotes as delimiters
# (""" or '''). Here is how you might write a long paragraph using this
# approach:

multiline_string = """ Notice that you don’t have to close each line with a quotation mark\
             you can just use backslash """

"""
Triple-quoted strings have a special purpose in Python. They
are used to document code. You’ll often find them at the top
of a .py with a description of the code’s purpose. They are also
used to document custom functions.

When used to document code, triple-quoted strings are called
docstrings. You’ll learn more about docstrings
"""

# Print a string that spans multiple lines, with whitespace preserved.

print("""An example of a
        string that spans across multiple lines
        that also preserves whitespace.""")

""" =============== Concatenation =============================== 

Concatenation , which joins two strings together 

String Concatenation

Two strings can be combined, or concatenated, using the + operator:

"""
string1 = "Manideep"
string2 = "Bangaru"
magic_string = string1 + string2
print(magic_string)

""" ===================== String Indexing         ============================

Each character in a string has a numbered position called an index.
You can access the character at the Nth position by putting the num￾ber N in
between two square brackets ([ and ]) immediately after the string

"""

name = "ManideepBangaru"
print(name[6])

"""
In Python—and most other programming languages—counting
always starts at zero. To get the character at the beginning of a string,
you need to access the character at position 0:
"""
name = "ManideepBangaru"
print(name[0])

# To get last letter of string need to give -1 

0   1   2   3   4   5   6   7   8   9   10
V   a   n   a   j   a   m   b   i   k    a
-11-10 -9  -8  -7  -6  -5  -4  -3  -2   -1

name = "ManideepBangaru"
print(name[-1])

# to print the string in reverse

name = "ManideepBangaru"
print(name[::-1])

# to get the string from 3 rd letter

name = "ManideepBangaru"
print(name[2:])
 
# we can also get final character using len() 

name = "ManideepBangaru"
lastletter = len(name)-1
print(name[lastletter])

# simplest way

name = "ManideepBangaru"
print(name[-1])


""" ===================   String Slicing     ============================="""


# to print the first three letters

""" we can access each character by index and
concatenate them, like this:
"""
name = "Manideep"
firstthree = name[0] + name[1] + name[2]
print(firstthree)

""" You can extract a portion of a string, called a substring, by inserting a
colon between two index numbers inside of square brackets, like this:"""

name = "ManideepBangaru"
print(name[0:3])

name = "ManideepBangaru"
print(name[:3])

# to print the full string

name = "ManideepBangaru"
print(name[:])

# The [0:3] part of name[0:3] is called a slice

"""
name[13:15] attempts to get the
thirteenth and fourteenth characters, which don’t exist. Instead of
raising an error, the empty string "" is returned.
"""

name = "ManideepBangaru"
print(name[13:15])

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



""" ===============   Strings Are Immutable    =============================

Strings are immutable, which means that you can’t change
them once you’ve created them. For instance, see what happens when
you try to assign a new letter to one particular character of a string:

"""

# trying to change the first letter of the word

name = "Manideep"
name[0] = "B"  # which throws an error
    
name = "Mani"
name = "W" + name[1:]
print(name)    


""" Strings come bundled with special functions called string methods that can
be used to work with and manipulate strings======== 

=================== Converting String Case ===============================

"""
# To convert a string to all lower case letters, you use the string’s .lower()

name = "MANIDEEP"
print(name.lower())

# To convert a string to all upper case letters, you use the string’s .upper()

name = "ManideepBangaru"
print(name.upper())

"""
As we already know strings are immutable

name.upper() or name.lower() returns a new string  "VANAJA"  or "vanaja", which 
is re-assigned to the name variable. This overrides the original string assigned to
"name".
"""
name = "MANIDEEP"
name = name.lower()
print(name)

"""

The dot (.) tells Python that what follows is the name of a method—
the lower() method in this case.

We will refer to the names of string methods with a dot at the
beginning of them. So, for example, the .lower() method is writ￾ten with a dot,
instead of lower().

The reason we do this is to make it easy to spot functions that
are string methods, as opposed to built-in functions like print()
and type().

Compare the .upper() and .lower() string methods to the general￾purpose len() function

"""

""" len() is a stand-alone function If you want to determine
the length of the name ,  call the len() function directly,
like this:
"""

name = "ManideepBangaru"
len(name)


"""
On the other hand, .upper() and .lower() must be used in conjunction
with a string. They do not exist independently
"""

""" Removing Whitespace From a String========================================

There are three string methods that you can use to remove whitespace
from a string:
    
1. .rstrip()
2. .lstrip()
3. .strip()

"""
name = "Manideep Bangaru          "
print(name.rstrip())    # removes white space from the left side of the string

name = "          Manideep Bangaru"
print(name.lstrip())     # removes white space from the right side of the string 

name = "      Manideep Bangaru      "
print(name.strip())     # removes white space from both the sides of the string


""" None of the .rstrip(), .lstrip(), and .strip() methods remove
whitespace from the middle of the string. In each of the pre￾vious examples the 
space between “Vanaja Ambika” is always preserved. """



""" Determine if a String Starts or Ends With a
Particular String            ==============================================
"""

# To check if a string starts with ap

word = "Apple"
word.startswith("ap")  # Here the output is False 
word.endswith("plE")   # Here the output is False 

"""  .startswith() , .endswith() methods are case-sensitive """

word = "Apple"
word.startswith("Ap")  # Here the output is True 
word.endswith("ple")   # Here the output is True 


""" ==================  interact with user input =============================
"""
# program to ask the user to input some info

prompt = " Hey , What's up ? "
user__input = input(prompt)
print( " You said: " , user__input)

# program to ask user to input some info and convert that to upper care and print the same

response = input (" Hello , How are you? ")
provided_response = response.upper()
print(provided_response)

""" ================ Working With Strings and Numbers  ========================

Strings and Arithmetic Operators
"""
num = "2"
print(num+num)   # here the ouput is 22 as the value 2 is entered as string 


num = "3"
print(num * 3)   # here the ouput is 333 as the value 3 is entered as string 


# we cant add int to string datatype

num = "2"
num1 = num + 3
print(num1)      

""" when we execute above program we encounter a TypeError in console as 2 is given 
as string and we are trying to add integer 3 to "2" """ 

""" ==================== Converting Strings to Numbers  =======================

"""

num = input("Enter a number to be doubled ")
newnum = num*2
print(newnum)    # Here the output is 

"""When you enter a number, such as 2, you expect the output to be 4, but
in this case, you get 22. Remember, input() always returns a string, so
if you input 2, then num is assigned the string "2", not the integer 2.
Therefore, the expression num * 2 returns the string "2" concatenated
with itself, which is "22".

To overcome this we have to convert the datatypes

To perform arithmetic on numbers that are contained in a string, you
must first convert them from a string type to a number type

int() stands for integer and converts objects into whole numbers,
while float() stands for сoating-point number and converts ob￾jects into numbers
with decimal points
"""

num1 = input("ener a number ")
num2 = input ("enter another number ")
prod = int (num1) * int (num2)
print(prod)


num = 10
print(float(num))   # output is 10.0 as we have converted num from int to float


""" ================= Converting Numbers to Strings =============================

Streamline Your Print Statements

Suppose you have a string name = "Zaphod" and two integers heads = 2
and arms = 3. You want to display them in the following line: Zaphod
has 2 heads and 3 arms. This is called string interpolation, which is
just a fancy way of saying that you want to insert some variables into
specific locations in a string

"""

num1 = input("ener a number ")
num2 = input ("enter another number ")
prod = int (num1) * int (num2)
print( "the product of " + str(num1 ) + " and " + str (num2) + " is " + str( prod))


"""
print( "the product of " + str(num1 ) + " and " + str (num2) + " is " + str( prod))

instead we can use easy method to combine strings 

=============== formatted strings or f-strings ====================

"""
# program to print value of first number raised to the power of second number

num1 = input("enter first number ")
num2 = input ("enter second number ")
num3 = int(num1) ** int(num2)
print(f"{num1} to the power of {num2} is {num3} ")

""" we can also do the same with .format() method """


num1 = input("enter first number ")
num2 = input ("enter second number ")
num3 = int(num1) ** int(num2)
print("{} to the power of {} is {} " .format(num1 , num2 , num3 ))

"""
f-strings are shorter, and sometimes more readable, than using .for￾mat().

"""

# another best way is using %s 

num1 = input("enter first number ")
num2 = input ("enter second number ")
num3 = int(num1) ** int(num2)
print(" %s to the power of %s is %s " %( num1 , num2 , num3) ) 

""" ===========  Find a String in a String  ==========================

One of the most useful string methods is .find(). As its name implies,
you can use this method to find the location of one string in another
string—commonly referred to as a substring

""" 

phrase = "the surprise is in here somewhere"
phrase.find("surprise")
4

"""
The value that .find() returns is the index of the first occurrence of the
string you pass to it. In this case, "surprise" starts at the fifth character
of the string "the surprise is in here somewhere" which has index 4
because counting starts at 0.
"""
# If .find() doesn’t find the desired substring, it will return -1 instead:


phrase = "the surprise is in here somewhere"
phrase.find("dkjsdfzvzxbvkjdfsdjk")

# we can also call string methods directly on string literal

"the surprise is in here somewhere".find("surprise")


# when we call find method matching is done exactly character by character and is
# case sensitive 

"the surprise is in here somewhere".find("Surprise")
-1 # returns -1 as it is case sensitive

# find() only returns the first index of the first appearance

"I put a string in your string".find("string")
8

word = "Do % whatever @ you$ # want to do ? * : "

# To get the string after @

word[word.find("@")+1:]

# To get the string after #

word[word.find("#")+1:]

# to get the string between @ and $ 

word[word.find("@")+1: word.find("$")]

# to get the string from ? 

word[word.find("?"):]

# to get the string before @

word[:(word.find("@"))]

# to get string before * (including *)

word[:(word.find("*")+1)]

# to print the total string  excluding characters that are present between @ and #

word[:(word.find("@"))] + " " + word[word.find("#")+1:]

# to print the string excluding first character D

word[word.find("D")+1:]

# to print the string reverse 

word[::-1]


"""

replace() is used to find and replace the value
"""

my_story = "I'm telling you the truth; nothing but the truth!"
my_story.replace("the truth", "lies")


# Replace every occurrence of the character "s" with "x" in the string

text = "somebody said something to samantha"
text1 = text.replace("s" , "x")
print(text1)
