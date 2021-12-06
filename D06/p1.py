from pathlib import Path


def newFishes(fishes):
    zeroDayFishes = fishes[0]
    for i in range(0, 8):
        fishes[i] = fishes[i+1]
    fishes[6] += zeroDayFishes
    fishes[8] = zeroDayFishes
    return fishes


script_location = Path(__file__).absolute().parent
with open(script_location / 'test.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(lambda x: list(map(int, x.split(","))), f.readlines()))[0]

fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in inpu:
    fishes[i] += 1


for i in range(256):
    fishes = newFishes(fishes)

print(sum(fishes))

result = sum(fishes)


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    f.write(str(result))
