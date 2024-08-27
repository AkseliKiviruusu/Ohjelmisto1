luku = float(input("Anna luku: "))
suurin = luku
pienin = luku

while str(luku) != "":
    luku = input("Anna luku: ")
    if luku != "":
        if suurin < float(luku):
            suurin = float(luku)
        else: suurin = suurin
        if pienin > float(luku):
            pienin = float(luku)
        else: pienin = pienin

print(f"Pienin antamasi luku: {pienin}")
print(f"Suurin antamasi luku: {suurin}")