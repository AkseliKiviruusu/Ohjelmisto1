kuha_pituus = float(input("Kerro kuhan pituus senttimetreinä: "))
if kuha_pituus < 37:
    print("Kuha on ", 37 - int(kuha_pituus), "cm alamittainen, laske se takaisin järveen")
else:
    print("Hieno kuha, pidä se :)")
