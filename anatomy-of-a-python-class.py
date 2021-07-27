"""
Notes from Anatomy of a Python Class from EuroPython 2021
"""

# Instance dictionary takes precedence to class dictionary

# When working with dictionaries you are working with the instance and class dictionary

# Define dummy class
class myClass:
    pass

# Define simple function
def say_hello():
    print('Hello')

# Assign the function to the class  - myfunc is pointing to the function, it is not redefining it
myClass.myfunc = say_hello

myClass.myfunc()

# Print the class dictionary
print()
print(myClass.__dict__)

# You can redefine the functions within the class

class Calculator:

    # The staticmethod annotation will modify the behaviour of the function, wrapping the function - telling it to only expect 2 inputs here
    @staticmethod
    def add(x, y):
        return x + y


# Class methods
"""
Use the classmethods annotation to define a class method. This tells the method to expect the class object as the first argument
to a given method rather an instance object. This means class methods have access to all class attributes.

The decorator will change the object type
"""


# Properties
"""
Use a @property decorator to force consumers of the class to go through setters and getters get_attr, set_attr
"""

class myClass:

    def __init__(self):
        self._myattr = 1

    def get_attr(self):
        return float(self._myattr)

    def set_attr(self, value):
        self._myattr = value

    myattr = property(get_attr, set_attr)


# Instead of the above you can use a property

class myClassprop():

    def __init__(self):
        self._myattr = 1

    @property
    def myattr(self):
        return float(self._myattr)

    @myattr.setter
    def myattr(self, value):
        self._myattr = value



