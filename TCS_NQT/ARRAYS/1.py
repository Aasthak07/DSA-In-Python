# find the smallest element in array
# 

def getMin(arr):
    minElement = float('inf')
    for i in range(len(arr)):
        minElement= min(minElement, arr[i])
    return minElement 

arr= [1,2,3,4,5,1, 0] 
res= getMin(arr)  
print(res)