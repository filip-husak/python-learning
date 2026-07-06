my_string = "Hello, World!"
print(my_string)

string1 = "Python is fun." + " " + "Let's learn it together."
print(string1)

### String Concatenation and Interpolation
name = "Alice"
word = "is not okay."
name_and_word = f"{name} {word}"
print(name_and_word)

### way to transform a number into a string
name = 'John Doe'
age = 26

name_and_age = name + (" " + str(age))
print(name_and_age) # John Doe 26

name = 'John Doe'
age = 26

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26


### f-strings, typical for python. same as $ in C# - interpolation
name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15

### Slicing
# my_string = "Hello World!"
print(my_string[0]) # H
print(my_string[7]) # W
print(my_string[-1]) # ! - od zadu (-)
print(my_string[0:5]) # Hello - 0,1,2,3,4
print(my_string[7:12]) # World - 7,8,9,10,11

### String Methods
my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD

lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world

title_my_str = my_str.title()
print(title_my_str)  # Hello World

my_str_strip = '  hello world  '

trimmed_my_str = my_str_strip.strip()
print(trimmed_my_str)  # "hello world"

replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world

