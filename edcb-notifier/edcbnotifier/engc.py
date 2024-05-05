from datetime import datetime

from googleapiclient.discovery import build
from google.oauth2 import service_account


class ENGC:

    # public

    SCOPES = ['https://www.googleapis.com/auth/calendar']
    SERVICE_ACCOUNT_FILE = 'secrets/credentials_service.json'

    def __init__(self, calendar_id:str) -> None:
        self.credentials = service_account.Credentials.from_service_account_file(ENGC.SERVICE_ACCOUNT_FILE, scopes=ENGC.SCOPES)
        self.calendar = build('calendar', 'v3', credentials=self.credentials)
        self.calendar_id = calendar_id

    def add_event(self, macros:dict) -> dict:
        start_time = f'{macros["SDYYYY"]}/{macros["SDMM"]}/{macros["SDDD"]} {macros["STHH"]}:{macros["STMM"]}:{macros["STSS"]}'
        end_time = f'{macros["EDYYYY"]}/{macros["EDMM"]}/{macros["EDDD"]} {macros["ETHH"]}:{macros["ETMM"]}:{macros["ETSS"]}'
        new_event = {
            'summary': macros['Title'],
            'location': macros['ServiceName'],
            'start': {
                'dateTime': datetime.strptime(start_time, '%Y/%m/%d %H:%M:%S').isoformat(),
                'timeZone': 'Asia/Tokyo',
            },
            'end': {
                'dateTime': datetime.strptime(end_time, '%Y/%m/%d %H:%M:%S').isoformat(),
                'timeZone': 'Asia/Tokyo',
            },
        }
        return self.calendar.events().insert(calendarId=self.calendar_id, body=new_event).execute()

