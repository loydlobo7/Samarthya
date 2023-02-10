# Write a program to reverse a string using loops only.
def reverse_string(string):
    result = ""
    for i in range(len(string) - 1, -1, -1):
        result += string[i]
    return result
