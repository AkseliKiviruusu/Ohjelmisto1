GRAMMA = 1
KILO = 1000 * GRAMMA
LUOTI = 13.3 * GRAMMA
NAULA = 32 * LUOTI
LEIVISKA = 20 * NAULA

leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

grammat = (luodit * LUOTI + naulat * NAULA + leiviskat * LEIVISKA)
kilot = float(grammat) /1000
massa_kilot = round(float(grammat) // 1000)
massa_grammat = round((float(kilot) - float(massa_kilot)) * 1000)

print("Massa nykymittojen mukaan: kilot: " + str(massa_kilot),"grammat: " + str(massa_grammat))