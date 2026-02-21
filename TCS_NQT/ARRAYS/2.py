# Find the largest element in array

arr= list(map(int, input('enter the elemnet').split()))
def getMax(arr):
    maxElement= arr[0]
    for i in range(len(arr)):
        maxElement= max(maxElement, arr[i])
    return maxElement    

res = getMax(arr)
print(res)
    