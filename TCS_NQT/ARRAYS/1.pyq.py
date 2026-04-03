# 🧾 Question (From Image)

# In the intergalactic archive of Planet Xyphor, two ancient data crystals a[] and b[] store encrypted energy signatures. Due to cosmic duplication anomalies, many signatures may repeat within and across the crystals.

# The Galactic Council must compute the total number of distinct energy signatures present when both crystals are merged into a unified repository.

# If a signature appears multiple times, it must be counted only once.

# Your task is to determine the number of unique energy signatures after combining both arrays.

# 📥 Input

# Two arrays:

# a[] → first array of integers
# b[] → second array of integers
# 📤 Output
# Print a single integer representing the count of distinct elements
# 🧪 Case 1
# Input:
# a[] = [1, 2, 3, 4, 5]
# b[] = [1, 2, 3]
# Output:
# 5

a = list(map(int, input().split()))
b = list(map(int, input().split()))

unique_elements = set()
unique_elements.update(a)
unique_elements.update(b)

print(len(unique_elements))