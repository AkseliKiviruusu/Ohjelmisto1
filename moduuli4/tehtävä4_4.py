import random

LUKU = random.randint(1,10)
arvaus = int(input("Arvaa luku: "))

while LUKU != arvaus:
    if LUKU < arvaus:
        print("Liian suuri arvaus.")
    else:
        print("Liian pieni arvaus.")
    arvaus = int(input("Arvaa luku: "))

print("Oikein!")