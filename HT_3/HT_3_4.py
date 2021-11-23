"""4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат.
   Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат.
   Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3"""

def your_name(name):
    return "Hi " + str(name)

def your_age(age):
    return "\nYou are " + str(age) + " years old\n"

def animal(animal_name):
    return "Your dogs' name is " + str(animal_name)

def final_text(name, age, animal_name):
    return your_name(name) + your_age(age) + animal(animal_name)

print(final_text('Ihor', 30, 'Kurt'))
