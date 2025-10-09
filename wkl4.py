# n= int(input("enter only odd number"))
n=5
# first part pyramid

for i in range(n//2 +1):

    # for spaces

    for j in range(n*2+1-i):
        print(' ', end=' ')
    #   for characters


    for j in range(2*i+1):
        print('e', end=' ') 
    print() 

# 2nd part vertical star

for i in range(n-1):
    for j in range(n*2+1):
        print(' ', end=' ')
    for j in range(1):
        print('*', end=' ')
    print()

# 3rd part
for i in range(n//2):
    for j in range(n+2):
        print(' ', end=' ')
    for j in range(n):
        if i==0 or j==0:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()  


#  fourth part # 
# 
for i in range(n):
    for j in range(n-2):
        if j >=n//2-i and j>= i- n//2:
            print('e', end=' ')
        else:
            print(' ', end=' ')

    for j in range(n-1):
        if i==n-3:
            print('*', end=' ')
        else:
            print(' ', end=' ')

    for j in range(n-4):
        if i<3:
            print('*', end=' ')                
    print()

    


     
    





    