#Write a program to convert a given number to binary, octal, and hexadecimal.
def convert_number_systems(number):
    binary = bin(number)
    octal = oct(number)
    hexadecimal = hex(number)
    return binary, octal, hexadecimal
