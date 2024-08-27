luku = float(input("Anna luku: "))
suurin_luku = luku
pienin_luku = luku

while str(luku) != str():
    luku = input("Anna luku: ")
    if luku != "":
        if suurin_luku < float(luku):
            suurin_luku = float(luku)
        else: suurin_luku = suurin_luku
        if pienin_luku > float(luku):
            pienin_luku = float(luku)
        else: pienin_luku = pienin_luku

print(f"Pienin antamasi luku: {pienin_luku}")
print(f"Suurin antamasi luku: {suurin_luku}")