#   *
#  ***
# *****
#   *
#   *
#   *
#   *
#   *

n=5
for i in range(n//2+1):
    for j in range(n//2-i):
        print(' ',end='')
    for j in range(2*i + 1):
        print('*',end='')
    print()

for i in range(n):
    for j in range(n//2):
        print(' ',end='')
    print('*',end='')
    print()    