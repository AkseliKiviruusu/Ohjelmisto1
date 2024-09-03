import random

def noppa(tahkot):
    silmaluku = random.randint(1,tahkot)
    while silmaluku < tahkot:
        print(silmaluku)
        silmaluku = random.randint(1,tahkot)
    print(silmaluku)
    return

noppa(int(input("Anna nopan tahkojen määrä: ")))