import random

arpakuutiot = []
maara = int(input("Anna arpakuutioiden määrä: "))
kerrat = 0

while kerrat < maara:
    kerrat = kerrat + 1
    arpakuutiot.append(random.randint(1,6))

print("Arpakuutioiden silmäluvut: ")
for x in arpakuutiot:
    print(x)