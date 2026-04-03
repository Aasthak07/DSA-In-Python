# Q3.

# A digital vault in CyberRealm stores commands in an encoded binary string. The string consists of binary digits separated by operation codes:

# A -> AND
# B -> OR
# C -> XOR

# The vault processes the string strictly from left to right, performing one operation at a time, ignoring conventional precedence.

# If the string is NULL, return -1.

# Determine the final binary result.

# Case 1:
# Input:
# 1C0C1C1A0B1
# Output:
# 1

# Case 2:
# Input:
# 0A1B1C1
# Output:
# 0

# Case 3 (Single Digit):
# Input:
# 1
# Output:
# 1

# Case 4 (NULL Case):
# Input:
# NULL
# Output:
# -1

s= input().strip() #for removing the extra spaces

if s=="NULL":
    print(-1)
else:
    if len(s)==1:
        print(int(s))
    else:
        result= int(s[0]) 

        i=1
        while i <len(s):
            op=s[i]
            num= int(s[i+1])

            if op=='A': #and
                result= result& num
            elif op=='B': # OR
                result = result| num

            elif op=='C': #XOR
                result = result ^num

            i+=2

        print(result)           

