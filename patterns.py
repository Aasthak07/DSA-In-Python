# # The pattern must be dynamic. It should work for any odd numbers.( Excluding1 and any negative numbers )
# # ● It should not run for even numbers.

# # ● It should not run for negative numbers.
# # ● It should not run for 1.
# # ● It should not run for 0.

# # lets say user input is 3 (n=3)

# """  *
#    * * *
#    @   @
# ***@   @***
#  *       *            """

# def print_pattern(n: int):
#     """
#     Print the requested pattern for odd n (>1).
#     If n is even or <=1, prints an error message.
#     """

#     if n <= 1 or n % 2 == 0:
#         print("Invalid input: enter an odd number greater than 1.")
#         return

#     # inner area where top pyramid base fits
#     inner_width = n

#     # left and right star-block widths for the bottom center row
#     left_block = n
#     right_block = n

#     # full line width (so we can compute spacing easily)
#     total_width = left_block + 1 + inner_width + 1 + right_block
#     # Explanation: layout is
#     # [ left_block stars ] [ '@' ] [ inner_width area ] [ '@' ] [ right_block stars ]
#     # columns (0 .. total_width-1)

#     # 1) Top pyramid: 1,3,5,...,n  (rows = (n+1)//2)
#     top_rows = (n + 1) // 2
#     for i in range(top_rows):
#         star_count = 2 * i + 1
#         # center the star-block inside the inner area:
#         left_pad = left_block + 1 + (inner_width - star_count) // 2
#         print(' ' * left_pad + '*' * star_count)

#     # 2) Middle: n-2 rows with two @ columns separated by inner_width spaces
#     for _ in range(n - 2):
#         print(' ' * left_block + '@' + ' ' * inner_width + '@')

#     # 3) Middle central row: left_block stars, @, inner gap, @, right_block stars
#     print('*' * left_block + '@' + ' ' * inner_width + '@' + '*' * right_block)

#     # 4) Lower mirrored shrinking star-blocks:
#     #    n-2, n-4, ..., 1  (each side)
#     for k in range(n - 2, 0, -2):
#         # place left k-stars at column 0 and right k-stars at the far right
#         print('*' * k + ' ' * (total_width - 2 * k) + '*' * k)


# if __name__ == "__main__":
#     # Example usage:
#     for val in (3, 5, 7):
#         print(f"\nPattern for n = {val}:\n")
#         print_pattern(val)

n= int(input("enter only odd number"))
for i in range(n//2+1):
    for j in range(n):
        print(' ',end='')
    for j in range(n//2-i):
        print(' ',end='')
    for j in range(1+2*i):
        print('*',end='')
    print()
for i in range(n-1):
    for j in range(3*n):
        if(j==n or j==2*n-1):
            print('@',end='')
        elif(i==n-2 and(j<n or j>2*n-1)):
            print('*',end='')
        else:
            print(' ',end='')
    print()
for i in range(n//2):
    for j in range(i+1):
        print(' ',end='')
    for j in range(n-2-2*i):
        print('*',end='')
    for j in range(i+1):
        print(' ',end='')
    for j in range(n):
        print(' ',end='')
    for j in range(i+1):
        print(' ',end='')
    for j in range(n-2-2*i):
        print('*',end='')
    print()







                                   


                 