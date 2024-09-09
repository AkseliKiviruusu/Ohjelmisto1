nimet = set()
nimi = str(input("Anna nimi: "))
nimet.add(nimi)
while nimi != "":
    nimi = str(input("Anna nimi: "))
    if nimi not in nimet:
        print("Uusi nimi")
    else:
        print("Aiemmin syötetty nimi")
    if nimi != "":
        nimet.add(nimi)

for nimi in nimet:
    print(nimi)