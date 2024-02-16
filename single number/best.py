def find_single_number(lst):
    low = 0
    high = len(lst) - 1

    while low < high:
        mid = (low + high) // 2

        if mid % 2 == 0:
            if lst[mid] == lst[mid + 1]:
                low = mid + 2
            else:
                high = mid
        else:
            if lst[mid] == lst[mid - 1]:
                low = mid + 1
            else:
                high = mid

    return low

l = [1, 1, 2, 2, 8, 8, 4, 9, 9]
result = find_single_number(l)
print(result)
