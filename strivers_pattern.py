N = int(input("Enter N: "))

# ---------- Upper half ----------
iniS = 0  # initial spaces

for i in range(N):
    # Left stars
    for j in range(N - i):
        print("*", end="")

    # Spaces in the middle
    for j in range(iniS):
        print(" ", end="")

    # Right stars
    for j in range(N - i):
        print("*", end="")

    iniS += 2  # increase spaces by 2 each row
    print()  # move to next line


# ---------- Lower half ----------
iniS = 2 * N - 2  # initial spaces for lower half

for i in range(1, N + 1):
    # Left stars
    for j in range(i):
        print("*", end="")

    # Spaces in the middle
    for j in range(iniS):
        print(" ", end="")

    # Right stars
    for j in range(i):
        print("*", end="")

    iniS -= 2  # decrease spaces by 2 each row
    print()  # move to next line
