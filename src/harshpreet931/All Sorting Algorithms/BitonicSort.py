def bitonic_sort(arr, up=True):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        first = bitonic_sort(arr[:mid], True)
        second = bitonic_sort(arr[mid:], False)
        return bitonic_merge(first + second, up)

def bitonic_merge(arr, up=True):
    if len(arr) == 1:
        return arr
    else:
        bitonic_compare(arr, up)
        mid = len(arr) // 2
        first = bitonic_merge(arr[:mid], up)
        second = bitonic_merge(arr[mid:], up)
        return first + second

def bitonic_compare(arr, up):
    dist = len(arr) // 2
    for i in range(dist):
        if (arr[i] > arr[i+dist]) == up:
            arr[i], arr[i+dist] = arr[i+dist], arr[i]
