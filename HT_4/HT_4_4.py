"""
Написати функцію < prime_list >, яка прийматиме 2 аргументи:
початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.
"""

def prime_list(start, end):
    prime_list = []
    for n in range(start, end):
        if n > 1:
            for i in range(2,n):
                if(n % i == 0):
                    break
            else:
                prime_list.append(n)
    return prime_list

start_value = int(input("Enter the 'start' range: "))
end_value = int(input("Enter the 'end' range: "))

print(prime_list(start_value, end_value))
