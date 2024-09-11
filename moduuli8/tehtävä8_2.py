import config
import mysql.connector

def laske_maara(tyyppi):
    maara_small_airport = 0

    for i in range(len(airport_list)):
        if airport_list[i] == (tyyppi):
            maara_small_airport += 1

    print(f"{tyyppi} määrä: {maara_small_airport}")

def get_airport_type_by_country_name(country_id):
    sql = """
    select airport.type
    from airport
    inner join country on country.iso_country = airport.iso_country
    where country.iso_country = %s
    """
    kursori = yhteys.cursor(dictionary = True)
    kursori.execute(sql, (country_id,))
    airport_type = kursori.fetchall()
    return airport_type

yhteys = mysql.connector.connect(
         host = '127.0.0.1',
         port = 3306,
         database = 'flight_game',
         user = config.user,
         password = config.password,
         autocommit = True
         )

def main():
    airport_type = get_airport_type_by_country_name(input("Anna valtiotunnus: "))
    for type in airport_type:
        airport_list.append(f"{type['type']}")

    laske_maara("small_airport")
    laske_maara("medium_airport")
    laske_maara("large_airport")
    laske_maara("heliport")
    laske_maara("closed")
    laske_maara("seaplane_base")
    return

airport_list = []
main()