n=4

for i in range(n+1):
    for j in range(1):
        print("@", end="")
    

    for j in range(n):
        if i==n-2 or j==n :
            print("*", end="")
        # else:
        #     print(" ", end="")
        

    # for j in range(n-3):
    #     if i==n-1:
    #         print("*", end="")

    # for j in range(n-1):
    #     if i ==n-1:
    #         print("*", end="")

    # for j in range(n-3):
    #     if i==n :
    #         print("*", end="")

    print()          