def func(file, number):
    with open(file, 'r') as f:
        text = f.read()

        if len(text) >= 3 * number:
            start = text[0:number]
            end = text[-number:]
            middle = text[(len(text) - number) // 2:(len(text) + number) // 2]
            return start, middle, end
        else:
            return "The number you specified is bigger '>' than the length of the line. You failed."


print(func('test.txt', int(input("Specify the number please: "))))
