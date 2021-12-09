

from pathlib import Path
script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(lambda x: list(map(int, x[:len(x)-1])), f.readlines()))

# print(inpu)
heightPoints = [[9 for j in range(len(inpu[0])+2)]for i in range(len(inpu)+2)]


def sumBasins(i, j):
    global heightPoints
    if heightPoints[i][j] == 9 or i < 0 or j < 0:
        return 0
    heightPoints[i][j] = 9
    return 1 + sumBasins(i-1, j) + sumBasins(i, j-1) + sumBasins(i+1, j) + sumBasins(i, j+1)


baisins = list()


# print(heightPoints)

for i in range(len(inpu)):
    for j in range(len(inpu[0])):
        heightPoints[i+1][j+1] = inpu[i][j]

# print(heightPoints)

for i in range(1, len(inpu)+1):
    for j in range(1, len(inpu[0])+1):
        if (heightPoints[i][j] < heightPoints[i][j-1] and heightPoints[i][j] < heightPoints[i][j+1] and heightPoints[i][j] < heightPoints[i-1][j] and heightPoints[i][j] < heightPoints[i+1][j]):
            baisins.append(sumBasins(i, j))

baisins.sort(reverse=True)
# print(baisins)
print(baisins[0]*baisins[1] * baisins[2])
result = list()
result.append([str(sum(baisins))])


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:
        f.write(str(i)+"\n")
