from datetime import datetime
from time import sleep
from playsound import playsound

alarm_time = datetime.strptime(input("When to wake up? \nInput example: 2020 Oct 2 08 30\n"), "%Y %b %d %H %M")
sleep((alarm_time - datetime.now()).total_seconds())
while True:
    playsound('good_alarm.mp3')