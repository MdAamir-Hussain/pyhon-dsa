def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage:
arr = [2, 4, 6, 8, 10]
target = 6
result = binary_search(arr, target)
print(f"Element {target} found at index {result}" if result != -1 else "Element not found")
