#Before running the script, pip install -r requirements.txt

#Download all the required python libraries
from __future__ import print_function


import datetime as dt
import os.path
import holidays

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json. 
SCOPES = ['https://www.googleapis.com/auth/calendar']

creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

#Possible attendees emails
emails = [{"email": "angeline.marcelle11@gmail.com"}]

#Avoid weekend and public holiday function
def is_weekend_or_holiday(date):
    # Check if the date is a weekend or in a public holiday
    hk_holidays = holidays.CountryHoliday('HK')
    if date.weekday() in [5, 6] or (date in hk_holidays):
        return True
    return False


def main():
    # Important things, don't edit
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token: #'w' is in writing mode
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        #Edit start date and name with on-boarding details
        start_date = dt.datetime(2023, 7, 21) #edit the start date of the new talent (year, month, date)
        talent_name = "Frankie" # put in name of new talent
       
        #Flags, don't edit
        event_date = start_date
        start_datetime = event_date.strftime("%Y-%m-%dT00:00:00")
        end_datetime = event_date.strftime("%Y-%m-%T00:00:00")
        
        # NEW TALENT ON-BOARDING CODE
        ''' 
        for i in range(4):
            # Fill in details for the new meetings
            if i == 0:
                event_date = start_date + dt.timedelta(days=0)
                event_name = f"[On-Boarding] {talent_name} On-Boarding"
                description = f"Day 1 {talent_name} On Boarding. PIC: People team."
                start_time = "T11:00:00"
                end_time = "T12:30:00"
                attendees_email = [{"email": "angeline.marcelle11@gmail.com"}]

                start_datetime = event_date.strftime(f"%Y-%m-%d{start_time}")
                end_datetime = event_date.strftime(f"%Y-%m-%d{end_time}")
            
            elif i == 1:
                event_date += dt.timedelta(days=30)
                event_name = "1-on-1 Chat"
                description = "First month 1-on-1 meeting with People Team. Raise concerns..."
                start_time = "T09:30:00"
                end_time = "T10:30:00"
                attendees_email = [{"email": "angeline.marcelle11@gmail.com"}]

                start_datetime = event_date.strftime(f"%Y-%m-%d{start_time}")
                end_datetime = event_date.strftime(f"%Y-%m-%d{end_time}")
            
            elif i == 2:
                event_date += dt.timedelta(days=45)
                event_name = "Probation Team Reminder"
                description = "To all team heads, please report probation status..."
                start_time = "T09:50:00"
                end_time = "T10:00:00"
                attendees_email = [{"email": "angeline.marcelle11@gmail.com"}]
                
                start_datetime = event_date.strftime(f"%Y-%m-%d{start_time}")
                end_datetime = event_date.strftime(f"%Y-%m-%d{end_time}")
            
            elif i == 3:
                event_date += dt.timedelta(days=15)
                event_name = "Probation Meeting"
                start_time = "T13:00:00"
                end_time = "T15:00:00"
                attendees_email = [{"email": "angeline.marcelle11@gmail.com"}]
                
                start_datetime = event_date.strftime(f"%Y-%m-%d{start_time}")
                end_datetime = event_date.strftime(f"%Y-%m-%d{end_time}")

            # Keep generating an event date until a valid date (weekday and not a public holiday) is found
            while is_weekend_or_holiday(event_date):
                event_date += dt.timedelta(days=1)
                start_datetime = event_date.strftime(f"%Y-%m-%d{start_time}")
                end_datetime = event_date.strftime(f"%Y-%m-%d{end_time}")

            # Create the event with the calculated name and date
            event = {
                "summary": event_name,
                "description": description,
                "colorId": 5,
                "start": {
                        "dateTime": start_datetime,
                        "timeZone": "Asia/Hong_Kong"
                },
                "end": {
                        "dateTime": end_datetime,
                        "timeZone": "Asia/Hong_Kong"
                },
                "attendees": attendees_email,
            }

            # Insert the event into the calendar
            event = service.events().insert(calendarId = "primary", body = event).execute()
            print(f"Event created {event.get('htmlLink')}")
        '''

        #NEW CANDIDATE EVENT CREATION
        '''
        event_date = 
        event_name = f"Video Interview with {name}"
        description = "Video Interview Round 1"
        start_datetime = start_date.strftime("%Y-%m-%dT09:00:00")
        end_datetime = start_date.strftime("%Y-%m-%dT10:00:00")
        attendees_email = [{"email": "adelia.kusumawardhani@preface.ai"}]

        event = {
                "summary": event_name,
                "description": description,
                "colorId": 1,
                "start": {
                        "dateTime": start_datetime,
                        "timeZone": "Asia/Hong_Kong"
                },
                "end": {
                        "dateTime": end_datetime,
                        "timeZone": "Asia/Hong_Kong"
                },
                "attendees": attendees_email,
        }

        # Insert the event into the calendar
        event = service.events().insert(calendarId = "primary", body = event).execute()
        print(f"Event created {event.get('htmlLink')}")
        '''

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()
