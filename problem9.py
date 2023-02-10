#Write a function that takes two lists as input and returns a new list that contains the
#elements that are common to both lists.
def common_elements(list1, list2):
    result = []
    for elem in list1:
        if elem in list2:
            result.append(elem)
    return result

