"""
Вводиться число.
Якщо це число додатне, знайти його квадрат, якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.
"""

def some_function(n):
    if n > 0:
        n *= n
    elif n==0:
        return n
    else:
        n += 100
    return n

print(some_function(int(input("Enter a number: "))))
