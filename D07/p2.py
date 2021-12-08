
from pathlib import Path
import statistics
script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(int, f.readlines()[0].split(",")))


inpu = sorted(inpu)
median = statistics.median(inpu)
print(inpu[0], inpu[-1], median)

minSumFuel = float("inf")
for currPos in range(inpu[-1]):
    print((currPos/inpu[-1])*100, "%")
    currentSumFuel = 0

    for item in inpu:
        currentSumFuel += sum(range(1, abs(int(currPos) - int(item))+1))
        #print(currPos, item, numFuel)
    # print(currentSumFuel)
    minSumFuel = min(minSumFuel, currentSumFuel)


print(minSumFuel)

result = list()
result.append([str(minSumFuel)])


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n")
