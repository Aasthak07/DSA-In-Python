#               *
#             * * *
#           * * * * *
#           *       *
#           *       *
#           *       *
# * * * * *           * * * * *
#   * * *               * * *
#     *                   *


# n=int(input("Enter the value of n: "))
n=7
for i in range((n//2)+1):
    for j in range(n+(n//2)-i):
        print(" ",end=" ")
    for i in range(2*i+1):
        print("*",end=" ")
    print()
for i in range((n//2)+1):
    for j in range(n):
        print(" ",end=" ")
    for j in range(n):
        if(j==0 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range((n//2)+1):
    for j in range(3*n):
        if(j>=i and j<=n-1-i) or (j>=2*n+i and j<=3*n-1-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()