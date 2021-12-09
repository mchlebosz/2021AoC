
from pathlib import Path
script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(lambda x: list(map(int, x[:len(x)-1])), f.readlines()))

# print(inpu)

lowpoints = list()

newList = [[9 for j in range(len(inpu[0])+2)]for i in range(len(inpu)+2)]

# print(newList)

for i in range(len(inpu)):
    for j in range(len(inpu[0])):
        newList[i+1][j+1] = inpu[i][j]

# print(newList)

for i in range(1, len(inpu)+1):
    for j in range(1, len(inpu[0])+1):
        if (newList[i][j] < newList[i][j-1] and newList[i][j] < newList[i][j+1] and newList[i][j] < newList[i-1][j] and newList[i][j] < newList[i+1][j]):
            lowpoints.append(newList[i][j]+1)
# print(lowpoints)
print(sum(lowpoints))
result = list()
result.append([str(sum(lowpoints))])


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:
        f.write(str(i)+"\n")
