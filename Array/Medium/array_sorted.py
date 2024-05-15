
# print check array is sorted or not 

def isSorted(arr):
    for i in range(1,len(arr)):
        if arr[i]< arr[i-1]:
            return False
    return True

arr = [1,2,8,4,6]
sort = isSorted(arr)
if sort==True:
    print("array is sorted")
else:
    print("array is not sorted ")