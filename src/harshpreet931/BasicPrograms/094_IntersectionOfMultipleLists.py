def intersection_of_lists(lists):
    if not lists:
        return []
    result = set(lists[0])
    for lst in lists[1:]:
        result.intersection_update(lst)
    return list(result)

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [5, 6, 7, 8, 9]
result = intersection_of_lists([list1, list2, list3])
print("Intersection of lists:", result)
