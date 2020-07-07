#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 06:01:50 2020

@author: manideepbangaru
"""

#---------------------------------------------------- Classes vs Instances --------------------------------------------
"""

Classes are used to create user-defined data structures. Classes also have special functions, called methods, 
that define behaviors and actions that an object created from the class can perform with its data.

It’s important to note that a class just provides structure. A class is a blueprint for how something should 
be defined. It doesn’t actually provide any real content itself. The Dog class may specify that the name and 
age are necessary for defining a dog, but it will not actually state what a specific dog’s name or age is.

While the class is the blueprint, an instance is an object built from a class that contains real data.
An instance of the Dog class is not a blueprint anymore. It’s an actual dog with a name, like Miles, 
who’s four years old.

Put another way, a class is like a form or questionnaire. It defines the needed information. After you fill out 
the form, your specific copy is an instance of the class. It contains actual information relevant to you.

You can fill out multiple copies of a form to create many different in- stances, but without the form as a 
guide, you would be lost, not know- ing what information is required. Thus, before you can create individual
instances of an object, you must first specify what is needed by defining a class.

"""

# How to define a Class ----------------------------------------------------------------------------------------------

"""
All class definitions start with the class keyword, which is followed by the name of the class and a colon. 
This is similar to the signature of a function, except that you don’t need to add any parameters in parentheses. 
Any code that is indented below the class definition is considered part of the class’s body.
"""
# Here is an example of a simple Dog class:

class Dog:
    pass

"""
To define the properties, or instance attributes, that all Dog objects must have, you need to define a special 
method called .__init__(). This method is run every time a new Dog object is created and tells Python what 
the initial state—that is, the initial values of the object’s properties—of the object should be.

references the class instance. This variable is almost universally named self. After the self argument, you 
can specify any other arguments required to create an instance of the class.
"""
class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

"""
Functions that belong to a class are called instance methods because they belong to the instance of a class. 
For example, list.append() and string.find() are instance methods.
"""
"""
While instance attributes are specific to each object, class attributes are the same for all 
instances—which in this case is all dogs. In the next example, a class attribute called species is 
created and assigned the value "Canis familiaris"
"""
class dog:
    # class attribute
    species = "Canis familiaris"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

"""
You should use class attributes whenever a property should have the same initial value for all instances 
of a class. Use instance attributes for properties that must be specified before an instance is created.
"""

# Instantiate an Object--------------------------------------------------------------------------------------------
"""
Once a class has been defined, you have a blueprint for creating—also known as instantiating—new objects. 
To instantiate an object, type the name of the class, in the original CamelCase, followed by parentheses 
containing any values that must be passed to the class’s .__init__() method.
"""

# Lets create a simple dog class without any __init__

class dog:
    pass

a = dog()
a
b = dog()
b

a == b

"""
What this means is that even though the a and b objects are both instances of the Dog class and have the 
exact same attributes and methods—namely, no attributes or methods, in this case—a and b represent two 
distinct objects in memory.
"""
type(a) == type(b)


# Class and Instance Attributes
class dog:
    species = "Canis familiaris"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

micky = dog("Micky",'14')
ruby = dog("Ruby",12)

"""
After the Dog instances are created, you can access their instance at- tributes by using dot notation """

micky.name
ruby.age

"""
Class attributes are accessed the same way """
micky.species
ruby.species

"""
One of the biggest advantages of using classes to organize data is that instances are guaranteed to have 
the attributes you expect
"""
micky.species == ruby.species

"""
Contrast this to the method of using lists to represent similar data structures that you saw at the beginning 
of the previous section. With a class you no longer have to worry that an attribute may be missing
"""
# Both instance and class attributes can be modified dynamically ------------------------------------------
micky.age = 10
micky.age

ruby.species = 'Felis silvestris'
ruby.species
micky.species

"""
Now that you know the difference between a class and an instance, how to create instances and set class and 
instance attributes, the next step is to look at instance methods in more detail
"""
# Instance Methods -----------------------------------------------------------------------------------------
"""
Instance methods are functions defined inside of a class. This means that they only exist within the context 
of the object itself and cannot be called without referencing the object. Just like .__init__(), the first 
argument of an instance method is always self
"""

class Dog:
    
    species = 'Canis familiaris'
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    # Instance method
    def description(self):
        print('%s is %s years old'%(self.name,self.age))
    
    # Instance method
    def speak(self,sound):
        print('%s says %s'%(self.name,sound))
        
miles = Dog('Miles',8)
miles.description()
miles.speak('bow bow')

"""
The message displayed by print(miles) isn’t very helpful. You can change what gets printed by defining a 
special instance method called .__str__()
"""
# Let’s change .description() to .__str__() in the Dog clas

class Dog:
    
    species = 'Canis familiaris'
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    # Replace .description() with __str__()
    def __str__(self):
        return '%s is %s years old'%(self.name,self.age)
    
    # Instance method
    def speak(self,sound):
        print('%s says %s'%(self.name,sound))

miles = Dog('Miles',8)
print(miles) # works only when return is given, doesn't work when print() is used

"""
Methods like .__str__() are commonly called dunder meth- ods because they begin and end with double underscores.
"""

# Review Exercises ---------------------------------------------------------------------------------------
"""
1. Modify the Dog class to include a third instance attribute called coat_color that stores the color of the 
dog’s coat as a string. Store your new class in a script and test it out by adding the following code at the 
bottom of the script:
    
