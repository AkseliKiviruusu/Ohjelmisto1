import random

pisteet = int(input("Anna neliön sisälle piirrettävien pisteiden määrä: "))
kerrat = 0
sisalla = 0

while kerrat < pisteet:
    kerrat = kerrat + 1
    piste_1 = random.uniform(-1, 1)
    piste_2 = random.uniform(-1, 1)
    if piste_1 ** 2 + piste_2 ** 2 < 1:
        sisalla = sisalla + 1

pi = 4 * (sisalla / pisteet)
print(pi)