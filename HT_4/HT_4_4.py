"""
Написати функцію < prime_list >, яка прийматиме 2 аргументи:
початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.
"""

def prime_list(start, end):
    return list(i for i in range(start, end+1))

start_value = int(input("Enter the 'start' range: "))
end_value = int(input("Enter the 'end' range: "))

print(prime_list(start_value, end_value))