philo = Dog("Philo", 5, "brown") 
print(f"{philo.name}'s coat is {philo.coat_color}.") 

The output of your script should be:
Philo's coat is brown.
"""

class Dog:
    
    species = 'Canis familiaris'
    
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    
    # Replace .description() with __str__()
    def __str__(self):
        return '%s is %s years old'%(self.name,self.age)
    
    # Instance method
    def speak(self,sound):
        print('%s says %s'%(self.name,sound))
        
philo = Dog('Philo', 5, 'brown')
print("%s's coat is %s"%(philo.name,philo.coat_color))


"""
2. Create a Car class with two instance attributes: .color, which stores the name of the car’s color as a string, 
and .mileage, which stores the number of miles on the car as an integer. Then instantiate two Car objects a blue car
with 20,000 miles, and a red car with 30,000 miles, and print out their colors and mileage. 

Your output should look like the following:
The blue car has 20,000 miles. 
The red car has 30,000 miles.
"""
class car:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return "The %s car has %s miles."%(self.color,self.mileage)

car1 = car('blue','20,000')
car2 = car('red','30,000')

print(car1)
print(car2)

"""
3. Modify the Car class with an instance method called .drive() that takes a number as an argument and adds 
that number to the .mileage attribute. Test that your solution works by instantiating a car with 0 miles, 
then call .drive(100) and print the .mileage attribute to check that it is set to 100.
"""
class car:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return "The %s car has %s miles."%(self.color,self.mileage)
    
    def drive(self,miles):
        self.mileage += miles

car1 = car('blue',20000)
car1.mileage
car1.drive(0)
car1.mileage
car1.drive(100)
car1.mileage

# Inherit from the other classes -----------------------------------------------------------------------------------

"""
Inheritance is the process by which one class takes on the attributes and methods of another. 
Newly formed classes are called child classes, and the classes that child classes are derived 
from are called parent classes.
"""
"""
Child classes can override and extend the attributes and methods of parent classes. In other words, child 
classes inherit all of the par- ent’s attributes and methods but can also specify different attributes and 
methods that are unique to themselves, or even redefine methods from their parent class.

The concept of object inheritance can be thought of sort of like genetic inheritance, even though the analogy
isn’t perfect.
For example, you may have inherited your hair color from your mother. It’s an attribute you were born with. 
You may decide that you want to color your hair purple. Assuming your mother doesn’t have purple hair, you have 
just overridden the hair color attribute you inherited from your mom.

You also inherit, in a sense, your language from your parents. If your parents speak English, then you will 
also speak English. One day, you may decide to learn a second language, like German. In this case you are 
extending attributes, because you have added an attribute that your parents do not have.
"""

# The object Class
"""
The most basic type of class is an object, which generally all other classes inherit from as their parent. 
When you define a new class, Python 3 implicitly uses object as the parent class, so the following two 
definitions are equivalent.
"""

class Dog(object):
    pass

# In Python 3, this is the same as below
class Dog:
    pass

# Dog Park Example
"""
Pretend for a moment that you are at a dog park. There are many dogs of different breeds at the park, 
all engaging in various dog behaviors.

Suppose now that you want to model the dog park with Python classes. The Dog class you wrote in the 
previous section can distinguish dogs by name and age, but not by breed.

You could modify the Dog class by adding a .breed attribute
"""
class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, age, breed): 
        self.name = name
        self.age = age 
        self.breed = breed

miles = Dog("Miles", 4, "Jack Russell Terrier") 
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

"""
Each breed of dog has slightly different behaviors. For example, bull- dogs have a low bark that sounds 
like “woof” but dachshunds have a higher pitched bark that sounds more like “yap”.

