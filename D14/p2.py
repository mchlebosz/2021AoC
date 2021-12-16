from collections import Counter
from functools import cache
from pathlib import Path

script_location = Path(__file__).absolute().parent
with open(script_location / 'test.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(lambda x: list(x[:len(x)-1].split()), f.readlines()))

polymer = inpu[0][0]
counter = dict()
rules = dict()
for rule in inpu[2:]:
    left_right, _, mid = rule.partition(" -> ")
    left, right = tuple(left_right)
    rules[(left, right)] = mid


print(rules)


def solve(template, rules, n):

    if not len(template):
        return 0

    @cache
    def count_between(left, right, n):
        if n == 0:
            return Counter(left)
        mid = rules[(left, right)]
        return count_between(left, mid, n - 1) + count_between(mid, right, n - 1)
    counts = Counter(template[-1])
    for left, right in zip(template, template[1:]):
        counts += count_between(left, right, n)
    lowest, *_, highest = sorted(counts.values())

    return highest - lowest


print(solve(polymer, rules, 40))

result = list()
#result.append([str(most[1] - least[1])])


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n")
