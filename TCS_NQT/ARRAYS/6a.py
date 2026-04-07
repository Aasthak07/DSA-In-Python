arr = list(map(int, input().replace('[','').replace(']','').replace(',',' ').split()))

count = 0
n = len(arr)

for i in range(n):
    if arr[i] > arr[(i + 1) % n]:
        count += 1

if count <= 1:
    print("true")
else:
    print("false")