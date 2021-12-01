
from pathlib import Path
script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(lambda x: list(x[:len(x)-1].split()), f.readlines()))

prev = int(inpu[0][0])
counter = 0
for i in range(1, len(inpu)):
    now = int(inpu[i][0])
    if now > prev:
        counter += 1
    prev = now

result = list()
result.append([str(counter)])


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n")
