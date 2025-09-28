# Find Duplicates in a List


def find_duplicates_by_frequency_count(list):
    duplicates = {}
    for item in list:
        if item in duplicates:
            duplicates[item] += 1
        else:
            duplicates[item] = 1
    return [item for item, count in duplicates.items() if count > 1]


def find_duplicates_by_slice(list):
    duplicates = []
    for index, item in enumerate(list):
        if item in list[:index]:
            duplicates.append(item)
    return duplicates


list = ["ai", "ml", "python", "ml", "dl", "ai"]
# answer = find_duplicates_by_frequency_count(list)
# print(answer)
answer = find_duplicates_by_slice(list)
print(answer)
