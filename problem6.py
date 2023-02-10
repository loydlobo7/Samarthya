#Write a program to find the most common element in a string.
def most_common(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    most_common = None
    max_count = 0
    for char, count in char_count.items():
        if count > max_count:
            most_common = char
            max_count = count
    return most_common
