# # make a square star pattern

n=int(input("enter the number "))

for i in range(1, n+1):
    for j in range(1, n+1):
        print("*", end="")
    print()


# # right triangle star pattern
# # 
n1= int(input("enter the number"))

for i in range(0,n1):
    for j in range(0, i+1):
        print("*", end="")
    print() 

# # inverted right triangle star pattern

n3= int(input("enter the number"))
for i in range(n3, 0, -1):
    for j in range(0, i):
        print("*", end="")
    print()


# # number pattern
n4= int(input("enter the number"))
for i in range(1,n4+1):
    for j in range(1, i+1):
        print(j, end="")
        # print(i, end="")
    print()       


# # equilateral triangle star pattern
# # 
n5 = int(input ("enter n5"))
for i in range(1, n5+1):
    for j in range(0, n5-i+1):
        print(" ", end="")
    for j in range(0, 2*i -1):
        print("*", end="")
    for j in range(0, n5-i+1):
        print(" ", end="")
    print()

# # inverted equilateral triangle star pattern
n6 = int(input ("enter n6"))
for i in range(n6, 0, -1):
    for j in range(0, n6-i+1):
        print(" ", end="")
    for j in range(0, 2*i -1):
        print("*", end="")
    for j in range(0, n6-i+1):
        print(" ", end="")
    print()    

# # diamond star pattern
n7 = int(input ("enter n7"))
for i in range(1, n7+1):    
    for j in range(0, n7-i+1):
        print(" ", end="")
    for j in range(0, 2*i -1):
        print("*", end="")
    for j in range(0, n7-i+1):
        print(" ", end="")
    print()

#  # combine both equilateral and inverted equilateral triangle star pattern
n8 = int(input("Enter n8: "))

# 🔺 Upper (equilateral) triangle
for i in range(1, n8 + 1):    
    for j in range(0, n8 - i):
        print(" ", end="")
    for j in range(0, 2 * i - 1):
        print("*", end="")
    print()

# # 🔻 Lower (inverted) triangle
for i in range(n8, 0, -1):    
    for j in range(0, n8 - i):
        print(" ", end="")
    for j in range(0, 2 * i - 1):
        print("*", end="")
    print()


    #n8 = int(input("Enter n8: "))

# 🔺 Upper (equilateral) triangle
for i in range(1, n8 + 1):    
    # spaces before stars
    for j in range(0, n8 - i):
        print(" ", end="")
    # stars
    for j in range(0, 2 * i - 1):
        print("*", end="")
    print()  # move to next line

# 🔻 Lower (inverted) triangle
for i in range(n8-1 , 0, -1):    
    # spaces before stars
    for j in range(0, n8 - i):
        print(" ", end="")
    # stars
    for j in range(0, 2 * i - 1):
        print("*", end="")
    print()  # move to next line




# #combined right triangle and inverted right triangle star pattern
num1=int(input("enter the number 1: "))

for i in range(1, num1+1):
    for j in range(1, i+1):
        print("*", end="")
    print()
for i in range(num1-1,0,-1):
    for j in range(1,i+1):
        print("*", end="")
    print()    

   
# print 1,0 pattern in right triangle form

num2 = int (input("enter the number for 1,0 pattern: "))
for i in range(1,num2+1):
    for j in range(1,i+1 ):
        if(i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
             
            print(1, end="")
        else:
            print(0, end="")
    print()

#     # ascending numbers to the left and descending numbers to the right in a triangle form
num3 = int(input("Enter an odd number greater than 1 for the pattern: "))
def print_number_pattern(num3):
    
    for i in range(1, num3 + 1):
        # Left side: ascending numbers
        for j in range(1, i + 1):
            print(j, end="")
        # Spaces in the middle
        spaces = 2 * (num3 - i)
        print(" " * spaces, end="")
        # Right side: descending numbers
        for j in range(i, 0, -1):
            print(j, end="")
        print()

# Example usage (for n=4, matching the image pattern)
print_number_pattern(4)
n= int(input("enter the number of rows: "))
start= 1
for i in range(1, n+1):
    if i%2==0:
        start=0
    else:
        start=1
    for j in range(1, i+1):
        print(start, end="")
        start=1-start

    print()    

# #numbers in a triangle form
top=1
num4= int(input("enter the number of rows: "))
for i in range(1,num4+1):
    for j in range(1,i+1):
        print(top, end=" ")
        top+=1
    print()

# alphabet pattern in a triangle form  
# 
num5= int(input("enter the number of rows: "))
for i in range(0,num5):
    for j in range(0, i+1):
        print(chr(ord('A')+j), end="")
    print()  



# # inverted alphabet pattern in a triangle form
# # 
num6= int(input("enter the number of rows: "))
for i in range(num6,0,-1):
    for j in range(0, i):
        print(chr(ord('A')+j), end="")

    print()

   