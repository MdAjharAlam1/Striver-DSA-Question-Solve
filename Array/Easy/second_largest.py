
# print second largest element in the array  and largest element in ther array  

# Better approach Solution 


# Time Complexity => O(2N) =>  O(N)

# find largest element function    
def largestElement(arr):
    largest = arr[0]
    for  i in range(len(arr)):
        if(arr[i]>largest):
            largest = arr[i]
    return largest

# find second largest element in the array
def secondlargest(arr,largest):
    second_largest = -1
    for i in range(len(arr)):
        if(arr[i]>second_largest and arr[i]!=largest):
            second_largest = arr[i]
    return second_largest



# this code is optimal approah solution because it takes just only on passes 

# Time Complexity  => O(n)

def slargest(arr):
    n =len(arr)
    largest = arr[0]
    s_largest = -1
    for i in range(n):
        if arr[i] > largest:
            s_largest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > s_largest:
            slargest = arr[i]
    return s_largest



arr = [15,20,60,18,123,13]

# optimal approach solution 
secondlargest1 = slargest(arr)
print(secondlargest1)

# better approach solution 
largest = largestElement(arr)
print("largest element in the array : ", largest)
second_max = secondlargest(arr,largest)
print("Second Largest element in array :" ,second_max)