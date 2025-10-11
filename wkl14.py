# *****     ***
# *****eeeee***
# *****  e  ***
#        e
#        e
#       eee



n=3
for i in range(n+3):
    for j in range(n+2):
        if i <n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(n+2):
        if i == n//2:
            print("e",end=" ")
    for j in range(n-1):
        print(" ",end=" ")        
    for j in range(1):
        if i>=n//2+1:
            print("*",end=" ")
    for j in range(n-1):
        print(" ",end=" ")
    
            
    for j in range(3*n+1, 4*n+1):
        if i<n :
            print("*",end=" ")      
                
    print() 
# # Pattern for odd n >= 3
# *****     ***
# *****eeeee***
# *****  e  ***
#        e
#        e
#       eee

