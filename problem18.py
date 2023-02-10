#rite a program to find the union and intersection of two lists.
def union_intersection(list1, list2):
    union = set(list1) | set(list2)
    intersection = set(list1) & set(list2)
    return union, intersection
