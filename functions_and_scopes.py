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

# Example of Global Scope
def