Using just the Dog class, you must supply a string for the sound argu- ment of the .speak() method every time 
you call it on a Dog instance:
"""
buddy.speak("Yap") 
# 'Buddy says Yap'
jim.speak("Woof") 
# 'Jim says Woof'
jack.speak("Woof")
# 'Jack says Woof'

"""
You can simplify the experience of working with the Dog class by creating a child class for each breed of dog. 
This allows you to extend the functionality each child class inherits, including specifying a default argument 
for .speak()
"""

# Parent Classes vs Child Classes ------------------------------------------------------------------------------
"""
Let’s create a child class for each of the three breeds mentioned above: Jack Russell Terrier, Dachshund, 
and Bulldog.
"""

class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, age): 
        self.name = name
        self.age = age 
    
    def __str__(self):
        return "%s is %s years old"%(self.name,self.age)
    
    def speak(self, sound):
        print("%s says %s"%(self.name,sound))

"""
Remember, to create a child class, you create new class with its own name and then put the name of the parent 
class in parentheses. The following creates three new child classes of the Dog class
"""
class JackRussellTerrier(Dog): 
    pass

class Dachshund(Dog): 
    pass

class Bulldog(Dog): 
    pass

miles = JackRussellTerrier('Miles',4)
buddy = Dachshund('Buddy',9)
jack = Bulldog('Jack',3)
jim = Bulldog('Jim',5)

"""
Instances of child classes inherit all of the attributes and methods of the parent class
"""

miles.species
buddy.name
jack.age
jim.speak('woof')

"""
To determine which class a given object belongs to, you can use the built-in type() function
"""
type(miles)

"""
What if you wanted to determine if miles is also an instance of the Dog class? You can do this with 
the built-in isinstance() function
"""
isinstance(miles,JackRussellTerrier)
isinstance(miles,Dog)
isinstance(miles,Bulldog)

"""
More generally, all objects created from a child class are instances of the parent class, although 
they may not be instances of other child classes
"""

# Extending the Functionality of a Parent Class --------------------------------------------------------------
class JackRussellTerrier(Dog):
    def speak(self, sound = 'Arf'):
        print('%s says %s'%(self.name,sound))

miles = JackRussellTerrier('Miles',5)
miles.name
miles.speak()
"""
Sometimes dogs make different barks, so if Miles gets angry and growls, you can still call .speak() 
with a different sound
"""
miles.speak('grrrrr')

"""
One advantage of class inheritance is that changes to the parent class will automatically propagate to their 
child classes. This occurs as long as the attribute or method being changed isn’t overridden in the 
child class.

For example, let’s say you decide to change the string returned by .speak() in the Dog class
"""
class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, age): 
        self.name = name
        self.age = age 
    
    def __str__(self):
        return "%s is %s years old"%(self.name,self.age)
    
    def speak(self, sound):
        print("%s barks %s"%(self.name,sound))

class JackRussellTerrier(Dog): 
    pass

class Dachshund(Dog): 
    pass

class Bulldog(Dog): 
    pass

class JackRussellTerrier(Dog):
    def speak(self, sound = 'Arf'):
        print('%s says %s'%(self.name,sound))

jim = Bulldog('Jim',5)
jim.speak('woof')

""" 
However, calling .speak() on a JackRussellTerrier instance won’t show the new style of output
"""
miles = JackRussellTerrier('Miles',5)
miles.speak()

"""
what if you want to use the parent's class style for miles?
Here we go....
"""
class JackRussellTerrier(Dog):
    def speak(self, sound = 'Arf'):
        return super().speak(sound)
miles.speak()

# Review Exercise --------------------------------------------------------------------------------------------
"""
Create a Golden Retriever class that inherits from the Dog class.
Give the sound argument of the GoldenRetriever.speak() method a default value of "Bark". 
Use the following code for your parent Dog class

class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, age):
         self.name = name 
         self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}
"""

class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, age):
         self.name = name 
         self.age = age
    
    def __str__(self):
        return "%s is %s years old"%(self.name,self.age)
    
    def speak(self, sound):
        return "%s says %s"%(self.name,sound)

class GoldenRetriever(Dog):
    def speak(self,sound = 'Bark'):
        print('%s says %s'%(self.name,sound))

dog1 = GoldenRetriever('Mickey',14)
dog1.age
dog1.speak()

"""
Write a Rectangle class that must be instantiated with two attributed: length and width. 
Add a .area() method to the class that returns the area (length * width) of the rectangle. 
Then write a Square class that inherits from the Rectangle class and that is instantiated with a 
single attribute called side_length. Test your Square class by instantiating a Square with a side_length of 4.
Calling the .area() method should return 16
"""
class Rectangle:
    
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self,side_length):
        super().__init__(side_length,side_length)

sq1 = Square(4)
sq1.area()

Rec1 = Rectangle(4,2)
Rec1.area()