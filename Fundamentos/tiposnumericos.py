# Part 01

print(dir(int))
print(dir(float))

a = 5
b = 2.5

print(a / b)
print(a + b)
print(a * b)

print(type(a))
print(type(b))
print(type(a - b))

b.is_integer()
5.0.is_integer()

print(dir(int))
print(int.__add__(2, 5))
print(2 + 5)

print(abs(-2))

# Part 02
from decimal import Decimal, getcontext
getcontext().prec = 4
print(Decimal(1) / Decimal(7))
print(Decimal.max(Decimal(2), Decimal(3)))

print(1.1 + 2.2)
print(Decimal(1.1) + Decimal(2.2))