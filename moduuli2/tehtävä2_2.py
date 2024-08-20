import math

sade_str = input('Anna ympyran sade: ')
sade = float(sade_str)
pintaala = (sade ** 2) * math.pi
pintaala = round(pintaala, 2)
print("Ympyran pinta-ala: " + str(pintaala))
