########Import ############
from myconfig import Search
from key import *
from myimport import *
################

#### running the main part of the code,  write()
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
      results = Search()
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
