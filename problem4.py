#Write a function that takes a string as input and returns the number of vowels and
#Consonants in the string.

def count_vowels_consonants(string):
    vowels = "aeiouAEIOU"
    vowels_count = 0
    consonants_count = 0
    for char in string:
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
    return (vowels_count, consonants_count)
