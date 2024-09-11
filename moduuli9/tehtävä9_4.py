import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinennopeus, kuljettumatka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinennopeus = tamanhetkinennopeus
        self.kuljettumatka = kuljettumatka

    def kiihdyta(self, nopeuden_muutos):
        if 0 <= nopeuden_muutos + self.tamanhetkinennopeus <= self.huippunopeus:
            self.tamanhetkinennopeus = self.tamanhetkinennopeus + nopeuden_muutos
        elif self.tamanhetkinennopeus + nopeuden_muutos <= 0:
            self.tamanhetkinennopeus = 0
        else:
            self.tamanhetkinennopeus = self.huippunopeus

    def kulje(self, tunnit):
        self.kuljettumatka += tunnit * self.tamanhetkinennopeus

loppu = False
autot = []
a = 0
while True:
    if a < 10:
        autot.append(Auto(f"ABC-{a+1}", random.randint(100,200),0,0))
    else:
        break
    a += 1

def tunti_kerroin():
    tunnit = 0
    for i in range(len(autot)):
        autot[i].kiihdyta(random.randint(-10, 15))
        autot[i].kulje(1)
        tunnit += 1
    return autot

def check_loppu(d):
    for i in range(len(autot)):
        if autot[i].kuljettumatka > 10000:
            d = True
            break
    return d

#Pääohjelma (kilpailu)

def kilpailu():
    loppu = False
    while loppu == False:
        tunti_kerroin()
        loppu = check_loppu(False)
    for i in range(len(autot)):
        print(f"Rekisteri:{autot[i].rekisteritunnus}")
        print(f"Huippunopeus:{autot[i].huippunopeus}")
        print(f"Nopeus lopussa:{autot[i].tamanhetkinennopeus}")
        print(f"Kuljettumatka:{autot[i].kuljettumatka}")
        print("------------------------")
    for i in range(len(autot)):
        if autot[i].kuljettumatka > 10000:
            print(f"Auto {autot[i].rekisteritunnus} voitti")
    return

kilpailu()