from cs50 import get_float

change = 0
while change <= 0:
    change = get_float('Change owed: ')

change = round(change*100)
count = 0
quarter, dime, nickel, penny = 25, 10, 5, 1
while change >= quarter:
    count += 1
    change = change - quarter
while change >= dime:
    count += 1
    change = change - dime
while change >= nickel:
    count += 1
    change = change - nickel
while change >= penny:
    count += 1
    change = change - penny

print(count)
