# Problem-4: Check if a Word is a Palindrome


def is_palindrome_by_array_reverse(word):
    word = word.lower()
    print(word)
    return word == word[::-1]


def is_palindrome_by_two_pointer(word):
    word = word.lower()
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome_by_loop(word):
    word = word.lower()
    half = len(word) / 2
    forward = 0
    backward = len(word) - 1
    for i in range(int(half)):
        if word[forward] != word[backward]:
            return False
        forward += 1
        backward -= 1
    return True


word = input("Enter a word: ")
# print(is_palindrome_by_array_reverse(word))
print(is_palindrome_by_two_pointer(word))
