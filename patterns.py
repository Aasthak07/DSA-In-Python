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

# # def print_pattern(n: int):
# #     """
# #     Print the requested pattern for odd n (>1).
# #     If n is even or <=1, prints an error message.
# #     """

# #     if n <= 1 or n % 2 == 0:
# #         print("Invalid input: enter an odd number greater than 1.")
# #         return

# #     # inner area where top pyramid base fits
# #     inner_width = n

# #     # left and right star-block widths for the bottom center row
# #     left_block = n
# #     right_block = n

# #     # full line width (so we can compute spacing easily)
# #     total_width = left_block + 1 + inner_width + 1 + right_block
# #     # Explanation: layout is
# #     # [ left_block stars ] [ '@' ] [ inner_width area ] [ '@' ] [ right_block stars ]
# #     # columns (0 .. total_width-1)

# #     # 1) Top pyramid: 1,3,5,...,n  (rows = (n+1)//2)
# #     top_rows = (n + 1) // 2
# #     for i in range(top_rows):
# #         star_count = 2 * i + 1
# #         # center the star-block inside the inner area:
# #         left_pad = left_block + 1 + (inner_width - star_count) // 2
# #         print(' ' * left_pad + '*' * star_count)

# #     # 2) Middle: n-2 rows with two @ columns separated by inner_width spaces
# #     for _ in range(n - 2):
# #         print(' ' * left_block + '@' + ' ' * inner_width + '@')

# #     # 3) Middle central row: left_block stars, @, inner gap, @, right_block stars
# #     print('*' * left_block + '@' + ' ' * inner_width + '@' + '*' * right_block)

# #     # 4) Lower mirrored shrinking star-blocks:
# #     #    n-2, n-4, ..., 1  (each side)
# #     for k in range(n - 2, 0, -2):
# #         # place left k-stars at column 0 and right k-stars at the far right
# #         print('*' * k + ' ' * (total_width - 2 * k) + '*' * k)


# # if __name__ == "__main__":
# #     # Example usage:
# #     for val in (3, 5, 7):
# #         print(f"\nPattern for n = {val}:\n")
# #         print_pattern(val)


# # def print_pattern(n):
# #     # Validate input
# #     if n <= 1 or n % 2 == 0:
# #         print("Please enter an odd number greater than 1.")
# #         return

# #     mid = n // 2 + 1  # middle line
# #     width = n * 4     # overall canvas width
# #     center = width // 2  # column index for center star (@ will align here)

# #     # 🔹 Step 1: Top pyramid
# #     for i in range(1, mid + 1):
# #         stars = '*' * (2 * i - 1)
# #         # Center pyramid horizontally around the center
# #         left_padding = center - i + 1
# #         print(' ' * left_padding + stars)

# #     # 🔹 Step 2: Middle vertical @ columns
# #     # left @ starts exactly below pyramid center star
# #     left_at = center - (n // 2) - 1
# #     right_at = center + (n // 2) + 1

# #     for _ in range(n - 2):
# #         line = ''
# #         for col in range(width):
# #             if col == left_at or col == right_at:
# #                 line += '@'
# #             else:
# #                 line += ' '
# #         print(line)

# #     # 🔹 Step 3: Central connecting line
# #     left_stars = '*' * n
# #     right_stars = '*' * n
# #     gap = right_at - left_at - 1 - (2 * n)
# #     line = left_stars + '@' + (' ' * gap) + '@' + right_stars
# #     left_padding = left_at - n
# #     print(' ' * left_padding + line)

# #     # 🔹 Step 4: Lower mirrored section
# #     for k in range(n - 2, 0, -2):
# #         left = '*' * k
# #         right = '*' * k
# #         gap = (right_at - left_at + 1) - 2 * k
# #         print(' ' * (left_at - k + 1) + left + ' ' * gap + right)


# # # 🔸 Example test
# # for val in (3, 5, 7):
# #     print(f"\nPattern for n = {val}:\n")
# #     print_pattern(val)

# n=5

# for i in range(n//2 +1):
#     for j in range(n):
#         print(" ", end= "")
#     for j in range(n//2-i):
#         print(" ", end="")
#     for j in range(2*i+1):
#         print(" ", end="")
#     print()

# for i in range(n-2):
#     for j in range(n):
#         print(" ", end="")
#     for j in range(n):
#         if j<n:
#             if j==0 or j==n-1:
#                 print("@", end="")
#             else:
#                 print(" ", end="")
#     print()


# for i in range(n//2+1):
#     for j in range(n//2):
#         if j<1:
#             print(" ", end="")
#     for j in range(n-(2*1)):
#         print("*", end="")
#     for j in range(n//2):
#         if j<1:
#             print(" ", end="") 

# for j in range(n):
#     if i==0 or (j==0 or j==n-1):
#         print("@", end="")
#     else:
#         print(" ", end="")

# for j in range(n//2):
#     if j<1:
#         print(" ", end="")
# for j in range(n-(2*1)):

#     print(" ", end="")

# print()                


                                   


                 