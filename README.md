# Calendar Event Automation for Placement Preparation

This script was designed to automate the process of adding events to my Google Calendar for tracking my 60-day preparation window for placements. It creates a series of events named "Day-1", "Day-2", and so on, covering the specified date range.

## Setup Google Calendar API

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project and enable the Google Calendar API.
3. Create credentials (OAuth client ID) and download the credentials file in JSON format.
4. Save the downloaded credentials file as `credentials.json` in the same directory as the Python script.

## Installation

Install the required Python libraries by running the following command in your command line or terminal:

```
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

## Configuration

Update the script with the following details:

1. Replace `'Your_Timezone'` in the script with your desired timezone (e.g., 'America/New_York', 'Europe/London', etc.).
2. Modify the `start_date` and `end_date` variables to define your desired date range.

## Usage

1. Execute the Python script in your preferred Python environment.
2. The script will prompt you to authorize access to your Google Calendar account.
3. Once authorized, it will start adding the events to your Google Calendar one by one.

## Improvisation

If you have any specific requirements or improvements in mind, you can modify the script as needed. For example, you could add more information to the event's description or set different time intervals between events. The script can be extended to include additional functionalities based on your preferences.

Please feel free to make the necessary modifications to suit your unique needs.

Enjoy using this automation to keep track of your placement preparation!
