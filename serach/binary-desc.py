def binary_search_desc(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage:
arr = [10, 8, 6, 4, 2,22,25,45,78,99]
x = 6
result = binary_search_desc(arr, x)
print(result)  
