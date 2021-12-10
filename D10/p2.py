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
            return True
    return False


script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(lambda x: x[:len(x)-1], f.readlines()))


notCorruptedRev = []

for l in inpu:
    lista = cropLine(l)
    if not findCorruptedPair(lista):
        notCorruptedRev.append(list(reversed(lista)))


outputs = []
brackets = {"{": 3, "[": 2, "(": 1, "<": 4}

# print(notCorruptedRev)
for l in notCorruptedRev:
    total = 0
    for i in range(len(l)):
        total *= 5
        total += brackets[l[i]]

    # print(total)
    outputs.append(total)

outputs.sort()

##
print(outputs[len(outputs) // 2])

result = list()

result.append([str(outputs[len(outputs) // 2])])


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n")
