# 7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!

def calculator(num_1, operator, num_2):
    if operator == "+":
        result = num_1+num_2
    elif operator == "-":
        result = num_1-num_2
    elif operator == "*":
        result = num_1*num_2
    elif operator == "/":
        if num_2:
            result = num_1/num_2
        else :
            result = "Oooops...division by zero isn't allowed."
    else:
        result = "Operation isn't supported, sorry."
    return result

print("Operators you can specify are: +, -, *, /")
number_1, operator, number_2 = str(input("Type the first number, the operator and the second number.\nNOTE: spaces are required!\n")).split(sep = " ")
print(calculator(int(number_1), operator, int(number_2)))
