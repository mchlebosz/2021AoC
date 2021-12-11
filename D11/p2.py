
from pathlib import Path
script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(lambda x: list(map(int, list(x)[:-1])), f.readlines()))


hasFlashed = [[False for x in range(10)] for y in range(10)]


def printArray(array):
    for i in array:
        print("".join(map(str, i)))
    print("\n")


def propegateFlash(i, j):
    global inpu
    global hasFlashed
    hasFlashed[i][j] = True
    for k in range(3):
        for v in range(3):
            if (k != 1 or v != 1) and 0 <= i+k - 1 < 10 and 0 <= j+v-1 < 10:
                inpu[i+k - 1][j+v-1] += 1
                if inpu[i+k-1][j+v - 1] > 9 and not hasFlashed[i+k-1][j+v-1]:
                    propegateFlash(i+k-1, j+v - 1)


# print(inpu)
counter = 1

while True:
    for i in range(10):
        for j in range(10):
            inpu[i][j] += 1
    for i in range(10):
        for j in range(10):
            if inpu[i][j] > 9 and not hasFlashed[i][j]:
                propegateFlash(i, j)
    for i in range(10):
        for j in range(10):
            if inpu[i][j] > 9:
                inpu[i][j] = 0
    if sum(x.count(0) for x in inpu) == 100 or counter > 1000:
        break
    hasFlashed = [[False for x in range(10)] for y in range(10)]
    counter += 1

    # printArray(inpu)

print(counter)

""" result = list()
result.append(4)
result = inpu


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n") """
