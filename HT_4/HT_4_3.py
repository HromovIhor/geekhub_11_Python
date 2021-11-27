"""
Написати функцию < is_prime >, яка прийматиме 1 аргумент:
число від 0 до 1000, и яка вертатиме True, якщо це число просте, и False - якщо ні.
"""

def is_prime(a):
    if a < 2:
        return False
    for i in range(2, (a//2)+1):
        if a % i == 0:
            return False
    else:
        return True

print(is_prime(int(input("Enter a number: "))))
