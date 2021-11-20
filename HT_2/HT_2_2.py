replaceable_value = input("Please enter a number you want to replace with: ")
replaceable_value = int(replaceable_value)

list_of_tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([i[:-1] + (replaceable_value,) for i in list_of_tuples])


