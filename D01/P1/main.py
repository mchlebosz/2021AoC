
from pathlib import Path
script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(lambda x: list(x[:len(x)-1].split()), f.readlines()))


result = list()
result.append(4)
result = inpu


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n")
