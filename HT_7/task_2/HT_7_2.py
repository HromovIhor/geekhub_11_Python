"""
Написати функцію, яка приймає два параметри: ім'я файлу та кількість символів.

На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу.
Кількість символів в блоках - та, яка введена в другому параметрі.
Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі
(наприклад, файл із двох символів і треба вивести по одному символу, то що виводити на місці середнього блоку символів?)
В репозиторій додайте і ті файли, по яким робили тести.
Як визначати середину файлу (з якої брать необхідні символи) - кількість символів поділити навпіл,
а отримане "вікно" символів відцентрувати щодо середини файла і взяти необхідну кількість.
В разі необхідності заокруглення одного чи обох параметрів - дивіться на свій розсуд.
   Наприклад:
   █ █ █ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ ░ █ █ █    - правильно
                     ⏫ центр

   █ █ █ ░ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ █ █ █    - неправильно
                     ⏫ центр
"""


# test.txt text:   itissome26weirdtestcasetext with n_char = 3 should be
#                    ['iti', 'ird', 'ext']

def func(file, n_char):
    empty_string = ''
    with open(file) as f:
        for i in f.readlines():
            empty_string += i

        if (n_char * 3) > len(empty_string):
            print("The number of characters is less '<' than the specified number")
        else:
            new_list = [empty_string[0:n_char]]

    a = len(empty_string) // 2
    number = n_char // 2
    if n_char % 2 != 0:
        center = empty_string[a - number:a + number + 1]
    else:
        center = empty_string[a - number:a + number]

    new_list.append(center)
    new_list.append(empty_string[-n_char:])

    print(new_list)


func('test.txt', 3)
