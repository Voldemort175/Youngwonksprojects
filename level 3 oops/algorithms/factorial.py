##def factorial(n):
##    if n==1:
##        return 1
##    return n*(factorial(n-1))
##
##n=int(input())
##print(factorial(n)
##

# def fibonacci(n):         # without recursion
#     fib_seq = [0, 1]
#     while len(fib_seq) < n + 1:
#         fib_seq.append(fib_seq[-1] + fib_seq[-2])
#     return fib_seq

# Example usage
# print(fibonacci(5))  # Output: [0, 1, 1, 2, 3, 5]


# def fibonacci(n):       #with recursion 
#     # Base cases
#     if n == 0:
#         return [0]
#     elif n == 1:
#         return [0, 1]
#     # Recursive case
#     else:
#         fib_seq = fibonacci(n - 1)
#         fib_seq.append(fib_seq[-1] + fib_seq[-2])
#         return fib_seq

# # Example usage
# print(fibonacci(5))  # Output: 

# def sum_of_digits(n):
#     if n < 10:  # base case: single digit number
#         return n
#     else:
#         last_digit = n % 10
#         remaining_number = n // 10
#         return last_digit + sum_of_digits(remaining_number)

# # Example usage:
# num = int(input("Enter a number: "))
# result = sum_of_digits(num)
# print("Sum of digits:", result)


# def reverse_string(s):
    
#     if len(s) <= 1:  # base case: empty or single character string
#         return s
#     else:
#         first_char = s[0]
#         remaining_string = s[1:]
#         return reverse_string(remaining_string) + first_char

# # Example usage:
# string = input("Enter a string: ")
# result = reverse_string(string)
# print("Reversed string:", result)




# def pascal_triangle(n, row=0, triangle=[[1]]):
#     if row == n:  # base case: reached the desired number of rows
#         return triangle
#     else:
#         new_row = [1]  # first element of the new row is always 1
#         for i in range(1, len(triangle[row]) - 1):
#             new_row.append(triangle[row][i - 1] + triangle[row][i])
#         new_row.append(1)  # last element of the new row is always 1
#         triangle.append(new_row)
#         return pascal_triangle(n, row + 1, triangle)

# # Example usage:
# num_rows = int(input("Enter the number of rows: "))
# pascal_triangle = pascal_triangle(num_rows)
# for row in pascal_triangle:
#     print(" ".join(str(x) for x in row))

# def pascal(layer):
#     if len(layer) > 10:  # stop when the layer has more than 10 elements
#         return
#     print(" ".join(str(x) for x in layer))  # print the current layer
#     new_layer = [1]  # initialize the new layer with 1
#     for i in range(len(layer) - 1):
#         new_layer.append(layer[i] + layer[i + 1])  # calculate the sum of adjacent elements
#     new_layer.append(1)  # add 1 to the end of the new layer
#     pascal(new_layer)  # call the Pascal function again with the new layer

# # Start with the initial layer [1]
# pascal([20])

# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1  # not found

# # Example usage:
# arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# target = 23
# index = binary_search(arr, target)
# if index != -1:
#     print(f"Target {target} found at index {index}")
# else:
#     print(f"Target {target} not found in the array")


# def binary_search(arr, target, left=0, right=None):   # recursive binary search function
#     if right is None:
#         right = len(arr) - 1
#     if left > right:
#         return -1  # not found
#     mid = (left + right) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         return binary_search(arr, target, mid + 1, right)
#     else:
#         return binary_search(arr, target, left, mid - 1)

# # Example usage:
# arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# target = 23
# index = binary_search(arr, target)
# if index != -1:
#     print(f"Target {target} found at index {index}")
# else:
#     print(f"Target {target} not found in the array")


# def bubble_sort(arr):           #bubble sort
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# # Example usage:
# arr = [64, 34, 25, 12, 22, 11, 90]
# print("Original array:", arr)
# print("Sorted array:", bubble_sort(arr))


# def selection_sort(arr):          # selection sort
#     n = len(arr)
#     for i in range(n-1):
#         min_idx = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr

# # Example usage:
# arr = [64, 34, 25, 12, 22, 11, 90]
# print("Original array:", arr)
# print("Sorted array:", selection_sort(arr))


# Note: Selection Sort has a slight advantage over Bubble Sort 
# in that it only swaps elements when necessary, 
# whereas Bubble Sort swaps elements in every iteration.


# def selection_sort_recursive(arr, n):    #Recursive Selection Sort Algorithm
#     if n <= 1:
#         return arr
#     min_idx = 0
#     for i in range(1, n):
#         if arr[i] < arr[min_idx]:
#             min_idx = i
#     arr[0], arr[min_idx] = arr[min_idx], arr[0]
#     return selection_sort_recursive(arr[1:], n-1)

# # Example usage:
# arr = [64, 34, 25, 12, 22, 11, 90]
# print("Original array:", arr)
# print("Sorted array:", selection_sort_recursive(arr, len(arr)))
