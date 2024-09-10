import mysql.connector
from geopy.distance import geodesic

def calc_distance():
    icao_1 = get_coordinates_by_icao(input("Anna ensimmäinen ICAO-koodi:\n"))
    icao_2 = get_coordinates_by_icao(input("Anna toinen ICAO-koodi:\n"))

    distance = geodesic(icao_1[0], icao_2[0])
    print(f"Lentoasemien etäisyys:{distance}")
    return distance

def get_coordinates_by_icao(icao):
    sql = """
    select latitude_deg, longitude_deg
from airport
where airport.ident = %s
    """
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao,))
    coordinates = kursori.fetchall()
    return coordinates

yhteys = mysql.connector.connect(
         host = '127.0.0.1',
         port = 3306,
         database = 'flight_game',
         user = 'akselikiviruusu',
         password = 'Rm4g9090?',
         autocommit = True
         )

calc_distance()