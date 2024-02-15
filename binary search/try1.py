def binary_search(target, l):
    l.sort()
    low = 0
    high = len(l) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = l[mid]
        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
l = [1, 2, 2, 4, 7, 6, 9, 8, 0]
value = 4
result = binary_search(value, l)
if result != -1:
    print("Target value",value," found at index",result)
else:
    print(f"Target value ",value," not found.")

