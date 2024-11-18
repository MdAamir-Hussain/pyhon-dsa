def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Example usage:
arr = [2, 4, 6, 8, 10]
target = 6
result = linear_search(arr, target)
print(f"Element {target} found at index {result}" if result != -1 else "Element not found")
