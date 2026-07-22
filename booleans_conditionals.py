### Booleans and Conditionals
print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True
print("")
### Basic conditional statement - If syntax
age = 18

if age >= 18:
    print('You are an adult') # You are an adult

age = 12

if age >= 18:
    print('You are an adult') # Nothing shows up in the terminal

print("")
### elif statement - else if in C#
age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child') # You are a child
### More complex example with multiple elif statements
age = 2

if age >= 65:
    print('You are a senior citizen')
elif age >= 30:
    print('You are an adult in your prime')
elif age >= 18:
    print('You are a young adult')
elif age >= 13:
    print('You are a teenager')
elif age >= 3:
    print('You are a young child')
else:
    print('You are a toddler or an infant') # You are a toddler or an infant
print("")

### Truthy and Falsy values
print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True

### The and operator - can be used to combine multiple conditions
age = 20
is_citizen = True

if age >= 18 and is_citizen:
    print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')

### The or operator - can also be used to combine multiple conditions
age = 20
is_citizen = False

if age >= 18 or is_citizen:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')

age = 19
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')

### Last operator of this file - not - can be used to reverse the truthiness of a value
is_raining = False
print(not is_raining) # True
print("")
print(not '') # True, because empty string is falsy
print(not 'Hello') # False, because non-empty string is truthy
print(not 0) # True, because 0 is falsy
print(not 1) # False, because 1 is truthy
print(not False) # True, because False is falsy
print(not True) # False, because True is truthy


