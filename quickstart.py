########Import ############
from myconfig import *
from key import *
from myimport import *
################

#### running the main part of the code,  write()
api = OpenSkyApi_key



api = OpenSkyApi_key


def search_previous(previous_planes):
    # Använd global för att komma åt api utanför funktionen
    global api

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

    # Returnera resultatet och tidigare flygplan
    return results, set(result["Icao24"] for result in results)


def write():
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        # Initialisera tidigare flygplan
        previous_planes = set()

        while True:
            # Hämta aktuella flygplan och tidigare flygplan
            current_results, current_planes = search_previous(previous_planes)

            # Hitta nya flygplan genom att subtrahera tidigare set från nuvarande set
            new_planes = current_planes - previous_planes
            # Hitta flygplan som har lämnat genom att subtrahera nuvarande set från tidigare set
            left_planes = previous_planes - current_planes

            # Uppdatera previous_planes
            previous_planes = current_planes

            if new_planes or left_planes:
                # Skriv bara till Google Sheet om det finns nya eller borttagna flygplan
                service = build("sheets", "v4", credentials=creds)
                sheets = service.spreadsheets()

                for result in current_results:
                    if result["Icao24"] in new_planes or result["Icao24"] in left_planes:
                        request_body = {
                            "requests": [
                                {
                                    "insertDimension": {
                                        "range": {
                                            "sheetId": 0,
                                            "dimension": "ROWS",
                                            "startIndex": 1,
                                            "endIndex": 2
                                        },
                                        "inheritFromBefore": False
                                    }
                                }
                            ]
                        }
                        response = sheets.batchUpdate(spreadsheetId=SPREADSHEET_ID, body=request_body).execute()

                        callsign = result["Callsign"]
                        icao24 = result["Icao24"]
                        longitude = result["Longitude"]
                        latitude = result["Latitude"]
                        country = result["Country"]
                        time_now = result["Time"]

                        values = [[callsign, icao24, longitude, latitude, country, time_now]]
                        resource = {"values": values}

                        sheets.values().update(
                            spreadsheetId=SPREADSHEET_ID,
                            range="A2",
                            valueInputOption='USER_ENTERED',
                            body=resource
                        ).execute()

                print("Added new rows and data to the top of your Google Sheet.")


            # Vänta innan nästa iteration
            time.sleep(180)  # 60 sekunder väntetid

    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    write()

"""


def write():

    #See, edit, create, and delete all your Google Sheets spreadsheets.
    # https://developers.google.com/sheets/api/scopes
  SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.

    # check if token.jason exist
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
      results = search_previous()
      service = build("sheets", "v4", credentials=creds)
      sheets = service.spreadsheets()

      for result in results:
          # For each result, insert a new row at the top
          request_body = {
              "requests": [
                  {
                      "insertDimension": {
                          "range": {
                              "sheetId": 0,
                              "dimension": "ROWS",
                              "startIndex": 1,  # adds empty row on second row
                              "endIndex": 2
                          },
                          "inheritFromBefore": False
                      }
                  }
              ]
          }
          response = sheets.batchUpdate(spreadsheetId=SPREADSHEET_ID, body=request_body).execute()

            # gets airplane info from file myconfig.py
          var0, var1, var2, var4, var5 = result
          x = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
          values = [[var0, var1, var2, var4, var5, x]]
          resource = {"values": values}
            # writes the output to first empty row
          sheets.values().update(
              spreadsheetId=SPREADSHEET_ID,
              range="A2",
              valueInputOption='USER_ENTERED',
              body=resource
          ).execute()

      print("Added new rows and data to the top of your Google Sheet.")
      # print(result)


  except HttpError as err:
      print(err)


def main():
    write()




if __name__ == "__main__":
  main()



"""