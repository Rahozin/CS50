import math

number = 0
while number <= 0:
    number = int(input('Number: '))
    strnumber = str(number)
while len(strnumber) < 16:
    strnumber = "0" + strnumber
numbers = strnumber
d1 = int(numbers[0])
d2 = int(numbers[1])
d3 = int(numbers[2])
d4 = int(numbers[3])
d5 = int(numbers[4])
d6 = int(numbers[5])
d7 = int(numbers[6])
d8 = int(numbers[7])
d9 = int(numbers[8])
d10 = int(numbers[9])
d11 = int(numbers[10])
d12 = int(numbers[11])
d13 = int(numbers[12])
d14 = int(numbers[13])
d15 = int(numbers[14])
d16 = int(numbers[15])

ds1 = math.floor(d1*2/10)+round(d1*2 % 10)
ds3 = math.floor(d3*2/10)+round(d3*2 % 10)
ds5 = math.floor(d5*2/10)+round(d5*2 % 10)
ds7 = math.floor(d7*2/10)+round(d7*2 % 10)
ds9 = math.floor(d9*2/10)+round(d9*2 % 10)
ds11 = math.floor(d11*2/10)+round(d11*2 % 10)
ds13 = math.floor(d13*2/10)+round(d13*2 % 10)
ds15 = math.floor(d15*2/10)+round(d15*2 % 10)

final_d = d2+d4+d6+d8+d10+d12+d14+d16+ds1+ds3+ds5+ds7+ds9+ds11+ds13+ds15

if final_d % 10 == 0 and number > 1000000000000:
    if d1 == 5 and d2 <= 5:
        print("MASTERCARD")
    elif d1 == 4 or (d1 == 0 and d2 == 0 and d3 == 0):
        print("VISA")
    elif d1 == 0 and d2 == 3 and (d3 == 4 or d3 == 7):
        print("AMEX")
    else:
        print("INVALID")
else:
    print("INVALID")
