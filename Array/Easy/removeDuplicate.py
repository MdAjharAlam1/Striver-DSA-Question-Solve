
# leetcode Question 
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

#geeksforgeeks Link
#https://www.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article


# remove duplicate from sorted array 

# brute force approach solution using set
# Time complexity  => O(NlogN)
# space complexity  => O(N)  because using set storing array element in set 


# optimal approch using two pointer approach 
# Time complexity => O(N)
# space complexity => O(1)

def removeDuplicate(arr,n):
    i = 0
    for j in range(1,n,1):
        if arr[i] != arr[j]:
            arr[i+1] = arr[j]
            i+=1
    return i+1

arr = [1,1,2,2,3,3,3,4,4,4,5,5,5]
n = len(arr)
ans = removeDuplicate(arr,n)
print(ans)