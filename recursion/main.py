# program to find factorial using recursion

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


print(factorial(5))
