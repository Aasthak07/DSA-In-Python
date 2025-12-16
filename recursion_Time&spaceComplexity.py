# Time complexity in computer science describes how the execution time of an ##algorithm grows as the input size increases. it essentially quantifies the #number of operation an algorithm performs as a function of the input data size.

#Asymptotic notation is a notation that provides a way to describe the growth rate of a function as the input size grows.
# Best Case (O(omega) , Average Case (O(theta)) , Worst Case (O(oh))

# types of time complexities 

# 1. O(1) - constant time complexity
# 2. O(log n) - logarithmic time complexity
# 3. O(n) - linear time complexity
# 4. O(n^2) - quadratic time complexity
# 5. O(2^n) - exponential time complexity

#linear time complexity O(n)
n=10
for i in range(n):
    print(i, end= " " )

# n ke saath koi constant no. se operation ho rha hoga to  order of n hi hoga

# constant time complexity O(1)
for i in range(10000):
    print(i, end= " " )

#QUADRATIC TIME COMPLEXITY O(n^2)

for i in range(n**2):
    print(i, end= " " )

#logarithmic time complexity O(log n)
n=100
while n>1:
    n= n//2
    print(n)    

