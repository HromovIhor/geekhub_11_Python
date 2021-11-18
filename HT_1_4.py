number_of_strings = int(input("Specify the number of strings you want to concatenate? - "))

final_string = ""

for i in range(number_of_strings):
    input_string = str(input(""))
    final_string += input_string

print(final_string)
