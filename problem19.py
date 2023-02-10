#Write a function that takes a list of tuples as input and returns a new list of tuples where
#each tuple contains the sum and product of the elements in the original tuple.
def sum_product(tuples_list):
    result = []
    for tup in tuples_list:
        result.append((sum(tup), reduce(lambda x, y: x*y, tup)))
    return result
