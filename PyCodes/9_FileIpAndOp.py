#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 22:43:53 2020

@author: manideepbangaru
"""

"""
So far, you’ve written programs that get their input from one of two places: from the program itself or 
from the user
"""
# Files and the File System -----------------------------------------------------------------------------------
"""
A file is just a sequence of bytes called contents of the file

Each byte in a file can be thought of as an integer with a value between 0 and 255 including both the end points

The bytes are the values that are stored on a physical storage of a device when the file is saved

When you access a file on the computer, the contents are read in the correct sequence of bytes

As a programmer, it’s your job to properly interpret the contents when you open a file. This might 
sound difficult, but Python does a lot of the hard work for you
"""

# Working with FIlepaths in Python -----------------------------------------------------------------------------

import pathlib

"""
The pathlib module contains a class called Path that is used to represent a file path
"""

# Creating path objects
"""
There are several ways to create a new Path object:
1. Fromastring
2. With Path.home() and Path.cwd() class methods 
3. With the / operator

The most straightforward way to create a Path object is from a string.
"""

# Creating Path Objects from Strings
"""
For instance, the following creates a Path object representing the macOS file path 
"/Users/David/Documents/hello.txt"
"""
# on MACos
path = pathlib.Path('/Users/manideepbangaru/Documents/RealPythonLearn/FileIPOPFiles/hello.txt')

# on WINDOWSos
path = pathlib.Path(r'C:\Users\manideepbangaru\Documents\RealPythonLearn\FileIPOPFiles\hello.txt')
path = pathlib.Path('C:/Users/manideepbangaru/Documents/RealPythonLearn/FileIPOPFiles/hello.txt')

"""
Besides creating a Path object from a string, the Path class has class methods that return Path objects of 
special directories. 

Two of the most useful class methods are Path.home() and Path.cwd()
"""
pathlib.Path.home()
pathlib.Path.cwd()

"""
Every operating system has a special directory for storing data for the currently logged in user.
This directory is called the user’s home directory. The location of this directory depends on the
operating system

Windows      : C:\Users<username>
macOS        : /Users/<username>
Ubuntu Linux : /home/<username>

"""
"""
The Path.home() class method creates a Path object representing the home directory regardless of which 
operating system the code runs on
"""
home = pathlib.Path.home()

"""
The Path.cwd() class method returns a Path object representing the current working directory, or CWD. 

The current working directory is a dynamic reference to a directory that depends on where a process on 
the computer is currently working.
"""
currDir = pathlib.Path.cwd()

# Using the / Operator
home/'Documents'/'RealPythonLearn'/'FileIPOPFiles'/'hello.txt'

# Absolute vs. Relative Paths -------------------------------------------------------------------------------
"""
A path that begins with the root directory in a file system is called an absolute path. Not all file paths 
are absolute. A file path that is not absolute is called a relative path
"""
path = pathlib.Path('/Users/')
path.is_absolute() #True

# Relative path for macos
path = pathlib.Path('Photos/')
path.is_absolute() #False

# You can extend a relative path to an absolute path using the forward slash (/) operator
home / pathlib.Path('Photos/')

# Accessing File path components
path = pathlib.Path.home()
list(path.parents)

"""
Notice that the list of the directories are returned in reverse order from how they appear in the file path. 
That is, the last directory in the path is the first directory in the list of parent directories
"""
# You can iterate over the parent directories in a for loop

for directory in path.parents:
    print(directory)

# To access parent directory
path.parent

# If the file path is absolute, you can access the root directory of the file path with the .anchor attribute
path.parent.anchor

"""
Note that .anchor returns a string, and not another Path object. 
For relative paths, .anchor return an empty string
"""
path = pathlib.Path('hello.txt')

"""
The .name attribute returns the name of the file or directory that the path points to
"""
home = pathlib.Path.home() / 'Hello_world.txt'
home.name
home.stem
home.suffix

# Checking Whether Or Not a File Path Exists ------------------------------------------------------------------
path = pathlib.Path.home() / "hello.txt"
path.exists()

"""
You can check whether or not a file path refers to a file or a directory. To check if the path is a file, 
use the .is_file() method
"""
path.is_file()

# Use the .is_dir() method to check if the file path refers to a directory
path.is_dir()
home.is_dir()

# Review Exercises ---------------------------------------------------------------------------------------------
"""
1. Create a new Path object to a file called my_file.txt in a folder called my_folder/ in your computer’s home 
directory. 

