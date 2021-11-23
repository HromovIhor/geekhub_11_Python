"""5. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
-  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї), пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
-  Повиннi опрацювати такi умови:
-  x > y;       вiдповiдь - х бiльше нiж у на z
-  x < y;       вiдповiдь - у бiльше нiж х на z
-  x == y.      вiдповiдь - х дорiвнює z"""

x = int(input("Specify 'x' valuable: "))
y = int(input("Specify 'y' valuable: "))

def final_result():
    if x > y:
        result = x - y
        return print(f'{x} більше ніж {y} на {result}')
    elif x < y:
        result = y - x
        return print(f'{y} більше ніж {x} на {result}')
    else:
        return print(f'{x} дорівнює {y}')

final_result()
