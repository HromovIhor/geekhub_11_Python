list_of_numbers = list(input("Specify the comma separated numbers: ").split(", "))
check_up_number = input("Specify the check-up number: ")
for i in list_of_numbers:
    if check_up_number in i:
        print("True")
    else:
        print("False")
