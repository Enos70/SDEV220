# M03 Tutorial - Functional Ptogramming

# Firisiya Chiomadzi
# 04/05/2024
# BinarySearch.py

# Given a sorted array of size N and an integer K, find the position(0-based indexing) 
# at which K is present in the array using binary search.
# Complete the function binarysearch() which takes arr[], N and K as input parameters and
# returns the index of K in the array. If K is not present in the array, return -1.

# Example 1:

# Input:
# N = 5
# arr[] = {1 2 3 4 5} 
# K = 4
# Output: 3
# Explanation: 4 appears at index 3.

# Example 2:

# Input:
# N = 5
# arr[] = {11 22 33 44 55} 
# K = 445
#Output: -1
#Explanation: 445 is not present. 

class Solution:
    def binary_search(self, arr, n, k):
        left = 0
        right = n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Check if k is present at mid
            if arr[mid] == k:
                return mid
            
            # If k is greater, ignore left half
            elif arr[mid] < k:
                left = mid + 1
            
            # If k is smaller, ignore right half
            else:
                right = mid - 1
        
        # If we reach here, then the element was not present
        return -1

# Driver code
if __name__ == "__main__":
   
    sol = Solution()
    N = 5
    arr = [1, 2, 3, 4, 5]
    K = 4
    print(sol.binary_search(arr, N, K))  # Output: 3
    
    N = 5
    arr = [11, 22, 33, 44, 55]
    K = 445
    print(sol.binary_search(arr, N, K))  # Output: -1