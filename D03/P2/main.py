
from collections import Counter
from pathlib import Path
script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(lambda x: x[:len(x)-1], f.readlines()))


def oxygen(arr):

    for i in range(len(arr[0])):
        if(len(arr) == 1):
            break
        ones = 0
        zeroes = 0
        for item in arr:
            ones += str(item)[i] == "1"
            zeroes += str(item)[i] == "0"
        if ones >= zeroes:
            arr = list(filter(lambda x: x[i] == '1', arr))
        else:
            arr = list(filter(lambda x: x[i] == '0', arr))

    return arr[0]


def co2(arr):
    for i in range(len(arr[0])):
        if(len(arr) == 1):
            break
        ones = 0
        zeroes = 0
        for item in arr:
            ones += str(item)[i] == "1"
            zeroes += str(item)[i] == "0"
        if ones >= zeroes:
            arr = list(filter(lambda x: x[i] == '0', arr))

        else:
            arr = list(filter(lambda x: x[i] == '1', arr))

    return arr[0]


oxygen = oxygen(inpu)
co2 = co2(inpu)


result = list()
result.append([str(int(oxygen, 2) * int(co2, 2))])


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n")
