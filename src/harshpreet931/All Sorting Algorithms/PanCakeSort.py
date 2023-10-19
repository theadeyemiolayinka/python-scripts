def pancake_sort(arr):
    def flip(arr, i):
        return arr[:i+1][::-1] + arr[i+1:]

    for curr_size in range(len(arr), 1, -1):
        max_idx = arr.index(max(arr[:curr_size]))
        if max_idx != curr_size - 1:
            if max_idx != 0:
                arr = flip(arr, max_idx)
            arr = flip(arr, curr_size - 1)
