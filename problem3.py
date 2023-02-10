#Write a program to find the largest and Smallest element in a list of numbers without
#inbuilt function.
def min_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return (smallest, largest)
