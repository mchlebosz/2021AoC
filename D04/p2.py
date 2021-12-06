from pathlib import Path
from collections import Counter


def splitBingoes(bingoes):
    newBingoes = list()
    for i in range(int(len(bingoes)/6)):
        tempBingo = list()
        tempBingo.append(bingoes[6*i+1])
        tempBingo.append(bingoes[6*i+2])
        tempBingo.append(bingoes[6*i+3])
        tempBingo.append(bingoes[6*i+4])
        tempBingo.append(bingoes[6*i+5])
        newBingoes.append(tempBingo)
    return newBingoes


def replaceElem(bingo, a):
    newBingo = [["" for _ in range(5)] for _ in range(5)]
    for i in range(len(bingo)):
        for j in range(len(bingo[i])):
            if bingo[i][j] == a:
                newBingo[i][j] = "B"
            else:
                newBingo[i][j] = bingo[i][j]
    # print(newBingo)
    return newBingo


def checkBingo(bingo):
    for i in range(5):
        if bingo[i].count("B") == 5:

            return True
        if(bingo[0][i] == "B" and bingo[1][i] == "B" and
                bingo[2][i] == "B" and bingo[3][i] == "B" and bingo[4][i] == "B"):

            return True
    return False


def removeBingoes(bingoes):
    filledBingo = [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], [
        'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B']]
    bSize = len(bingoes)
    i = 0
    for i in range(bSize):
        if checkBingo(bingoes[i]):
            bingoes[i] = filledBingo
    bingoes = list(filter((filledBingo).__ne__, bingoes))
    return bingoes


script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    numbers = f.readline()[: -1].split(",")
    bingoes = list(map(lambda x: x[: len(x)-1].split(), f.readlines()))

bingoes = splitBingoes(bingoes)


foundBingo = list()
bSize = len(bingoes)

for number in numbers:

    print(number, bingoes)

    bingoes = list(map(lambda x: replaceElem(x, number), bingoes))
    if bSize > 1:
        bingoes = removeBingoes(bingoes)
    bSize = len(bingoes)
    if bSize <= 1 and checkBingo(bingoes[0]):
        foundBingo = bingoes[0]
        foundAtNum = int(number)
        # print(bingoes)
        break


# print(bingoes, "\n")
print(foundAtNum, foundBingo)

sumBingo = 0
for row in foundBingo:
    for i in row:
        if i != "B":
            sumBingo += int(i)


# print(foundAtNum*sumBingo)

result = [[str(foundAtNum*sumBingo)]]

with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n")
