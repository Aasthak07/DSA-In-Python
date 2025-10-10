
#   @@@@@
#    @@@
#     @
# *****
# *   *
# *   *
# *   *
# *   *
n = int(input("enter only odd number"))

# Check condition
if n < 1 or n % 2 == 0:
    exit()

# First pattern (upper pyramid of '@')
for i in range(n // 2 + 1):
    # Left spaces
    for j in range(n // 2):
        print(" ", end="")
    # Extra inner spaces
    for j in range(i):
        print(" ", end="")
    # '@' symbols
    for j in range(n - 2 * i):
        print("@", end="")
    print()

# Second pattern (U-shaped box of '*', open bottom)
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()