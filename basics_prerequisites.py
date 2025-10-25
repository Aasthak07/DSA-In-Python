print("hello world")
print(type("hello world")) # <class 'str'>
print(type(5)) # <class 'int'>

# varibles naming rules
# 1. can only contain letters, numbers, and underscores
# 2. cannot start with a number
# 3. should be descriptive
# & cant use
# 4. cannot be a reserved keyword (like print, if, else, etc.)

#comments
# single line comment
# THIS IS FROM COLLEGE WALAAH

# multi line comments

"""THIS 
IS 
fromCOLLEGE
WALAAH"""


# operators
# arithmetic operators: +, -, *, /, %, **, //
print(5 + 3) # 8
print(5 - 3) # 2    
print(5 * 3) # 15
print(5 / 3) # 1.6666666666666667
print(5 % 3) # 2
print(5 ** 3) # 125
print(5 // 3) # 1

# assignment operators: =, +=, -=, *=, /=, %=, **=, //=
x = 5
x += 3 # x = x + 3
x -= 3 # x = x - 3
x *= 3 # x = x * 3
x /= 3 # x = x / 3
x %= 3 # x = x % 3
x **= 3 # x = x ** 3
x //= 3 # x = x // 3

# Identity operators: is, is not
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) # False
print(a is not b) # True

# Membership operators: in, not in
a = [1, 2, 3]
print(1 in a) # True
print(4 in a) # False
print(4 not in a) # True
print(1 not in a) # False   

# comparison operators: ==, !=, >, <, >=, <=
print(5 == 3) # False
print(5 != 3) # True
print(5 > 3) # True
print(5 < 3) # False
print(5 >= 3) # True
print(5 <= 3) # False


# logical operators: and, or, not
print(5 > 3 and 5 < 10) # True  
print(5 > 3 or 5 < 10) # True
print(not 5 > 3) # False        
print(not 5 < 3) # True

# bitwise operators: &, |, ^, ~, <<, >>
print(5 & 3) # 1
print(5 | 3) # 7        
print(5 ^ 3) # 6        
print(~5) # -6        
print(5 << 2) # 20 # 5 * 2^2
print(5 >> 2) # 1 # 5 / 2^2
print(5 >> 1) # 2 # 5 / 2^1
print(5 << 1) # 10 # 5 * 2^1

# operator precedence
# 1. parentheses ()
# 2. exponentiation **
# 3. multiplication *, division /, floor division //, modulus %
# 4. addition +, subtraction - -
# 5. bitwise shifts <<, >>
# 6. and &
# 7. exclusive or ^
# 8. inclusive or | 


# DATA TYPES
# 1. int
x = 5   # integer
print(type(x)) # <class 'int'>  
# 2. float  
x = 5.0 # float
print(type(x)) # <class 'float'>  
# 3. complex  
x = 5 + 3j # complex
print(type(x)) # <class 'complex'>  
# 4. string  
x = "hello" # string
print(type(x)) # <class 'str'>  
# 5. list  
x = [1, 2, 3] # list
print(type(x)) # <class 'list'>  
# 6. tuple  
x = (1, 2, 3) # tuple
print(type(x)) # <class 'tuple'>  
# 7. set  
x = {1, 2, 3} # set
print(type(x)) # <class 'set'>  
# 8. dictionary  
x = {"name": "John", "age": 36} # dictionary
print(type(x)) # <class 'dict'>  
# 9. boolean  
x = True # boolean
print(type(x)) # <class 'bool'>  
# 10. NoneType  
x = None # NoneType
print(type(x)) # <class 'NoneType'> 
# 11. bytes  
x = b"hello" # bytes
print(type(x)) # <class 'bytes'>  
# 12. bytearray , BYTEARRAY IS MUTABLE VERSION OF BYTES 
 
x = bytearray(5) # bytearray
print(type(x)) # <class 'bytearray'>  
# 13. memoryview
x = memoryview(b"hello") # memoryview
print(type(x)) # <class 'memoryview'>  
# 14. frozenset , FROZENSET IS IMMUTABLE VERSION OF SET

x = frozenset({1, 2, 3}) # frozenset
print(type(x)) # <class 'frozenset'>


# type conversion
x = 5 # int 
y = 3.0 # float
z = "10" # str
print(type(x)) # <class 'int'>
print(type(y)) # <class 'float'>
print(type(z)) # <class 'str'>
print(x + y) # 8.0  # int + float = float
print(x + int(z)) # 15  # int + int = int
print(str(x) + z) # "55"  # int + str = str
print(float(x) + y) # 8.0  # int + float = float    

#TYPE CASTING   
x = 5 # int
y = 3.0 # float
z = "10" # str
print(type(x)) # <class 'int'>
print(type(y)) # <class 'float'>
print(type(z)) # <class 'str'>
print(x + y) # 8.0  # int + float = float
print(x + int(z)) # 15  # int + int = int
print(str(x) + z) # "55"  # int + str = str
print(float(x) + y) # 8.0  # int + float = float

# input and output function

full_name = "Abhinav Awasthi"
age = 100
address = "Lucknow"

print(full_name)
print(age)
print(address)

print(full_name, age, address, sep=', ')
print(full_name, age, address, end=" ")
print()
print(full_name, age, address)

#control statements
# 1. if
# 2. elif
# 3. else
# 4. for
# 5. while

# if
x = 5
if x > 0:
    print("x is positive")
else:
    print("x is negative")

# elif
x = 5
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# else
x = 5
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")


# ternary operator
x = 5
print("x is positive") if x > 0 else print("x is negative")
print()

# while
x = 5
while x > 0:
    print(x)
    x -= 1
print()
# for
for i in range(5):
    print(i)
print()

list= [1,2,3,4,5]
for i in list:
    print(i, end= " ")
print()

for i in range(1, 11, 2):
    print(i, end= " ")
print()

for i in range(20, 0 , -1):
    print(i, end= " ")
print()

# Functions
# def function_name (parameters):
# code-------

def sun(a, b):
    c = a + b
    print(c)

sun(1, 2)



# Practice question

n= 5146

while n>0:
    r= n%10   # remainded matlab last digit milti hai
    print(r, end= " ")
    n= n//10  # last digit ko remove karo



