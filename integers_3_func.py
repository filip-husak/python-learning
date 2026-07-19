my_int_1 = 56
my_float_1 = float(my_int_1)

print(my_float_1) # 56.0
print(type(my_float_1))  # <class 'float'>

my_float = 9.555556
my_int = int(my_float)

print(my_int) # 9
print(type(my_int)) # <class 'int'>

## In python, we can convert even a string to an int/float.
my_str_int = '45'
my_str_float = '7.8'

converted_int = int(my_str_int)
converted_float = float(my_str_float)

print(converted_int, type(converted_int))  # 45 <class 'int'>
print(converted_float, type(converted_float))  # 7.8 <class 'float'>

### Few more functions for float and int operations
### Ustřihne na počet čísel za desetinou čárkou.
my_float_2 = 5.7757577789
round(my_float_2, 2) # 5.78

### Udělá absolutní hodnotu z čísla.
my_int_2 = -56
abs(my_int_2) # 56

### pow - Raises a number to the power of another number. - Je to číslo na několíkátou (2 ** 3 = 8), třetí argument je volitelný a určuje modulo (zbytek po dělení).
my_int_3 = 5
my_int_4 = 3
pow(my_int_3, my_int_4) # 125

print(pow(my_int_3, my_int_4, 10)) # 5 (125 % 10)

