import collections
from pathlib import Path
script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(lambda x: list(x[:len(x)-1].split()), f.readlines()))

polymer = inpu[0][0]

instructions = dict()
for item in inpu[2:]:
    instructions[item[0]] = item[2]


for j in range(10):
    newpolymer = ""

    for i in range(len(polymer)-1):
        #print(polymer[i:i+2], instructions[polymer[i:i+2]])
        newpolymer += polymer[i] + instructions[polymer[i:i+2]]
    newpolymer += polymer[-1]
    #print(polymer, newpolymer)
    polymer = newpolymer

least = collections.Counter(polymer).most_common()[-1]
most = collections.Counter(polymer).most_common(1)[0]
print(most[1] - least[1])

result = list()
result.append([str(most[1] - least[1])])


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n")
