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
        print(int(number, 2))
        return (int(packet["Ver"], 2), i+6)
    else:
        verSums = int(packet["Ver"], 2)
        if packet["LID"] == "1":
            amount = int(packet["Data"][1:12], 2)
            usedLength = 0
            for i in range(amount):
                out = resolvePacket(packet["Data"][12+usedLength:])
                verSums += out[0]
                usedLength += out[1]
            return (verSums, usedLength+11+7)
        if packet["LID"] == "0":
            dataLength = int(packet["Data"][1:16], 2)
            usedLength = 0
            while dataLength > usedLength:
                out = resolvePacket(packet["Data"][16+usedLength:])
                verSums += out[0]
                usedLength += out[1]
            return (verSums, usedLength+15+7)


script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(
        map(lambda x: bin(int(x[:len(x)-1], 16))[2:].zfill(len(x[:len(x)-1]) * 4), f.readlines()))

packets = []

for item in inpu:
    packets.append(resolvePacket(item)[0])

print(packets)


result = list()
result.append(4)
result = inpu


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n")
