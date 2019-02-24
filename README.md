# What
A pythonistic way of viewing upcoming calendar events.
This is based on https://developers.google.com/calendar/quickstart/python

We have tech team culture meetings about improving culture and quality of life for the tech team, and I thought, it would be nice to have a shared calendar where the team can see all events, so it is easier to join in and participate. Instead of copying events from the google calendar UI, I made this tool to make it easy for me to announce upcoming events.

# How

Visit this page to enable google api auth: https://developers.google.com/calendar/quickstart/python
Save the auth tokens in the same directory as this script.

Install dependencies.
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

run this like so:
```
python main.py
```

Get a lovely output like this:
```
Getting the upcoming 10 Tech Team Events
Event :: Daily Standup, Location :: Whiteboard / Hangout, Start time :: 2019-02-25T10:00:00Z, End time :: 2019-02-25T10:30:00Z, Click here for details :: https://www.google.com/calendar/event?eid=rrrrrrrrrrrrr

```

By default this targets YOUR primary calendar, if you would like to target any other calendar in google, you should change the `CALENDAR_ID`.
You can find the calendar id by following this guide: https://wiki.mozilla.org/Help:Widget:Google_Calendar#Share_your_Google_Calendar
