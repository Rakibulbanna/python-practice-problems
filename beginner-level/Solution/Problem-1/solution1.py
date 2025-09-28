# Problem-1: Reverse a String Without Slicing

str = input("Enter a string: ")


def reverse_string(str):
    rev_str = ""
    length = len(str) - 1

    for i in range(length, -1, 1):
        rev_str += str[i]
    return rev_str


# print reverse string
print(reverse_string(str))
