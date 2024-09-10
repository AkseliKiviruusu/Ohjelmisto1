def new_airport(new_nimi, new_icao):
    lentokentat[f"{new_icao}"] = f"{new_nimi}"
    return lentokentat

def airport_info(info_icao):
    if info_icao in lentokentat:
        print(f"lentoaseman nimi: {lentokentat[info_icao]}")
        print(f"lentoaseman ICAO-koodi: {info_icao}")
    else:
        print("Lentoasemaa ei löytynyt")
    return

lentokentat = {"HECA":"Cairo international airport",
               "EFHK":"Helsinki-Vantaa airport",
               "EGLL":"Heathrow airport",
               "ZSPD":"Shanghai Pudong international airport",
               "KJFK":"John F. Kennedy international airport"}

def main():
    ind = int(input("Haluatko syöttää uuden lentoaseman(1), Hakea jo syötetyn lentoaseman tiedot(2) vai lopettaa toiminnot(3):\n"))
    if ind == 1 or ind == 2 or ind == 3:
        while ind != 3:
            if ind == 1:
                new_nimi = input("Syötä lentoaseman nimi: ")
                print()
                new_icao = input("Syötä lentoaseman ICAO-koodi: ")
                new_airport(new_nimi, new_icao)
            elif ind == 2:
                info_icao = input("Syötä lentoaseman ICAO-koodi: ")
                airport_info(info_icao)
            ind = int(input("Haluatko syöttää uuden lentoaseman(1), Hakea jo syötetyn lentoaseman tiedot(2) vai lopettaa toiminnot(3):\n"))
        print("lopetit toiminnot")
    else:
        print("teit jotain väärin")
    return

main()