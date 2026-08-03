# Local scope (L): Variables defined in functions or classes.
#
# Enclosing scope (E): Variables defined in enclosing or nested functions.
#
# Global scope (G): Variables defined at the top level of the module or file.
#
# Built-in scope (B): Reserved names in Python for predefined functions, modules, keywords, and objects.

# Example of Local Scope
def my_func():
    my_var = 10
    print(my_var)

# My_var is defined in the local scope of my_func, so it can only be accessed within that function.
my_func() # 10

print(my_var) # NameError: name 'my_var' is not defined

# Example of Enclosing Scope
def outer_func():
    outer_var = 20

    def inner_func():
        print(outer_var) # Accessing the variable from the enclosing scope

    inner_func() # 20

print(outer_var) # NameError: name 'outer_var' is not defined

# Another example of Enclosing Scope - 
def outer_func():
    msg = 'Hello there!'
    res = ""  # Declare res in the enclosing scope

    def inner_func():
        nonlocal res  # Allow modification of an enclosing variable
        res = 'How are you?'
        print(msg)  # Accessing msg from outer_func()

    inner_func()
    print(res)  # Now res is accessible and modified

outer_func()

# Output:
# Hello there!
# How are you?

# Example of Global Scope - can be accessed from anywhere in the module
global_var = "Global variable string"

def access_global_var():
    print(global_var)  # Accessing the global variable

access_global_var() # Global variable string
print(global_var) # Global variable string

# I can use 
my_var_1 = 7

def show_vars():
    global my_var_2
    my_var_2 = 10
    print(my_var_1)
    print(my_var_2)

show_vars() # 7 10

# my_var_2 is now a global variable and can be accessed anywhere in the program
print(my_var_2) # 10
