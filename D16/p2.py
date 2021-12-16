from pathlib import Path


def createPacket(item):
    return {"Ver": item[:3], "ID": item[3:6],
            "Data": item[6:], "LID": item[6]}


def resolvePacket(packet):
    packet = createPacket(packet)
    if packet["ID"] == "100":
        number = ""
        i = 0
        while packet["Data"][i] == "1":
            number += packet["Data"][i+1:i+5]
            i += 5
        number += packet["Data"][i+1:i+5]
        i += 5
        return (int(packet["Ver"], 2), i+6, int(number, 2))
    if packet["ID"] == "000":
        # SUMPACKET
        verSums = int(packet["Ver"], 2)
        numSums = 0
        if packet["LID"] == "1":
            amount = int(packet["Data"][1:12], 2)
            usedLength = 0
            for i in range(amount):
                out = resolvePacket(packet["Data"][12+usedLength:])
                verSums += out[0]
                usedLength += out[1]
                numSums += out[2]
            return (verSums, usedLength+11+7, numSums)
        if packet["LID"] == "0":
            dataLength = int(packet["Data"][1:16], 2)
            usedLength = 0
            while dataLength > usedLength:
                out = resolvePacket(packet["Data"][16+usedLength:])
                verSums += out[0]
                usedLength += out[1]
                numSums += out[2]
            return (verSums, usedLength+15+7, numSums)
    if packet["ID"] == "001":
        # ProductPACKET
        verSums = int(packet["Ver"], 2)
        numProducts = 1
        if packet["LID"] == "1":
            amount = int(packet["Data"][1:12], 2)
            usedLength = 0
            for i in range(amount):
                out = resolvePacket(packet["Data"][12+usedLength:])
                verSums += out[0]
                usedLength += out[1]
                numProducts *= out[2]
            return (verSums, usedLength+11+7, numProducts)
        if packet["LID"] == "0":
            dataLength = int(packet["Data"][1:16], 2)
            usedLength = 0
            while dataLength > usedLength:
                out = resolvePacket(packet["Data"][16+usedLength:])
                verSums += out[0]
                usedLength += out[1]
                numProducts *= out[2]
            return (verSums, usedLength+15+7, numProducts)
    if packet["ID"] == "010":
        # MinPACKET
        verSums = int(packet["Ver"], 2)
        numMin = float("inf")
        if packet["LID"] == "1":
            amount = int(packet["Data"][1:12], 2)
            usedLength = 0
            for i in range(amount):
                out = resolvePacket(packet["Data"][12+usedLength:])
                verSums += out[0]
                usedLength += out[1]
                numMin = min(out[2], numMin)
            return (verSums, usedLength+11+7, numMin)
        if packet["LID"] == "0":
            dataLength = int(packet["Data"][1:16], 2)
            usedLength = 0
            while dataLength > usedLength:
                out = resolvePacket(packet["Data"][16+usedLength:])
                verSums += out[0]
                usedLength += out[1]
                numMin = min(out[2], numMin)
            return (verSums, usedLength+15+7, numMin)
    if packet["ID"] == "011":
        # MaxPACKET
        verSums = int(packet["Ver"], 2)
        numMax = -3
        if packet["LID"] == "1":
            amount = int(packet["Data"][1:12], 2)
            usedLength = 0
            for i in range(amount):
                out = resolvePacket(packet["Data"][12+usedLength:])
                verSums += out[0]
                usedLength += out[1]
                numMax = max(out[2], numMax)
            return (verSums, usedLength+11+7, numMax)
        if packet["LID"] == "0":
            dataLength = int(packet["Data"][1:16], 2)
            usedLength = 0
            while dataLength > usedLength:
                out = resolvePacket(packet["Data"][16+usedLength:])
                verSums += out[0]
                usedLength += out[1]
                numMax = max(out[2], numMax)
            return (verSums, usedLength+15+7, numMax)
    if packet["ID"] == "101":
        # GreaterPACKET
        verSums = int(packet["Ver"], 2)
        numGreater = 1
        lastPacket = 1
        if packet["LID"] == "1":
            amount = int(packet["Data"][1:12], 2)
            usedLength = 0
            for i in range(amount):
                out = resolvePacket(packet["Data"][12+usedLength:])
                verSums += out[0]
                usedLength += out[1]
                numGreater = lastPacket > out[2]
                lastPacket = out[2]
            return (verSums, usedLength+11+7, int(numGreater))
        if packet["LID"] == "0":
            dataLength = int(packet["Data"][1:16], 2)
            usedLength = 0
            while dataLength > usedLength:
                out = resolvePacket(packet["Data"][16+usedLength:])
                verSums += out[0]
                usedLength += out[1]
                numGreater = lastPacket > out[2]
                lastPacket = out[2]
            return (verSums, usedLength+15+7, int(numGreater))
    if packet["ID"] == "110":
        # LessPACKET
        verSums = int(packet["Ver"], 2)
        numLess = 1
        lastPacket = 1
        if packet["LID"] == "1":
            amount = int(packet["Data"][1:12], 2)
            usedLength = 0
            for i in range(amount):
                out = resolvePacket(packet["Data"][12+usedLength:])
                verSums += out[0]
                usedLength += out[1]
                numLess = lastPacket < out[2]
                lastPacket = out[2]
            return (verSums, usedLength+11+7, int(numLess))
        if packet["LID"] == "0":
            dataLength = int(packet["Data"][1:16], 2)
            usedLength = 0
            while dataLength > usedLength:
                out = resolvePacket(packet["Data"][16+usedLength:])
                verSums += out[0]
                usedLength += out[1]
                numLess = lastPacket < out[2]
                lastPacket = out[2]
            return (verSums, usedLength+15+7, int(numLess))
    if packet["ID"] == "111":
        # EqualPACKET
        verSums = int(packet["Ver"], 2)
        numEqual = 1
        lastPacket = 1
        if packet["LID"] == "1":
            amount = int(packet["Data"][1:12], 2)
            usedLength = 0
            for i in range(amount):
                out = resolvePacket(packet["Data"][12+usedLength:])
                verSums += out[0]
                usedLength += out[1]
                numEqual = lastPacket == out[2]
                lastPacket = out[2]
            return (verSums, usedLength+11+7, int(numEqual))
        if packet["LID"] == "0":
            dataLength = int(packet["Data"][1:16], 2)
            usedLength = 0
            while dataLength > usedLength:
                out = resolvePacket(packet["Data"][16+usedLength:])
                verSums += out[0]
                usedLength += out[1]
                numEqual = lastPacket == out[2]
                lastPacket = out[2]
            return (verSums, usedLength+15+7, int(numEqual))


script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(
        map(lambda x: bin(int(x[:len(x)-1], 16))[2:].zfill(len(x[:len(x)-1]) * 4), f.readlines()))

packets = []

for item in inpu:
    packets.append([str(resolvePacket(item)[2])])

print(packets)


result = packets


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n")
