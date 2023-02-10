#Write a function that takes a string as input and returns the longest substring without
#repeating characters.
def longest_substring(string):
    char_set = set()
    start = 0
    max_len = 0
    current_len = 0
    for i, char in enumerate(string):
        if char in char_set:
            while char in char_set:
                char_set.remove(string[start])
                start += 1
                current_len -= 1
        char_set.add(char)
        current_len += 1
        max_len = max(max_len, current_len)
    return max_len
