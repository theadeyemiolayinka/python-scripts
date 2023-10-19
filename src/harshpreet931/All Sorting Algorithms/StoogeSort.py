def stooge_sort(arr, i=0, j=None):
    if j is None:
        j = len(arr) - 1

    if arr[j] < arr[i]:
        arr[i], arr[j] = arr[j], arr[i]

    if j - i > 1:
        t = (j - i + 1) // 3
        stooge_sort(arr, i, j - t)
        stooge_sort(arr, i + t, j)
        stooge_sort(arr, i, j - t)
