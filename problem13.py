#Write a program to calculate the mean and median of a list of numbers.
def mean_median(numbers):
    numbers.sort()
    length = len(numbers)
    mean = sum(numbers) / length
    if length % 2 == 0:
        median = (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    else:
        median = numbers[length // 2]
    return mean, median
