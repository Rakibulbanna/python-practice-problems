# Problem-8: Factorial Using Recursion


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


input = int(input("Enter a number: "))
print(factorial(input))
