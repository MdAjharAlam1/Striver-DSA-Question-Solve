
# Given an integer array nums, rotate the array to the left by k steps, where k is non-negative.

def reverse(arr,first,second):
    while(first<second):
        temp = arr[first]
        arr[first] = arr[second]
        arr[second] = temp
        first+=1
        second-=1
    return arr

def rotateArrayLeft(arr,n,k):
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)
    return arr

arr = [1,2,3,4,5]
n =len(arr)
k =4
ans = rotateArrayLeft(arr,n,k)
print(ans)