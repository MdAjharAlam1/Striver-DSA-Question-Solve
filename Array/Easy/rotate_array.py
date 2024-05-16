
# rotate an array from one place

'''
arr = [1,2,3,4,5]
ouput = [2,3,4,5]
'''

def rotateArrayOnePlace(arr):
    n =len(arr)
    temp = arr[0]
    for i in range(1,n,1):
        arr[i-1] = arr[i]
    arr[n-1] = temp
    return arr

arr = [1,2,3,4,5]
ans = rotateArrayOnePlace(arr)
print(ans)