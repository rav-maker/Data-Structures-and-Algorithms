# Task: Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

# Example 1:

# Input:
# N = 5, S = 12
# A[] = {1,2,3,7,5}
# Output: (2,4)
# Explanation: The sum of elements from 2nd position to 4th position is 12.

def subArraySum(S,arr,n):
    for i in range(n):
        sum = arr[i]
        j = i+1
        while j<n:            
            if sum == S:
                return (i+1,j)
            if sum>S:
                break

            sum += arr[j]

            j+=1


if __name__ == "__main__":
    # test case 1
    arr = [2,3,7,8,5]
    S = 15
    print(subArraySum(S,arr,len(arr)))    ## Output = (3,4)

    # test case 2
    arr1 = [1,2,3,4,5,6,7,8,9,10]
    S1 = 15
    print(subArraySum(S1,arr1,len(arr1)))   ## Output = (1,5)

    # test case 3
    arr2  = [1,2,3,7,5]
    S2 = 12
    print(subArraySum(S2,arr2,len(arr2)))   ## Output = (2,4)
