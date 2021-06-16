# Task: Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

# Example 1:

# Input:
# N = 4
# arr[] = {1, 5, 3, 2}
# Output: 2
# Explanation: There are 2 triplets: 
# 1 + 2 = 3 and 3 +2 = 5 

# using normal method
def CountTriplets(arr,n):
    count = 0
    # choose an element using for loop
    # check if sum is available
    for i in range(n):
        j = i+1      
        while j<n:
            if (arr[i] + arr[j]) in arr:
                count += 1
            j += 1

    return count

if __name__=="__main__":
    arr = [6,5,4,3,2,1]
    result = CountTriplets(arr,len(arr))
    print(result)        # Output  = ((1+2 = 3), (1+3 = 4), (1+4 = 5), (1+5 = 6), (2+3 = 5), (2+4 = 6))



# using dynamic programming

from collections import defaultdict

def CountTriplet(arr,n):
    count = 0
    d = defaultdict(lambda:0)

    for a in arr:
        d[a]+=1

    for i in range(n):
        j = i+1
        while j<n:
            if d[arr[i]+arr[j]]:
                count+=1
            j+=1

    return count

if __name__=="__main__":
    arr = [6,5,4,3,2,1]
    result = CountTriplet(arr,len(arr))
    print(result) 

