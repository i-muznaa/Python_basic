def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2   # middle index

        if arr[mid] == target:
            return mid            # element found, return index
        elif arr[mid] < target:
            low = mid + 1         # search in right half
        else:
            high = mid - 1        # search in left half

    return -1   # not found


# Example use
arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = int(input("Enter a number: "))

result = binary_search(arr, target)

print("Index:", result)
