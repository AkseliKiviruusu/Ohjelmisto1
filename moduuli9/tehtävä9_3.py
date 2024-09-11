class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinennopeus, kuljettumatka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinennopeus = tamanhetkinennopeus
        self.kuljettumatka = kuljettumatka
    def kiihdyta(self, nopeuden_muutos):
        if 0 < nopeuden_muutos + self.tamanhetkinennopeus < self.huippunopeus:
            self.tamanhetkinennopeus = self.tamanhetkinennopeus + nopeuden_muutos
        elif self.tamanhetkinennopeus + nopeuden_muutos < 0:
            self.tamanhetkinennopeus = 0
        else:
            self.tamanhetkinennopeus = self.huippunopeus
    def kulje(self, tunnit):
        self.kuljettumatka = tunnit * self.tamanhetkinennopeus

#Pääohjelma
def main():
    auto1 = Auto("ABC-123", 142, 0, 0)
    auto1.kiihdyta(30)
    auto1.kiihdyta(70)
    auto1.kiihdyta(50)
    auto1.kulje(2)
    print(f"Auton rekisteritunnus:{auto1.rekisteritunnus} \nAuton huippunopeus:{auto1.huippunopeus}km/h")
    print(f"Auton nopeus:{auto1.tamanhetkinennopeus}")
    print(f"Auto on kulkenut {auto1.kuljettumatka}km")
    return
main()