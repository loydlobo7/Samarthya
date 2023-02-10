#Write a function that takes a list of dictionaries as input and returns a new dictionary that
#contains the count of the occurrences of each key across all dictionaries.
def count_keys(dict_list):
    result = {}
    for dic in dict_list:
        for key in dic:
            if key in result:
                result[key] += 1
            else:
                result[key] = 1
    return result
