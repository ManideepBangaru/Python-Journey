#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 18:57:25 2020

@author: manideepbangaru
"""

# --------------------------- Modules and Packages ----------------------------------------------------------------
"""
As you gain experience writing code, you will eventually work on projects that are so large that keeping all 
of the code in a single file becomes cumbersome.

Instead of writing a single file, you can put related code into separate files called modules. 
Individual modules can be put together like building blocks to create a larger application
"""

"""
There are four main advantages to breaking a program into modules:
1. Simplicity: Modules are focused on a single problem
2. Maintainability: Small files are better than large files 
3. Reusability: Modules reduce duplicate code
4. Scoping: Modules have their own namespaces
"""

"""
A namespace is a collection of names, such as variable names, function names, and class names. 
Every Python module has its own namespace
"""

# Working with modules --------------------------------------------------------
"""
A Module is a file containing python code, which can be re-used in another python code files
"""
"""
1) Create a folder by name MyProject in the current directory
2) Create adder.py file which has a function by name add(x,y), which should return sum of two numbers
3) save this file in this MyProject folder
4) Create main.py which has import adder and used adder.add(x,y), remember that both should be in same path
"""
"""
Refer to MyProject folder to finish off with adder.py, which has two functions
1) def add(x,y): return x+y
2) def double(x): return x+x
"""

"""
There are two ways in import statement

1) import <module>
2) import <module> as <alias_name>
3) from <module> import <required function>
4) from <module> import <function1>,<function2>
"""

# Review Excercise ------------------------------------------------------------
"""
1. Create a module called greeter.py that contains a single function greet(). 
This function should accept a single string parameter name print the text Hello {name}! to 
the interactive window with {name} replaced with the function argument.
"""
"""
2. Create a module called main.py that imports the greet() function from greet.py and calls 
the function with the argument "Real Python".
"""

# Working with packages -------------------------------------------------------
"""
Modules allow you to divide a program in to individual files that can be reused as needed. 
Related code can be organized into a single module and kept separate from other code
"""
"""
Package take this organizational structure one step further by allowing you to group 
related modules under a single namespace
"""

# Creating packages
"""
A package is a folder that contains one or more python modules.
It must also contain a special module called __init__.py

Example of the package structure is as below:

mypackage/
|
|-- __init__.py
|
|-- module1.py
|
|-- module2.py

"""

"""
The __init__.py module doesn’t need to contain any code! It only needs to exist so that Python 
recognizes the mypackage/ folder as a Python package
"""

"""
Using your computers file explorer, or whatever tool you are comfort- able with, create a new folder 
somewhere on your computer called packages_example/. Inside of that folder, create another folder 
called mypackage/.

The packages_example/ folder is called the project folder, or project root folder, because it contains 
all of the files or folders in the packages_examples project. The mypackage/ folder will eventually 
become a Python package. It isn’t one right now because it doesn’t contain any modules
"""

"""
1) In packages_example folder create main.py script which will have comment main.py
2) In mypackage folder create __init__.py which will have comment as __init__.py
3) In mypackage folder only create module1.py, module2.py which have respective comments
"""

# Importing modules from sub packages --------------------------------------------------------------------
"""
A package is just a folder containing one or more Python modules, one of which must be names __init__.py, 
so it’s entirely possible to have the following package structure

mypackage
|
|-- mysubpackage/
|    |
|    |-- __init__.py
|    |
|    |-- module3.py
|
|
|-- __init__.py
|
|-- module1.py
|
|-- module2.py
    
"""
"""
A package nested inside of another package is called a subpackage. For example, the mysubpackage folder 
is a subpackage of mypackage be- cause it contains an __init__.py module, as well as a second module 
called module3.py
"""














































