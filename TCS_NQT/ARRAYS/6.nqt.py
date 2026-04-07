# Q1. The Chrono-Locked Conveyor Belt

# In an ancient mechanical city, a circular conveyor belt transports crystalline energy cores in a strictly non-decreasing sequence of stability levels. The belt was originally calibrated in sorted order to prevent resonance collapse.

# However, during a maintenance cycle, the system was restarted from an arbitrary position on the belt. As a result, the visible sequence now appears rotated, though it must still preserve the integrity of the original sorted structure.

# The engineers suspect that:
# - The belt was originally arranged in non-decreasing order.
# - It may have been rotated any number of positions (including zero).
# - Duplicate stability levels are allowed.
# - If the belt does not conform to such a rotated sorted configuration, the stabilization chamber will fail.

# Your task is to determine whether the currently observed sequence could represent a valid rotation of a non-decreasing sorted array.

# Return true if valid. Otherwise, return false.

# Test Cases:

# Input: [5,6,7,1,2,3,4]
# Output: true

# Input: [2,2,2,3,1,2]
# Output: true

# Input: [1,3,2,4]
# Output: false

# Input: [10,10,10]
# Output: true

# Input: [4,5,1,2,6]
# Output: false
# Function to find pivot (smallest element) using binary search
def find_pivot(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid

    return left


# Main code
arr = list(map(int, input().replace('[','').replace(']','').replace(',',' ').split()))
n = len(arr)

# Edge case: single element or empty
if n <= 1:
    print("true")
else:
    pivot = find_pivot(arr)
    valid = True

    # Check left part (0 → pivot-1)
    for i in range(0, pivot - 1):
        if arr[i] > arr[i + 1]:
            valid = False
            break

    # Check right part (pivot → n-1)
    for i in range(pivot, n - 1):
        if arr[i] > arr[i + 1]:
            valid = False
            break

    # Check circular condition
    if pivot > 0 and arr[n - 1] > arr[0]:
        valid = False

    # Output
    if valid:
        print("true")
    else:
        print("false")