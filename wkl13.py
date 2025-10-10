
# eeee     *
#    *     *     *
#    *     *     *
#    *eeeee*eeeee*
#    *     *     *
#    *     *     *
#          *     eeee
n=5
#1st part
for i in range(1):
    for j in range(n-1):
        print('e', end='')
    for j in range(n):
        print(' ', end='')
    for j in range(1):
        print('*', end='')
    print()    
#2nd part
for i in range(n):
    for j in range(n//2+1):
        print(' ', end='')
    for j in range(1):
        print('*', end='')
    for j in range(n):
        if i==n//2:
            print('e', end='') 
        else:
            print(' ', end='')
    for j in range(1):
        print('*', end='')
    for j in range(n):
        if i==n//2:
            print('e', end='') 
        else:
            print(' ', end='')
    for j in range(1):
        print('*', end='')
    print()
#3rd part
for i in range(1):
    for j in range(2*n-1):
        print(' ', end='')
    for j in range(1):
        print('*', end='')
    for j in range(n):
        print(' ', end='')
    for j in range(n-1):
        print('e', end='')        
    print()           
