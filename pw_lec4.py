## SETS and DICTIONARY

# A set is an unordered collection of unique elements.
# Sets are useful for membership testing, removing duplicates from a sequence, and performing mathematical set operations
# like union, intersection, difference, and symmetric difference.
# Sets are also useful for keeping track of unique elements in a collection.
# 

set1={1, 2, 'heello', 2, 'heello'}
print(set1)  # Output: {1, 2, 'heello'}
print(type(set1))  # Output: <class 'set'>
set2=set([1, 2, 3, 4, 5, 5, 4])
print(set2)  # Output: {1, 2, 3, 4, 5}
set3=set()  # empty set
print(set3)  # Output: set()
print(len(set2))  # Output: 5

list1=[1, 2, 3, 4, 5, 5, 4]
set4=set(list1)  # removing duplicates from list
print(set4)  # Output: {1, 2, 3, 4, 5}

#operations in sets
#len(), add(), remove(), discard(), pop(), clear(), union(), intersection(), difference(), symmetric_difference(), clear(), copy()

set2= {1, 2, 3, 4, 5, 'hello', 'world'}
set2.add('hello')  # adding element to set
print(set2)  # Output: {1, 2, 3, 4
set2.add('python')
print(set2)

set2.discard(3)  # removing element from set
print(set2)  # Output: {1, 2, 4, 5, 'hello', 'python'}
set2.discard(10)  # removing element not present in set
print(set2)  # Output: {1, 2, 4, 5, 'hello', 'python'} Note: discard() does not raise an error if the element is not present in the set.
set2.remove(4)  # removing element from set
print(set2)  # Output: {1, 2, 5, 'hello', 'python'}
#set2.remove(10)  # removing element not present in set raises KeyError
#print(set2)  # Output: {1, 2, 5, 'hello', 'python'}

if 'hello' in set2:
    print("hello is present in set2")
else:
    print("hello is not present in set2")

set3=set2.copy()  # copying set
print(set3)  # Output: {1, 2, 5, 'hello', 'python'}, 'python'}

set1.union(set2)  # union of two sets
print(set1 | set2)  # Output: {1, 2, 3, 4, 5, 'heello', 'hello', 'python'}
print(set1)  # Output: {1, 2, 'heello'}
set1.intersection(set2)  # intersection of two sets
print(set1 & set2)  # Output: set()
print(set1)  # Output: {1, 2, 'heello'}
set1.difference(set2)  # difference of two sets
print(set1 - set2)  # Output: {1, 2}
print(set1)  # Output: {1, 2, 'heello'}
set1.symmetric_difference(set2)  # symmetric difference of two sets
print(set1 ^ set2)  # Output: {3, 4, 5, 'heello', 'python'}
print(set1)  # Output: {1, 2, 'heello'}
set1.clear()  # clearing set

print(set1)  # Output: set()


#Python Dictionaries ( Map, HashMap )
# A dictionary is an unordered collection of key-value pairs.
# Dictionaries are useful for storing and retrieving data based on a unique key.
# Dictionaries are also useful for storing and retrieving data based on a unique key.

x={}
print(type(x))  # Output: <class 'dict'>
x1={1,2,3}  # set
print(type(x1))  # Output: <class 'set'>

dict1={'name': 'John', 'age': 25, 'city': 'New York'}
print(dict1)  # Output: {'name': 'John', 'age': 25, 'city': 'New York'}
print(type(dict1))  # Output: <class 'dict'>
print(dict1['name'])  # Output: 'John'
print(dict1['age'])  # Output: 25
print(dict1['city'])  # Output: 'New York'

#dict2= {[1,2,3]: 'tuple key', 10: 'integer key', 5.5: 'float key'} # invalid dictionary key
#print(dict2)  # Output: TypeError: unhashable type: 'list'
dict2= {(1,2,3): 'tuple key', 10: 'integer key', 5.5: 'float key'}  # valid dictionary key
print(dict2)  # Output: {(1, 2, 3): 'tuple key', 10: 'integer key', 5.5: 'float key'}

dict3={1: 'one', 2: 'two', 3: 'three'}
print(len(dict3))  # Output: 3  
dict3[4] = 'four'  # adding key-value pair to dictionary
print(dict3)  # Output: {1: 'one', 2: 'two', 3: 'three', 4: 'four'}  #ordered in python 3.7+
dict3[2] = 'TWO'  # updating value of existing key

dict4= {1: 'aastha', 2: 'taehyung', 3: 'jungkook', 4: 'jin'}
print(dict4)  # Output: {1: 'aastha', 2: 'taehyung', 3: 'jungkook', 4: 'jin'}
del dict4[3]  # deleting key-value pair from dictionary
print(dict4)  # Output: {1: 'aastha', 2: 'taehyung', 4: 'jin'}
dict4[4]='jimin'  # updating value of existing key
print(dict4)  # Output: {1: 'aastha', 2: 'taehyung', 4: 'jimin'}
dict3.pop(1)  # removing key-value pair from dictionary using pop()
print(dict3)  # Output: {2: 'TWO', 3: 'three', 4: 'four'}
print(dict3.get(2))  # Output: 'TWO'  # getting value of key using get()
print(dict3.get(10, 'Key not found'))  # Output: 'Key not found'  # getting value of non-existing key using get() with default value

var= {1: 'apple', 2: 'banana', 3: 'cherry'}
for key,value in var.items():  # iterating through dictionary using items()
    print(key,value) 

print(var.keys())
for key in var.keys():
    print(key)

print(var.values())
for value in var.values():
    print(value)

print(var.items())
for key,value in var.items():
    print(key,value)

var={'name': 'John', 'age': 25, 'city': 'New York'}
var.clear()  # clearing dictionary
print(var)

#hashing in python
# Hashing is the process of converting an object into a fixed-size integer value, called a hash value or hash code.
# Hashing is used in various applications, such as data storage, data retrieval, and data integrity verification.
# In Python, the built-in hash() function is used to compute the hash value of an object.
# Only immutable objects (like strings, numbers, and tuples) can be hashed.
# Mutable objects (like lists and dictionaries) cannot be hashed.
    