# Problem-5: Flatten a Nested List


def flatten_list_by_recursion(arr, flatList):
    for i in arr:
        if type(i) == list:
            flatten_list_by_recursion(i, flatList)
        else:
            flatList.append(i)
    return flatList


arr = [1, 13, [2, 3], 546, [4, [5]]]
print(flatten_list_by_recursion(arr, []))
