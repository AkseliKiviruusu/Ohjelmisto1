import math
import random

NELIO = 2 * 2
YMPYRA = (1 ** 2) * math.pi

pisteet = int(input("Anna neliön sisälle piirrettävien pisteiden määrä: "))
kerrat = 0
sisalla = 0

while kerrat < pisteet:
    kerrat = kerrat + 1
    piste = random.uniform(0, 4)
    if piste < YMPYRA:
        sisalla = sisalla + 1

pi = 4 * (sisalla / pisteet)
print()
print(f"pi likiarvo: {pi}")