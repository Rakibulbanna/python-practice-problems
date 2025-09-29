# Problem-2: Group Anagrams Together


def group_anagrams(tags):
    container = {}
    for i in tags:
        sorted_tag = "".join(sorted(i))
        if sorted_tag in container:
            container[sorted_tag].append(i)
        else:
            container[sorted_tag] = [i]

    return list(container.values())


# tags = input("Enter the tags: ")
tags = ["bat", "tab", "cat", "act"]
print(group_anagrams(tags))
