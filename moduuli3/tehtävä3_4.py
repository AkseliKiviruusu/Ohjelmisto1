vuosi = int(input("Anna vuosiluku: "))

if ((vuosi % 100 == 0 and vuosi % 400 == 0)
        or vuosi % 4 == 0
        and (vuosi % 100) % 400 > 0)\
        and vuosi != 0:
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")