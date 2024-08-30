import math

luku = input("Anna luku: ")

while luku != "":
    luku = int(luku)
    if luku < 2:
        print("Ei ole alkuluku")
    elif luku == 2:
        print("On alkuluku")
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
    luku = input("Anna luku: ")