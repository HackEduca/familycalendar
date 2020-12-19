from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file config/token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

"""
Prints the list of calendar you have access
"""
creds = None

# The file config/token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('config/token.pickle'):
    with open('config/token.pickle', 'rb') as token:
        creds = pickle.load(token)
else:
    raise Exception('config/token.pickle not found. Run "pyhton3 connect_google_calendar.py"')

# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        raise Exception('config/token.pickle expired and cannot refresh. Run "pyhton3 connect_google_calendar.py"')

service = build('calendar', 'v3', credentials=creds)

# Call the Calendar API
now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
calendars_result = service.calendarList().list(maxResults=10, minAccessRole='reader', showDeleted=False).execute()
calendars = calendars_result.get('items', [])

if not calendars:
    print('No calendars found.')
for calendar in calendars:
    print(calendar['id'], calendar['summary'], calendar['backgroundColor'], calendar['foregroundColor'])
