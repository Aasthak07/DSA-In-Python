



# 🔸 Program: Print pattern of '*' and '@' based on user input (odd number)
# 🔸 Example output same as question PDF (for n = 3, 5, 7)

# Input lena user se
n = int(input("Enter only odd number: "))

# ✅ Part 1: TOP PYRAMID (upar ka triangle)
# Ye part ek pyramid banata hai jo center ke upar hota hai (like temple top)
for i in range(n // 2 + 1):      # loop 0 se n//2 tak chalega (odd number hone par half+1 lines banti hain)
    
    # pehle n spaces dete hain -> ye base left margin banata hai
    for j in range(n):
        print(' ', end='')

    # ab extra spaces dete hain taaki pyramid center align ho
    # jaise-jaise i badhta hai, spaces kam hoti jati hain
    for j in range(n // 2 - i):
        print(' ', end='')

    # ab har line mein odd number of stars print hote hain (1,3,5,...)
    # formula: 1 + 2*i (kyunki pyramid odd width ka hota hai)
    for j in range(1 + 2 * i):
        print('*', end='')

    # ek line complete hone ke baad new line lena zaruri hai
    print()

# ✅ Part 2: MIDDLE SECTION (do pillars '@' aur base line)
# Ye part vertical pillars banata hai aur ek horizontal base
for i in range(n - 1):           # n-1 lines total
    for j in range(3 * n):       # total width = 3 * n (left + middle + right region)
        
        # condition 1️⃣ : agar column number n ya 2*n - 1 ho to '@' print karo (yeh pillars hain)
        if j == n or j == 2 * n - 1:
            print('@', end='')

        # condition 2️⃣ : agar ye second-last line hai (i == n-2)
        # aur pillar ke bahar ka region hai (j < n ya j > 2*n-1)
        # to wahan '*' print karna hai (yeh base banata hai)
        elif i == n - 2 and (j < n or j > 2 * n - 1):
            print('*', end='')

        # otherwise blank space print karte raho
        else:
            print(' ', end='')

    # line complete hone par next line
    print()

# ✅ Part 3: BOTTOM INVERTED TRIANGLES (do niche ke mirrored triangles)
# ye dono sides pe inverted triangles print karta hai
for i in range(n // 2):           # half lines (upar wale half ke mirror)
    
    # (i+1) spaces before left triangle (jaise-jaise neeche jaate ho, space badhta hai)
    for j in range(i + 1):
        print(' ', end='')

    # left triangle ke stars: har line me 2 kam hote ja rahe hain
    # formula: n - 2 - 2*i
    for j in range(n - 2 - 2 * i):
        print('*', end='')

    # (i+1) spaces again (left triangle ke baad)
    for j in range(i + 1):
        print(' ', end='')

    # middle ka fixed gap (do triangles ke beech)
    for j in range(n):
        print(' ', end='')

    # right side mirror: (i+1) space + stars
    for j in range(i + 1):
        print(' ', end='')

    for j in range(n - 2 - 2 * i):
        print('*', end='')

    # line complete hone ke baad new line
    print()

# ✅ End of program
# Agar n = 5 ho, output kuch aisa hoga:

#        *
#       ***
#      *****
#      @   @
#      @   @
#      @   @
# *****@   @*****
#  ***       ***
#   *         *

# Yehi pattern n = 3, 5, 7 ke liye question paper me diya gaya hai.


# 9) Tips / common pitfalls

# Input must be odd — else center symmetry breaks (n//2 truncation changes lengths).

# Watch off-by-one: pillars are at n and 2*n - 1 (0-based) — remember 2*n would be one too far.

# Use string multiplications (' '*k, '*'*k) to keep code short and readable.




                                   
