"""
Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.
"""

def fibonacci(n):
    number_1 = 0
    number_2 = 1
    count = 0

    if n <= 0:
        print("Nothing to return, start from '1' at least")
    elif n == 1:
        print("Fibonacci sequence upto", n,":")
        print(number_1)
    else:
        print("Fibonacci sequence is: ")
        while count < n:
            print(number_1)
            nth = number_1 + number_2
            number_1 = number_2
            number_2 = nth
            count += 1

fibonacci(int(input("Enter a number: ")))
