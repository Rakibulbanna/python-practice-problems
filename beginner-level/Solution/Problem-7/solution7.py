# Find Missing Number in a Sequence


def find_missing_number_in_sequence(arr):
    arr.sort()
    n = arr[-1]
    # print("n__", n)
    expected_sum = (n * (n + 1)) / 2
    # print("expected_sum__", expected_sum)
    actual_sum = 0
    for i in arr:
        actual_sum += i
    # print("actual_sum__", actual_sum)
    return expected_sum - actual_sum


arr = [1, 2, 4, 5]
print(find_missing_number_in_sequence(arr))
