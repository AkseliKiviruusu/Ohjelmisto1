def muunnos(gallonat):
    while float(gallonat) > 0:
        litrat = float(gallonat) / 3.785
        print(f"Bensiinin määrä litroina: {litrat}")
        gallonat = (input("Anna bensiinin määrä gallonina: "))
    return

muunnos(input("Anna bensiinin määrä gallonina: "))