from datetime import datetime
from time import sleep
from playsound import playsound

# Gets the time to play the alarm
alarm_time = datetime.strptime(input("When to wake up? \nInput example: 2020 Oct 2 08 30\n"), "%Y %b %d %H %M")
# Set which ringtone will be used
ringtone_path = 'good_alarm.mp3'
# Change if it's a weekend
if alarm_time.weekday() in [0, 6]:
    ringtone_path = 'good_alarm2.mp3'
# Sleeps until the given time and plays it
sleep((alarm_time - datetime.now()).total_seconds())
while True:
    playsound(ringtone_path)