import config
import mysql.connector

def get_airport_by_icao(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = %s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao, ))
    airport_data = kursori.fetchall()
    return airport_data

yhteys = mysql.connector.connect(
         host = '127.0.0.1',
         port = 3306,
         database = 'flight_game',
         user = config.user,
         password = config.password,
         autocommit = True
         )

name_municipality = get_airport_by_icao(input("Anna lentoaseman ICAO-koodi: "))
for i in name_municipality:
    print(f"Lentoaseman nimi: \n{i[0]}")
    print(f"Sijaintikunta: \n{i[1]}")