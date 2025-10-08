

n = int(input("enter only odd number"))  # user input (odd number) - yahaan hum n=5 le rahe hain

# 🔹 PART 1: UPPER TRIANGLE (increasing stars)
for i in range(n - 2):           # range(3) → i = 0, 1, 2  (total 3 lines)
    for j in range(i + 1):       # har line me (i+1) stars print hote hain
        print("*", end='')       # ek star print karo bina next line liye
    print()                      # har line ke baad new line

# Output so far:
# *
# **
# ***

# 🔹 PART 2: MIDDLE LINE (star-space pattern)
print("*" * (n - 1), end='')     # (n-1)=4 stars print — left side stars
print(" " * (n + 1), end='')     # (n+1)=6 spaces print — middle gap
print("*")                       # ek star print — right side star + newline

# Output so far:
# *
# **
# ***
# ****      *

# 🔹 PART 3: FULL LINE (long horizontal line)
print("*" * (2 * n + 2))         # (2*5+2)=12 stars print — full width line

# Output so far:
# *
# **
# ***
# ****      *
# ************

# 🔹 PART 4: AGAIN STAR-SPACE-STAR LINE (mirror of part 2)
print("*" * (n - 1), end='')     # 4 stars left side
print(" " * (n + 1), end='')     # 6 spaces middle
print("*")                       # ek star right side

# Output so far:
# *
# **
# ***
# ****      *
# ************
# ****      *

# 🔹 PART 5: INVERTED TRIANGLE (decreasing stars)
for i in range(n):               # range(5) → i = 0 to 4 (total 5 lines)
    for j in range(n - i - 2):   # har line me (n - i - 2) stars hote hain
        print("*", end='')
    print()                      # har line ke baad new line

# Let's see how many stars each line has:
# i=0 → 5-0-2 = 3 → ***
# i=1 → 5-1-2 = 2 → **
# i=2 → 5-2-2 = 1 → *
# i=3 → 5-3-2 = 0 → (blank)
# i=4 → 5-4-2 = -1 → loop skip (no stars)

# So actually, ye loop 3 proper lines print karega (***, **, *)

# Final Output:
# *
# **
# ***
# ****      *
# ************
# ****      *
# ***
# **
# *
                     