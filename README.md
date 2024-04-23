
# Swedish-Airspace-Tracking

Swedish-Airspace-Tracking is a Python script designed to monitor and track active aircraft within Swedish airspace.
It utilizes data from various sources to identify and track the positions and statuses of aircraft.




## Features
- Monitors aircraft with callsigns starting with "SAS" and originating from Sweden.
- Retrieves and displays aircraft information including callsign, ICAO24 identifier, longitude, latitude, and country of origin.
- Records the current time of data retrieval in the format YYYY-MM-DD HH:MM:SS.
- Inserts new data into a Google Sheets spreadsheet, allowing for real-time updates and tracking.


## How it Works
The application runs continuously, checking for new aircraft entering or leaving the monitored airspace.

When new aircraft are detected or existing ones leave, it updates the Google Sheets spreadsheet with the relevant information.

## Screenshots
https://alpflex.github.io/Swedish-Airspace-Tracking/

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Built With
- OpenSky Network API
- Google Sheets API
- Python
- 
## Contributing
Contributions to the Swedish-Airspace-Tracking project are welcome. Please feel free to fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
