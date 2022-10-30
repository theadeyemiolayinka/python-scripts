def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
 
 
arr = [ 1, 4, 5, 8, 12 ]
x = int(input("ENTER THE ELEMENT TO BE SEARCHED"))
 
result = binary_search(arr, x)
 
if result != -1:
    print("ELEMENT IS PRESENT AT INDEX", str(result))
else:
    print("ELEMENT IS NOT PRESENT")