Assign this Path object to the variable name file_path.
"""
file_path = pathlib.Path.home() / 'my_folder' / 'my_file.txt'

"""
2. Check whether or not the path assigned to file_path exists.
"""
file_path.exists()

"""
3. Print the name of the path assigned to file_path. The output
should be my_file.txt.
"""
file_path.name

"""
4. Print the name of the parent directory of the path assigned to
file_path. The output should be my_folder.
"""
file_path.parent.name

# Common File System Operations --------------------------------------------------------------------------------
"""
let’s take a look at some common file operations and how you do them in Python
"""

# Creating Directories and Files

from pathlib import Path

new_dir = Path.home()/'Documents'/'RealPythonLearn'/'FileIpOpFiles'
new_dir.mkdir()
new_dir.exists()
new_dir.is_dir()
""" If you try to create a directory that already exists, you get an error"""

"""
If you want to create a new directory if it doesn’t exists, but avoid rais- ing the FileExistsError if 
it does, then you can set the options exist_ok parameter of the .mkdir() method to True
"""
new_dir.mkdir()
new_dir.mkdir(exist_ok=True)

"""
Setting exist_ok to True when calling .mkdir() is equivalent to the following code
"""
if not new_dir.exists():
    new_dir.mkdir()

"""
Now let’s see what happens if you try to create a subdirectory within a directory that does not exist
"""
nested_dir = new_dir/'folder_a'/'folder_b'
nested_dir.mkdir()

"""
To create any parent directories needed in order to create the target directory, set the optional 
parents parameter of .mkdir() to True
"""
nested_dir.mkdir(parents=True)

""" Putting all together """
nested_dir.mkdir(parents=True,exist_ok=True)
nested_dir.exists()

"""
Now let’s look at how to create files. Create a new Path object called file_path for the path 
new_directory/file1.txt
"""
file_path = new_dir/'file1.txt'

"""
There is no file in new_directory/ called file1.txt, so the path doesn’t exist yet"""
file_path.exists()

# You can create the file using Path.touch() method
file_path.touch()
file_path.exists()

# you can't create a file in the directory that doesn't exist
file_path = new_dir / "folder_c" / "file2.txt"
file_path.touch()

"""
Unlike .mkdir(), the .touch() method has no parents parameter that you can set to automatically create 
an parent directories. This means that you need to first create any directories needed before calling 
.touch() to create the file

For instance, you can use .parent to get the path to the parent folder for file2.txt and then call 
.mkdir() to create the directory
"""
file_path.parent.mkdir()

""" with folder_c folder created, we can go ahead and create file2.txt """
file_path.touch()
file_path.exists()
file_path.is_file()
file_path.is_dir()

"""
Now that you know how to create files and directories, let’s look at
how to get the contents of a directory
"""

# Iterating over directory contents -------------------------------------------------------------------------
for path in new_dir.iterdir():
    print(path)

list(new_dir.iterdir())
"""
Notice that .iterdir() only returns items that are directly contained in the new_directoy/ folder. 
That is, you can’t see the path to the file that exists in the folder_c/ directory
"""

# Searching for files in the directory ----------------------------------------------------------------------
for path in new_dir.glob("*.txt"):
    print(path)

list(new_dir.glob('*'))

paths = [new_dir / "program1.py",
         new_dir / "program2.py",
         new_dir / "folder_a" / "program3.py",
         new_dir / "folder_a" / "folder_b" / "image1.jpg",
         new_dir / "folder_a" / "folder_b" / "image2.png"]

for path in paths:
    path.touch()

# The '*' Wild card
list(new_dir.glob('*.py'))
list(new_dir.glob('*1*'))
list(new_dir.glob('1*'))

# The '?' Wild card
list(new_dir.glob('program?.py'))
list(new_dir.glob('?older_?'))

# You can also combine the * and ? wildcards
list(new_dir.glob('*1.??'))

# The [] Wildcard
list(new_dir.glob('program[13].py'))

# Recursive Matching With The ** Wildcard
list(new_dir.glob("**/*.txt"))

"""
There is also a shorthand method to doing recursive matching called .rglob(). 
To use it, pass the pattern without the **/ prefix
"""
list(new_dir.rglob("*.txt"))

# Moving and deleting Files and Folders
source = new_dir / "file1.txt"
destination = new_dir / "folder_a" / "file1.txt"
source.replace(destination) 

"""
The .replace() method is called on the source path. The destina- tion path is passed to .replace() as a single 
argument. Notice that .replace() returns the path to the new location of the file

If the destination path already exists, .replace() overwrites the destination with the source file without raising any 
kind of exception. This can cause undesired loss of data if you aren’t careful.

You may want to first check if the destination file exists, and move the file only in the case that it does not
"""

if not destination.exists():
    source.replace(destination)














