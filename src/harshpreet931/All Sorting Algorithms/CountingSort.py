def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    sorted_arr = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    for num in reversed(arr):
        sorted_arr[count[num] - 1] = num
        count[num] -= 1

    return sorted_arr
