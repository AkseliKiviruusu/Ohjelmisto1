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

#Pääohjelma
def main():
    auto1 = Auto("ABC-123", 142, 0, 0)
    print(f"Auton rekisteritunnus:{auto1.rekisteritunnus} \nAuton huippunopeus:{auto1.huippunopeus}km/h")
    auto1.kiihdyta(30)
    auto1.kiihdyta(70)
    auto1.kiihdyta(50)
    print(f"Auton nopeus:{auto1.tamanhetkinennopeus}")
    auto1.kiihdyta(-200)
    print(f"Auton nopeus:{auto1.tamanhetkinennopeus}")
    return
main()