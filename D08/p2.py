
from pathlib import Path


def patternToNumber(x, pattern):
    x = "".join(sorted(x))
    return {
        "".join(sorted(pattern[0]+pattern[1]+pattern[2]+pattern[4]+pattern[5]+pattern[6])): '0',
        "".join(sorted(pattern[2]+pattern[5])): '1',
        "".join(sorted(pattern[0]+pattern[2]+pattern[3]+pattern[4]+pattern[6])): '2',
        "".join(sorted(pattern[0]+pattern[2]+pattern[3]+pattern[5]+pattern[6])): '3',
        "".join(sorted(pattern[1]+pattern[2]+pattern[3]+pattern[5])): '4',
        "".join(sorted(pattern[0]+pattern[1]+pattern[3]+pattern[5]+pattern[6])): '5',
        "".join(sorted(pattern[0]+pattern[1]+pattern[3]+pattern[4]+pattern[5]+pattern[6])): '6',
        "".join(sorted(pattern[0]+pattern[2]+pattern[5])): '7',
        "".join(sorted(pattern[0]+pattern[1]+pattern[2]+pattern[3]+pattern[4]+pattern[5]+pattern[6])): '8',
        "".join(sorted(pattern[0]+pattern[1]+pattern[2]+pattern[3]+pattern[5]+pattern[6])): '9',

    }[x]


script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(lambda x: list(
        map(lambda z: z.split(), list(x[:len(x)-1].split("|")))), f.readlines()))


suma = 0

for item in inpu:
    alfabet = item[0]
    alfabet.sort()
    alfabet.sort(key=len, reverse=False)
    for i in range(len(alfabet)):
        alfabet[i] = "".join(sorted(alfabet[i]))

    digitArray = [None] * 7

    digitArray[2] = alfabet[0]
    digitArray[5] = alfabet[0]
    digitArray[0] = alfabet[1].replace(
        alfabet[0][0], "").replace(alfabet[0][1], "")
    digitArray[1] = alfabet[2].replace(
        alfabet[0][0], "").replace(alfabet[0][1], "")
    digitArray[3] = digitArray[1]

    threeToFive = alfabet[3:6]
    for number in threeToFive:
        if number.count(digitArray[0]) == 1 and number.count(digitArray[2][0]) == 1 and number.count(digitArray[2][1]) == 1:
            three = number
            break
    cutthree = three.replace(digitArray[0], "").replace(
        digitArray[2][0], "").replace(digitArray[2][1], "").replace(
        digitArray[3][0], "").replace(digitArray[3][1], "")
    digitArray[6] = cutthree
    middle = three.replace(digitArray[0], "").replace(
        digitArray[2][0], "").replace(digitArray[2][1], "").replace(
        digitArray[6], "")
    digitArray[3] = middle
    digitArray[1] = digitArray[1].replace(digitArray[3], "")

    threeToFive.remove(three)

    for number in threeToFive:
        if number.count(digitArray[1]) == 1:
            five = number
            break

    a = five.count(digitArray[5][1])

    digitArray[5] = digitArray[5][a]
    digitArray[2] = digitArray[2].replace(digitArray[5], "")

    threeToFive.remove(five)

    digitArray[4] = threeToFive[0].replace(
        digitArray[0], "").replace(digitArray[2], "").replace(digitArray[3], "").replace(digitArray[6], "")

    digits = item[1]
    output = ""
    for digit in digits:
        output += patternToNumber(digit, digitArray)
    suma += int(output)

print(suma)

counter = 0
result = list()
result.append([str(suma)])


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n")
