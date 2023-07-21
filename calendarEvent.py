import datetime
import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Google Calendar API credentials setup
SCOPES = ['https://www.googleapis.com/auth/calendar']
creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

# Create Google Calendar service
service = build('calendar', 'v3', credentials=creds)

# Define start and end dates
start_date = datetime.datetime(2023, 5, 17)
end_date = datetime.datetime(2023, 7, 16)

# Create events from start_date to end_date
current_date = start_date
while current_date <= end_date:
    event_date = current_date.date().isoformat()
    event_summary = f"Day-{(current_date - start_date).days+1}"
    event = {
        'summary': event_summary,
        'start': {
            'date': event_date,
            'timeZone': 'Asia/Kolkata',  # Replace with your timezone
        },
        'end': {
            'date': event_date,
            'timeZone': 'Asia/Kolkata',  # Replace with your timezone
        },
    }

    # Add event to Google Calendar
    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f"Event '{event['summary']}' added on {event_date}")

    # Move to the next day
    current_date += datetime.timedelta(days=1)
