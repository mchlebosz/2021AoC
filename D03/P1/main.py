
from pathlib import Path
script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(lambda x: list(x[:len(x)-1].split()), f.readlines()))

gammaRate = ""
epsilonRate = ""
wordSize = len(inpu[0][0])

for i in range(wordSize):
    ones = 0
    zeroes = 0
    for item in inpu:
        ones += str(item[0])[i].count("1")
        zeroes += str(item[0])[i].count("0")

    if ones > zeroes:
        gammaRate += "1"
        epsilonRate += "0"
    else:
        gammaRate += "0"
        epsilonRate += "1"


powerCon = int(gammaRate, 2) * int(epsilonRate, 2)

print(powerCon)

result = list()
result.append([str(powerCon)])


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n")
