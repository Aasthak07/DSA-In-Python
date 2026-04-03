# Q5.

# In the Valley of Titans, warriors are ranked by strength values stored in an array arr[].

# The King requires immediate identification of:
# - the weakest warrior (minimum strength)
# - the strongest warrior (maximum strength)

# Return both values in the format:
# min max

# The scan must be done in a single traversal.

# Case 1:
# Input:
# arr = [3, 2, 1, 56, 10000, 167]
# Output:
# 1 10000

# Case 2:
# Input:
# arr = [1, 345, 234, 21, 56789]
# Output:
# 1 56789

# Case 3 (Single Element):
# Input:
# arr = [56789]
# Output:
# 56789 56789

arr = list(map(int, input().replace('[','').replace(']', ''). replace(',', '').split()))

min_val= arr[0]
max_val = arr[0]

for x in arr:
    if x<min_val:
        min_val=x
    if x>max_val:
        max_val= x
print(min_val, max_val)            