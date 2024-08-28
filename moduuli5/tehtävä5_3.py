import math

luku = int(input("Anna luku: "))

if luku < 2:
    print("Ei ole alkuluku")
elif luku == 2:
    print("Ei ole alkuluku")
else:
    on_alkuluku = True
    for i in range(2, int(math.sqrt(luku)) + 1):
        if luku % i == 0:
            on_alkuluku = False
            break
    if on_alkuluku:
        print("On alkuluku")
    else:
        print("Ei ole alkuluku")