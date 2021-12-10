from pathlib import Path


def cropLine(line):
    closeBrackets = {"{": "}", "[": "]", "(": ")", "<": ">"}
    s = []
    for t in line:
        s.append(t)
        while len(s) >= 2 and s[-2] in closeBrackets and s[-1] == closeBrackets[s[-2]]:
            s.pop()

            s.pop()
    return s


def findCorruptedPair(line):
    closing = {"}": 1197, "]": 57,  ")": 3,  ">": 25137}
    for i in range(1, len(line)):
        if line[i] in closing:
            return closing[line[i]]
    return 0


script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(lambda x: x[:len(x)-1], f.readlines()))

total = 0

for l in inpu:
    lista = cropLine(l)
    # print(lista)
    if findCorruptedPair(lista) > 0:
        print(l)
    total += findCorruptedPair(lista)

print(total)


result = list()
result.append([str(total)])


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n")
