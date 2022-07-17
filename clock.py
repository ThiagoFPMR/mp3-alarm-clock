from datetime import datetime
from time import sleep
from playsound import playsound

now = datetime.now()
input_time = input(
    "Takes in time of waking up as hour and minute using 24H system.\n(You can separate them by a space or colon).\nWhen to wake up? ")
input_time = input_time.replace(":", " ")

# Adjusting the day for tomorrow if the time given is earlier than the current time
day = now.day
if int(input_time[0]) < now.hour:
    day += 1
elif int(input_time[0]) == now.hour and int(input_time[1]) < now.minute:
    day += 1

time_str = f"{now.year} 0{now.month} {day} {input_time}"
# Gets the time to play the alarm
alarm_time = datetime.strptime(time_str, "%Y %m %d %H %M")
# Set which ringtone will be used
ringtone_path = 'good_alarm.mp3'
# Change if it's a weekend
if alarm_time.weekday() in [0, 6]:
    ringtone_path = 'good_alarm2.mp3'
# Sleeps until the given time and plays it
sleep((alarm_time - datetime.now()).total_seconds())
while True:
    playsound(ringtone_path)
