
from pathlib import Path
import statistics
script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(int, f.readlines()[0].split(",")))


inpu = sorted(inpu)
median = statistics.median(inpu)
print(inpu, median)
sumFuel = 0
for i in inpu:
    sumFuel += abs(i-int(median))

result = list()
result.append([str(sumFuel)])


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n")
