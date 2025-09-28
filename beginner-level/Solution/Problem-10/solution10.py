# Problem-10: Check if a Number is Prime


def is_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


input = int(input("Enter a number: "))
print(is_prime(input))
