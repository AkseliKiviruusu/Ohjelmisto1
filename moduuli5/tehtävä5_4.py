kaupungit = []
kerrat = 0

# tehtävänannossa "for", luennolla sanottiin käyttää "while" komentoa.

while kerrat < 5:
    kerrat = kerrat + 1
    kaupungit.append(input("Anna satunnaisen kaupungin nimi: "))

for kaupunki in kaupungit:
    print(kaupunki)