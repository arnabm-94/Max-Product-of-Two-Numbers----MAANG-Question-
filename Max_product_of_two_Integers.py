
'''
#Problem statement

#Max Product of Two Integers

Find the maximum product of two integers in an array where all elements are positive.

'''
#Solution : 1

def max_product(arr):
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements")
    
    # Initialize the two largest numbers
    max1 = max2 = float('-inf')
    
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    
    return max1 * max2

# Example usage
arr = [1, 7, 3, 4, 9, 5]
print(max_product(arr))  

# Output: 63 (9*7)

#=====================================================================================

#Solution : 2

def max_product(arr):   #Define a function named max_product that takes an input array arr.

    #Initialize two variables, max1 and max2, to store the two largest numbers in the array. 
    #Set both variables to 0 initially.
    # O(1), constant time initialization
    max1, max2 = 0, 0  
 
    # Iterate through the array
    #Iterate through the elements of the input array arr using a for loop. 
    #num represents the current element of the array.

    for num in arr:  # O(n), where n is the length of the array
        # If the current number is greater than max1, update max1 and max2
        
        #Check if the current number num is greater than the current maximum value max1.
        if num > max1:  # O(1), constant time comparison
            
            #If the above condition is True
#Then update the second-largest number max2 by assigning it the value of the current largest number max1.

            max2 = max1  # O(1), constant time assignment

#Update the largest number max1 by assigning it the value of the current number num.
            max1 = num  # O(1), constant time assignment
        # If the current number is greater than max2 but not max1, update max2
#If the above condition is False, check if the current number num is greater than the current second-largest number max2.
        elif num > max2:  # O(1), constant time comparison

#If the above condition is True, update the second-largest number max2 by assigning it the value of the current number num.
            max2 = num  # O(1), constant time assignment
 
#After the loop has finished iterating through the array, return the product of the two largest numbers, max1 and max2.
    # Return the product of the two largest numbers
    return max1 * max2  # O(1), constant time multiplication
 
arr = [1, 7, 3, 4, 9, 5]
print(max_product(arr))  # Output: 63 (9*7)


'''
Solution 2 Explaination :

#Time Complexity:

The time complexity of the max_product function is O(n), where n is the length of the input array arr. The reason for this complexity is that the function iterates through the input array once, comparing each element with max1 and max2 to find the two largest elements. There are no nested loops or other time-consuming operations, so the time complexity is linear.

#Space Complexity:

The space complexity of the max_product function is O(1), which means it uses a constant amount of extra memory regardless of the input size. In this case, the function uses two additional variables, max1 and max2, to store the two largest numbers in the array. No other data structures or memory allocations are required, so the space complexity remains constant regardless of the size of the input array.

'''
