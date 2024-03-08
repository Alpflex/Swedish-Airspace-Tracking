import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#test
from myconfig import Search
import datetime
from key import *

def write():
  # If modifying these scopes, delete the file token.json.
  SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

  # The ID and range of a sample spreadsheet.


  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
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
          var0, var1, var2, var4, var5 = result
          x = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

          list = [[var0, var1, var2, var4, var5, x]]
          resource = {"majorDimension": "ROWS", "values": list}

          sheets.values().append(
              spreadsheetId=SPREADSHEET_ID,
              range=blad,
              valueInputOption='USER_ENTERED',
              body=resource
          ).execute()
      print(result)
      print(list)
      print("Added new rows to your Google sheet")

  except HttpError as err:
      print(err)


def main():
    write()




if __name__ == "__main__":
  main()
