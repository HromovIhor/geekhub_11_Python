def concatenate_list(list):
    final = ''
    for i in list:
        final += str(i)
    return final

print(concatenate_list([1, "smaller", "than", 2, "but", "bigger", "than", 0.5]))
