# @
# @
# @****
# @   ****
# @      ****   @
#           ****@
#               @
#               @


n = 4
x = 0

for i in range(2 * n):
    flag = False

    # Left border '@'
    print('@' if i < n + 1 else ' ', end='')

    # Inner pattern
    for j in range(n * (n - 1) + 1):
        if n // 2 <= i < 2 * n - n // 2:
            if (n - 1) * x <= j <= (n - 1) * x + n - 1:
                print('*', end='')
                flag = True
            else:
                print(' ', end='')
        else:
            print(' ', end='')

    # Increase x only when * printed
    if flag:
        x += 1

    # Right border '@'
    print('@' if i > n - 1 else ' ', end='')

    print()