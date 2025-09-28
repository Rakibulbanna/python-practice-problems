# Count Vowels in a Sentence
def count_vowels(str):
    vowels = "aeiou"
    count = 0
    for char in str:
        if char.lower() in vowels:
            count += 1
    return count


str = input("Enter a string: ")
print(count_vowels(str))
