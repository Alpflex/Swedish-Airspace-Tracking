import time
from myimport import *
from key import *




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



#main()









