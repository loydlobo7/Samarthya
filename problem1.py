#Write a function that takes a list of numbers as input and returns the sum of all the even 
#numbers in the list.

def sum_of_evens(numbers):
    result = 0
    for num in numbers:
        if num % 2 == 0:
            result += num
    return result
