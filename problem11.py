#Write a function that takes a string as input and returns a new string with all the spaces
#removed using loops.
def remove_spaces(string):
    result = ""
    for char in string:
        if char != " ":
            result += char
    return result
