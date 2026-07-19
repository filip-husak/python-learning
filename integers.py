my_int_1 = 56
my_int_2 = 12

sum_ints = my_int_1 + my_int_2
print('Integer Addition:', sum_ints) # Integer Addition: 68

my_int_3 = 100
my_int_4 = 25
diff_ints = my_int_3 - my_int_4
print('Integer Subtraction:', diff_ints) # Integer Subtraction: 75

my_int_5 = 7
my_int_6 = 3
mult_ints = my_int_5 * my_int_6
print('Integer Multiplication:', mult_ints) # Integer Multiplication: 21

my_int_7 = 55
my_int_8 = 2
div_ints = my_int_7 / my_int_8
print('Integer Division:', div_ints) # Integer Division: 27.5

### Floats
my_float_1 = -12.0
my_float_2 = 4.9

print(type(my_float_1)) # <class 'float'>
print(type(my_float_2)) # <class 'float'>

my_float_1 = 5.4
my_float_2 = 12.0

float_division = my_float_2 / my_float_1
print('Float Division:', float_division) # Float Division: 2.222222222222222

### If I add float to an integer, the result will be a float
my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float

print(sum_int_and_float) # 61.4
print(type(sum_int_and_float)) # <class 'float'>


### Modulo operator - zbytek
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1

print('Integer Modulo:', mod_ints) # Integer Modulo: 8
print('Float Modulo:', mod_floats) # Float Modulo: 1.1999999999999993

