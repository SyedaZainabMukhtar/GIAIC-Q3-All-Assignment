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

# Example usage
arr = [2, 3, 4, 10, 40, 50, 60, 70]
target = 10
result = binary_search(arr, target)
print(f"Element {target} is at index {result}" if result != -1 else "Element not found")