
from pathlib import Path
script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(lambda x: list(x[:len(x)-1].split()), f.readlines()))


coord = inpu[:inpu.index([])]
instruction = inpu[inpu.index([])+1:]


coord = list(
    map(lambda x: {'x': int(x[0].split(',')[0]), 'y': int(x[0].split(',')[1])}, coord))
maxX = 0
maxY = 0
for item in coord:
    maxX = max(maxX, item['x'])
    maxY = max(maxY, item['y'])
#print(maxX, maxY)

matrix = [[' ' for i in range(maxX+1)] for j in range(maxY+1)]
for item in coord:
    matrix[item['y']][item['x']] = '█'
# print('\n'.join(map(''.join, matrix)))

# print(firstOrder)
# for inst in instruction:
order = instruction[0][2].split('=')

if order[0] == 'y':
    axis = int(order[1])
    for i in range(axis+1):
        for j in range(maxX+1):
            if axis+i < maxY+1 and axis-i >= 0 and matrix[axis+i][j] == "█":
                matrix[axis-i][j] = "█"
                matrix[axis+i][j] = ' '
else:
    axis = int(order[1])
    for i in range(axis+1):
        for j in range(maxY+1):
            if axis+i < maxX + 1 and axis-i >= 0 and matrix[j][axis+i] == "█":
                matrix[j][axis-i] = "█"
                matrix[j][axis+i] = ' '

#print('\n'.join(map(''.join, matrix)))
out = sum(x.count('█') for x in matrix)
print(out)


result = list()
result.append([str(out)])
#result = matrix


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write("".join(i)+"\n")
