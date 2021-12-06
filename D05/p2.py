
from pathlib import Path
from math import copysign
script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(lambda x: list(x[:len(x)-1].split(" -> ")), f.readlines()))

ventCoord = list(
    map(lambda x: {'from': list(map(int, x[0].split(","))), 'to': list(map(int, x[1].split(",")))}, inpu))

# print(ventCoord)
xmax = 0
ymax = 0
for item in ventCoord:
    xmax = max(item['from'][0], xmax)
    xmax = max(item['to'][0], xmax)
    ymax = max(item['from'][1], ymax)
    ymax = max(item['to'][1], ymax)


Matrix = [[0 for x in range(xmax+1)] for y in range(ymax+1)]

for coord in ventCoord:
    if coord['from'][0] == coord['to'][0]:
        start = min(coord['from'][1], coord['to'][1])
        end = max(coord['from'][1], coord['to'][1])
        # print(coord)

        for i in range(start, end+1, 1):
            # print(coord['from'][0], i)
            Matrix[i][coord['from'][0]] += 1
    elif coord['from'][1] == coord['to'][1]:
        start = min(coord['from'][0], coord['to'][0])
        end = max(coord['from'][0], coord['to'][0])
        # print(coord)

        for i in range(start, end+1):
            # print(coord['from'][1], i)
            Matrix[coord['from'][1]][i] += 1
    else:

        startx = coord['from'][0]
        starty = coord['from'][1]
        endx = coord['to'][0]
        endy = coord['to'][1]
        # print(coord)
        for i in range(abs(startx-endx)+1):
            """ print(int(i*copysign(1, endx-startx)),
                  int(i*copysign(1, endy-starty))) """
            Matrix[starty + int(i*copysign(1, endy-starty))][startx +
                                                             int(i*copysign(1, endx-startx))] += 1


""" for x in Matrix:
    print(*x, sep='') """

larger_elements = 0
for item in Matrix:
    for i in item:
        if i >= 2:
            larger_elements += 1


result = list()
result.append([str(larger_elements)])


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n")
