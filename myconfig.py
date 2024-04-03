import time
from myimport import *
from key import *

api = OpenSkyApi_key


def search_previous():
    global previous_planes  # Använd global för att komma åt previous_planes utanför funktionen
    global api  # Använd global för att komma åt api utanför funktionen

    # OpenSkyApi credentials
    states = api.get_states()

    # En lista för att lagra resultatet
    results = []

    # Loopa igenom alla flygplan
    for s in states.states:
        if "SAS" in s.callsign[0:5] and s.origin_country == "Sweden":
            result = {
                "Callsign": s.callsign,
                "Icao24": s.icao24,
                "Longitude": s.longitude,
                "Latitude": s.latitude,
                "Country": s.origin_country,
                "Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            results.append(result)

    return results


# Exempel på användning
if __name__ == '__main__':
    # Initialisera api och previous_planes
    api = OpenSkyApi_key
    previous_planes = set()

    while True:
        current_results = search_previous()

        # Skapa ett set av ICAO24-koder för aktuella flygplan
        current_planes = set(result["Icao24"] for result in current_results)

        # Hitta nya flygplan genom att subtrahera tidigare set från nuvarande set
        new_planes = current_planes - previous_planes
        # Hitta flygplan som har lämnat genom att subtrahera nuvarande set från tidigare set
        left_planes = previous_planes - current_planes

        # Om det finns nya flygplan eller flygplan som har lämnat, uppdatera previous_planes
        if new_planes or left_planes:
            previous_planes = current_planes

        # Hantera de nya eller borttagna flygplanen
        print("Nya flygplan:", new_planes)
        print("Borttagna flygplan:", left_planes)

        # Vänta innan nästa sökning
        time.sleep(60)  # 60 sekunder väntetid







"""
if current_results:
    # Skapa ett set av ICAO24-koder för aktuella flygplan
    current_planes = set(result[1] for result in current_results)

    # Hitta nya flygplan genom att subtrahera tidigare set från nuvarande set
    new_planes = current_planes - previous_planes
    # Hitta flygplan som har lämnat genom att subtrahera nuvarande set från tidigare set
    left_planes = previous_planes - current_planes

    # Skriv ut information om nya flygplan
    for icao24 in new_planes:
        print(f"Nytt SAS-plan i svenskt luftrum: {icao24}")



    # Skriv ut information om flygplan som har lämnat
    for icao24 in left_planes:
        print(f"SAS-plan har lämnat svenskt luftrum: {icao24}")

    # Uppdatera tidigare flygplan med nuvarande för nästa iteration
    previous_planes = current_planes

# Vänta i 60 sekunder innan nästa sökning
time.sleep(60)
"""






"""

def Search():
    # OpenSkyApi credentials
    api = OpenSkyApi_key
    states = api.get_states()

    # for loop, using icao24 to find airplane
    results = []
    for s in states.states:
        if "SAS" in s.callsign[0:5] and s.origin_country == "Sweden":
            result = (
                f"Callsign: {s.callsign}",
                f'Icao24: {s.icao24}',
                f"Longitude: {s.longitude}",
                f"Latitude: {s.latitude}",
                f"Country: {s.origin_country}"
            )
            results.append(result)
    return results


previous_planes = set()

while True:  # Kör detta i en oändlig loop
    # Sök efter SAS-flygplan i Sverige
    current_results = Search()

    if current_results:
        # Skapa ett set av ICAO24-koder för aktuella flygplan
        current_planes = set(result[1] for result in current_results)

        # Hitta nya flygplan genom att subtrahera tidigare set från nuvarande set
        new_planes = current_planes - previous_planes
        # Hitta flygplan som har lämnat genom att subtrahera nuvarande set från tidigare set
        left_planes = previous_planes - current_planes

        # Skriv ut information om nya flygplan
        for icao24 in new_planes:
            print(f"Nytt SAS-plan i svenskt luftrum: {icao24}")



        # Skriv ut information om flygplan som har lämnat
        for icao24 in left_planes:
            print(f"SAS-plan har lämnat svenskt luftrum: {icao24}")

        # Uppdatera tidigare flygplan med nuvarande för nästa iteration
        previous_planes = current_planes

    # Vänta i 60 sekunder innan nästa sökning
    time.sleep(60)


"""




