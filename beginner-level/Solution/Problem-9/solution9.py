# Problem-9: Sum of Digits of an Integer


def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum


input = int(input("Enter a number: "))
print(sum_of_digits(input))
