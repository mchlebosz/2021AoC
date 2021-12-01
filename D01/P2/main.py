from pathlib import Path
script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(int, f.readlines()))

prev = sum(inpu[0:3])
counter = 0
for i in range(1, len(inpu)-2):
    now = sum(inpu[i:i+3])
    if now > prev:
        # print(prev, now)
        counter += 1
    prev = now

result = list()


result.append([str(counter)])


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n")
