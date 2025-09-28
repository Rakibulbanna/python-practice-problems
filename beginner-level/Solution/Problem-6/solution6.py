# Capitalize First Letter of Each Word


def capitalize_first_letter_of_each_word(str):
    words = str.split(" ")
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    # print(words)
    return " ".join(words)


str = "python for web developers"
print(capitalize_first_letter_of_each_word(str))
