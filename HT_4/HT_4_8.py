"""
Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку.
Тобто, функція приймає два аргументи:
список і величину зсуву (якщо ця величина додатня - пересуваємо з кінця на початок,
якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).

   Наприклад:
       fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
       fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
"""

hardcoded_list = [1, 2, 3, 4, 5]

def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]

some_number = int(input("Enter a number: "))
print(shift(hardcoded_list, some_number))
