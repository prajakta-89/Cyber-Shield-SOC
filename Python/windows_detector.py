import win32evtlog
import mysql.connector
import time

server = "localhost"
logtype = "Security"

handle = win32evtlog.OpenEventLog(server, logtype)

flags = win32evtlog.EVENTLOG_BACKWARDS_READ | \
        win32evtlog.EVENTLOG_SEQUENTIAL_READ

events = win32evtlog.ReadEventLog(handle, flags, 0)

for event in events[:10]:

    print("Event ID:", event.EventID & 0xFFFF)