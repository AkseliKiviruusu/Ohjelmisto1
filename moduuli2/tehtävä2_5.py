gramma = 1
kilogramma = 1000 * float(gramma)
luoti = 13.3 * float(gramma)
naula = 32 * float(luoti)
leiviska = 20 * float(naula)

leiviska_massa = input("Anna leiviskät: ")
naula_massa = input("Anna naulat: ")
luoti_massa = input("Anna luodit: ")

grammat = (float(luoti_massa) * float(luoti) +
                   float(naula_massa) * float(naula) +
                   float(leiviska_massa) * float(leiviska))
kilot = float(grammat) /1000
massa_kilot = round(float(grammat) // 1000)
massa_grammat = round((float(kilot) - float(massa_kilot)) * 1000)

print("Massa nykymittojen mukaan: kilot: " + str(massa_kilot),"grammat: " + str(massa_grammat))
