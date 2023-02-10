#Write a function that takes a string as input and returns a dictionary with the frequency of
#each letter in the string.

def letter_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
