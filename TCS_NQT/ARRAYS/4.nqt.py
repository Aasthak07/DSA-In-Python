# Q4.

# In the Temple of Numbers, a sacred integer n is declared "Pure" only if it has exactly two divisors — 1 and itself.

# The priests must verify whether n is pure.

# Return:
# 1 if prime
# 0 otherwise

# Efficiency is critical — the temple forbids checking beyond √n.

# Case 1:
# Input:
# n = 5
# Output:
# 1

# Case 2:
# Input:
# n = 4
# Output:
# 0

# Instead of checking all numbers till n:
# We only check till: √n  💡 Why √n?

# Because factors come in pairs:
# Example:
# 36 → (1,36), (2,18), (3,12), (4,9), (6,6)
#  After √36 = 6, pairs repeat

# So no need to check beyond √n

# n= int(input().strip())
# if n<=1:
#     print(0)

# else:
#     is_prime= True

#     for i in range(2, int(n**0.5)+1):
#         if n%i ==0:
#             is_prime= False
#             break

#     if is_prime:
#         print(1)

#     else:
#         print(0)    

n = int(input().strip())

if n <= 1:
    print(0)
else:
    i = 2
    is_prime = True
    
    while i * i <= n:   # same as i <= √n
        if n % i == 0:
            is_prime = False
            break
        i += 1
    
    if is_prime:
        print(1)
    else:
        print(0)
