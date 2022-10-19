from cs50 import get_int

number = 0
while number < 1 or number > 8:
    number = get_int('Height: ')

for i in range(1, number+1):
    print(" " * (number - i), end='')
    print("#" * i)
