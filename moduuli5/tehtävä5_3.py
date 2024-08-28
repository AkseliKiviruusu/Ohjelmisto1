luku = int(input("Anna luku: "))
on_alkuluku = False

if (luku % 2 == 0) or (luku == 0) or (luku == 1):
    print("Ei ole alkuluku")
elif luku == 2:
    print("On alkuluku")
else:
    for i in range(2,luku):
        if luku % i != 0:
            on_alkuluku = True
if on_alkuluku == True:
    print("On alkuluku")
else:
    print("Ei ole alkuluku")