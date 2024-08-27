KAYTTAJA = "python"
SALASANA = "rules"

annettu_kayttaja = str(input("Anna käyttäjätunnus: "))
annettu_salasana = str(input("Anna salasana: "))

kerrat = 0

while (annettu_kayttaja != KAYTTAJA or annettu_salasana != SALASANA) and kerrat <= 4:
    kerrat = kerrat + 1
    print("Pääsy evätty.")
    annettu_kayttaja = str(input("Anna käyttäjätunnus: "))
    annettu_salasana = str(input("Anna salasana: "))

if kerrat <= 4:
    print("Tervetuloa!")
else:
    print("Syötit väärät tiedot liian monta kertaa.")