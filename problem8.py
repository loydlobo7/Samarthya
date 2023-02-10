#Write a program to generate the first n Fibonacci numbers.
def fibonacci(n):
    result = []
    a, b = 0, 1
    for i in range(n):
        result.append(b)
        a, b = b, a + b
    return result
