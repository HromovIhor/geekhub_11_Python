"""Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення (кортеж):
периметр квадрата, площа квадрата та його діагональ."""

def square(a):
	p = 4*a
	s = a*a
	d = ((a**2) / 2)**0.5
	final = (p, s, d)
	return final

print(square(int(input("Enter the value of the square's side: "))))

"""
def square (a):
return (4*a, a**2, (2*a**2)**.5)

result = square(int(input("Enter the value of the square's side: ")))
print(result)
"""
