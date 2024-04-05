# Firisiya Chiomadzi

# Arrays.py
# M03 Tutorial - Functional OOP Programming

# Python solution using the counting sort algorithm to sort the array containing only 0's, 1's, and 2's in ascending order:

# Example 1
# Input:
# N = 5
# arr[]= {0 2 1 2 0}

# Example 2
# Input:
# N = 3
# arr[]= {0 1 0}

class Solution:
    
    # Function to sort an array of 0s, 1s, and 2s.
    def sort012(self, arr, n):
        low = 0
        high = n - 1
        mid = 0
        
        # Iterating until mid pointer is less than or equal to high.
        while mid <= high:
            
            # If element at mid is 0, swap with element at low and move both pointers.
            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]
                mid += 1
                low += 1
                
            # If element at mid is 1, move mid pointer.
            elif arr[mid] == 1:
                mid += 1
                
            # If element at mid is 2, swap with element at high and move high pointer.
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        
        return arr

# Driver code ends

# Example usage:
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    arr1 = [0, 2, 1, 2, 0]
    print("Original array (Example 1):", arr1)
    sorted_arr1 = sol.sort012(arr1, len(arr1))
    print("Sorted array (Example 1):", sorted_arr1)

    # Example 2
    arr2 = [0, 1, 0]
    print("\nOriginal array (Example 2):", arr2)
    sorted_arr2 = sol.sort012(arr2, len(arr2))
    print("Sorted array (Example 2):", sorted_arr2)