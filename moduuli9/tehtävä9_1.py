class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinennopeus, kuljettumatka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinennopeus = tamanhetkinennopeus
        self.kuljettumatka = kuljettumatka

#Pääohjelma
def main():
    auto1 = Auto("ABC-123", 142, 0, 0)
    print(f"Auton rekisteritunnus:{auto1.rekisteritunnus} \nAuton huippunopeus:{auto1.huippunopeus}km/h")
    return
main()