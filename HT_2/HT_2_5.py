dict1 = {
    'a': 10.1,
    'b': 32,
    'c': 10.1,
    'd': "text",
    'e': "result",
    'f': "text",
    'g': 47,
    'h': 47
         }
print(dict1)

final = {}

for key,value in dict1.items():
    if value not in final.values():
        final[key] = value

print(final)
