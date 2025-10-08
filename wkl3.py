# #webkul pattern program round 1 
# #pattern runs for odd number like min 3 , 5, 7 etc
# #here is ther pattern

# #for n==3
# *       *
# **     **
# ***@@@***
#    @@@
#    @@@
#    ***
#     *
# #for n==5
#  
# *             *
# **           **
# ***         ***
# ****       ****
# *****@@@@@*****
#      @@@@@
#      @@@@@
#      @@@@@
#      @@@@@
#      *****
#       ***
#        *
# #and so on for n==7.....
# #here is the program


# n=5
# for i in range(n+1):
#     for j in range(i):
#         print('*',end='')
#     for j in range(n-i):
#         print(' ',end='')
#     for j in range(n):
#         if(i==n):
#             print('@',end='')
#         else:
#             print(' ',end='')
#     for j in range(n-i):
#         print(' ',end='')
#     for j in range(i):
#         print('*',end='')
#     print()
# for i in range(n-1):
#     for j in range(3*n):
#         if(j<n or j>2*n-1):
#             print(' ',end='')
#         else:
#             print('@',end='')
#     print()
# for i in range(n//2+1):
#     for j in range(n):
#         print(' ',end='')
#     for j in range(i):
#         print(' ',end='')
#     for j in range(n-2*i):
#         print('*',end='')
#     for j in range(i):
#         print(' ',end='')
#     for j in range(n):
#         print(' ',end='')
#     print()

n = int(input("Enter an odd number greater than 1 for the pattern: "))  # user input (odd number)

# ✅ PART 1: Upper section (hourglass-like structure)
for i in range(n + 1):      # i = 0 to 5 (total 6 lines)
    
    # 🔹 Left stars — increase each line
    for j in range(i):
        print('*', end='')  # har line ke start me i stars
    
    # 🔹 Spaces after left stars — decrease each line
    for j in range(n - i):
        print(' ', end='')  # left side gap
    
    # 🔹 Middle section: spaces or '@' (depends on last line)
    for j in range(n):      
        if i == n:          # agar last line hai (i == 5)
            print('@', end='')  # poore middle me '@' print karo
        else:
            print(' ', end='')  # baaki lines me sirf space print karo
    
    # 🔹 Right-side gap (mirror of left gap)
    for j in range(n - i):
        print(' ', end='')  
    
    # 🔹 Right stars — mirror of left stars
    for j in range(i):
        print('*', end='')

    print()  # ek line complete hone ke baad new line

# ✅ PART 2: Middle section (solid '@' block)

for i in range(n - 1):          # i = 0..3 (4 lines total)
    for j in range(3 * n):      # total width = 15 (for n=5)
        
        # middle region only '@', rest space
        if j < n or j > 2 * n - 1:
            print(' ', end='')  # left/right blank space region
        else:
            print('@', end='')  # middle pillar region

    print()                     # next line

# ✅ PART 3: Bottom section (inverted triangles on sides)

for i in range(n // 2 + 1):     # i = 0..2 (3 lines)
    
    # left margin (indent)
    for j in range(n):
        print(' ', end='')

    # spaces before left inverted triangle
    for j in range(i):
        print(' ', end='')

    # left inverted triangle stars
    for j in range(n - 2 * i):
        print('*', end='')

    # spaces between two triangles
    for j in range(i):
        print(' ', end='')

    # gap between left and right shapes
    for j in range(n):
        print(' ', end='')

    print()  # line complete




