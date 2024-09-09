va = ("talvi", "kevät", "kesä", "syksy")

kn = int(input("Anna kuukauden numero: "))

if kn == 12:
    print("Vuodenaika on " + va[0])
else:
    print("Vuodenaika on " + va[kn // 3])