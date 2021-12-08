
from pathlib import Path
script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(lambda x: list(
        map(lambda z: z.split(), list(x[:len(x)-1].split("|")))), f.readlines()))

# print(inpu)

counter = 0
for item in inpu:
    for word in item[1]:
        if len(word) == 2 or len(word) == 3 or len(word) == 4 or len(word) == 7:
            counter += 1

result = list()
result.append([str(counter)])


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n")
