def kadane(arr):
    curr = glob = arr[0]  # Initialize variables to the first element
    for i in range(1, len(arr)):
        curr = max(arr[i], curr + arr[i])  # Update current max sum
        if curr > glob:
            glob = curr  # Update global max sum if current max is greater
    return glob

# Example usage:
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
max_sum = kadane(arr)
print("Maximum contiguous sum is:", max_sum)
