import time
from myimport import *

from key import *
def main():

    limit = 1
    a = 1
    # While loop, always runs
    while a < 2:

        a += 1
        #Search()


def Search():
    # OpenSkyApi credentials
    api = OpenSkyApi("", "")
    states = api.get_states()
    # for loop, using icao24 to find airplane
    time.sleep(1)

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
            # Om du vill fortsätta att göra något här, gör det innan loopen avslutas
    return results



main()









