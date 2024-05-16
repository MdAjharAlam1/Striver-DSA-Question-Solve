#leetcode
#https://leetcode.com/problems/rotate-array/description/

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def reverse(arr,first,second):
    while(first<second):
        temp = arr[first]
        arr[first] = arr[second]
        arr[second] = temp 
        first+=1
        second-=1
        
    return arr

def reverseArrayRight(arr,n,k):
    reverse(arr,n-k,n-1)
    reverse(arr,0,n-k-1)
    reverse(arr,0,n-1)
    return arr


arr =[1,2,3,4,5,6,7]
n = len(arr)
k = 2 
result = reverseArrayRight(arr,n,k)
print(result)