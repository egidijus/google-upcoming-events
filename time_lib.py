#!/bin/env python

# this is for testing time problems in python
from datetime import datetime, date
from datetime import timedelta
from time import time
import calendar

now_date = datetime.now()


def timestamp_from_epoch(epoch_maybe_seconds):
    """
    i wanted to take in epoch time,
    either in seconds or milliseconds,
    and then convert it to a timestamp date object,
    which i use to do things.
    """
    if int and len(str(epoch_maybe_seconds)) == 13:
        epoch_milliseconds = epoch_maybe_seconds / 1000
        nice_timestamp_obj = datetime.fromtimestamp(epoch_milliseconds)
    elif datetime:
        nice_timestamp_obj = datetime.fromtimestamp(epoch_maybe_seconds)
        return nice_timestamp_obj
    else:
        nice_timestamp_obj = datetime.fromtimestamp(epoch_maybe_seconds)
    return nice_timestamp_obj


def datify_date(the_date):
    # the_date = the_date.replace(tzinfo, "None")
    # strftime Return a string representing the date and time, controlled by an explicit format string
    # strptime Return a datetime corresponding to date_string
    """
    This takes in the wierdo date like 'Dec 01 00:00:00 2018 GMT' and churns out a datetime compatible date
    we only chew first 20 charactes, because i do not want to faff with timezones
    """
    return datetime.strptime(the_date[:19], '%Y-%m-%dT%H:%M:%S')


def epoch_from_timestamp(atimestamp):
    """
    i want to produce an epoch from any timestamp datetime object
    """
    if datetime:
        # print(atimestamp)
        epoch_time = calendar.timegm(atimestamp.timetuple())
        return epoch_time
    else:
        print("mate, that is not a datetime")


def epoch_hours_ago(hours_ago):
    """
    you call it with int of hours, it returns epoch for that time
    """
    # timestamp_hours_ago = now_date - timedelta(hours=hours_ago)
    # epoch_hours_ago = epoch_from_timestamp(timestamp_hours_ago)
    return int((now_date - timedelta(hours=hours_ago)).timestamp()) * 1000


# print("the time", epoch_from_timestamp(now_date))
# print("rando date", timestamp_from_epoch(1543403560892))
# print("something now", (timestamp_from_epoch(time())))
# print("right now manual", datetime.fromtimestamp(time()))
# print("right now in epoch", int(time()))
# print("right now in epoch LONG", int(round(time() * 1000)))
cooltime = datify_date('2019-04-11T12:30:00+01:00')

print(type(cooltime))
print(cooltime.strftime('%A, %d. %B %Y %I:%M%p'))
