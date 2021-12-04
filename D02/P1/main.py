
from pathlib import Path
script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(lambda x: list(x[:len(x)-1].split()), f.readlines()))

depth = 0
horizontal = 0

for item in inpu:
    value = int(item[1])
    if item[0] == "forward":
        horizontal += value
    if item[0] == "up":
        depth -= value
    if item[0] == "down":
        depth += value

result = list()
result.append([str(depth*horizontal)])


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n")
