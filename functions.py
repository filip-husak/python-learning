name = input("What´s your name? ")
print("Hello, " + name + "!")

### Converting any value to integer
print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0

def hello():
    print("Hello, World!")

hello() # Calling the function

def calculate_area(length, width):
    area = length * width
    print("The area is:", area)

calculate_area(5, 3) # Calling the function with arguments

def calculate_sum(a, b):
    return a + b # Return will exit the function and return the value

my_sum = calculate_sum(3, 1)
print(my_sum) # 4