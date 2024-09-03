import math

def yksikkohinta(halkaisija, hinta):
    sade_m = halkaisija / 200
    ala = sade_m ** 2 * math.pi
    epn = round((hinta / ala), 2)
    return epn

halkaisija_1 = float(input("Ensimmäisen pizzan halkaisija senttimetreinä: "))
hinta_1 = float(input("Ensimmäisen pizzan hinta euroina: "))
halkaisija_2 = float(input("Toisen pizzan halkaisija senttimetreinä: "))
hinta_2 = float(input("Toisen pizzan hinta euroina: "))

pizza_1 = yksikkohinta(halkaisija_1, hinta_1)
pizza_2 = yksikkohinta(halkaisija_2, hinta_2)

print(f"Ensimmäinen pizza: {pizza_1}€/m^2")
print(f"Toisen pizza: {pizza_2}€/m^2")

if pizza_1 < pizza_2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle")
else:
    print("Toinen pizza antaa paremman vastineen rahalle")
