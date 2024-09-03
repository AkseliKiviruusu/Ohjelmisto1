import random

def noppa():
    silmaluku = random.randint(1,6)
    while silmaluku < 6:
        print(silmaluku)
        silmaluku = random.randint(1,6)
    print(silmaluku)

noppa()