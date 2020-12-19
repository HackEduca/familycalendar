from __future__ import print_function
import time
import json
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import datetime, date, timedelta
from settings import CALENDAR_LIST
from funcs import echoMsg, echoError

calendarService = None

def getNextEvents():

    global calendarService

    creds = None

    try:

        if os.path.exists('config/token.pickle'):
            with open('config/token.pickle', 'rb') as token:
                creds = pickle.load(token)
        else:
            raise Exception('config/token.pickle not found')

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                raise Exception('config/token.pickle expired and cannot refresh')

        calendarService = build('calendar', 'v3', credentials=creds)

        timeMin = (date.today()-timedelta(days=30)).isoformat() + 'T00:00:00.0000Z' # 'Z' indicates UTC time
        timeMax = (date.today()+timedelta(days=60)).isoformat() + 'T00:00:00.0000Z' # 'Z' indicates UTC time

        # Recuperamos los calendarios que se indican en CALENDAR_LIST
        events = []
        for calendarId in CALENDAR_LIST.keys():
            events += getEvents(calendarId, timeMin, timeMax)

        # Ahora ordenamos los eventos por la fecha de inicio
        events = sorted(events, key=lambda k: k['start'])

        with open('data/events.json', 'w') as fout:
            json.dump(events , fout)

        return True

    except:
        e = sys.exc_info()[1]
        echoError(str(e))
        return False


def getEvents(calendarId, timeMin, timeMax):

    global calendarService

    ret = []

    # Call the Calendar API
    events_result = calendarService.events().list(calendarId=calendarId,
                                                    timeMin=timeMin,
                                                    timeMax=timeMax,
                                                    maxResults=100,
                                                    singleEvents=True,
                                                    orderBy='startTime').execute()

    events = events_result.get('items', [])

    if not events:
        print('No hi han events.')

    for event in events:
        evt = {}
        evt['owner'] = calendarId
        evt['start'] = event['start'].get('dateTime', event['start'].get('date'))
        evt['summary'] = event['summary'] if "summary" in event else "-- Privat"
        ret.append(evt)

    return ret

if __name__ == '__main__':
    getNextEvents()
