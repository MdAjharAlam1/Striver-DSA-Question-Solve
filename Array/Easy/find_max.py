
# print max number from the array 

def findMax(arr):
    max_number = arr[0]
    for i in range(len(arr)):
        if(arr[i]>max_number):
            max_number = arr[i]
    print("maximum number :", max_number)

arr = [1,10,13,15,16,18]
findMax(arr)