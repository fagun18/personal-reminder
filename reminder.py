import datetime
import time
import os

def reminder(message, delay):
    time.sleep(delay)
    os.system("notify-send 'Reminder' '{}'".format(message))

reminder_time = input("Enter the reminder time in the format HH:MM: ")
reminder_message = input("Enter the reminder message: ")
current_time = datetime.datetime.now().time()
reminder_time = datetime.datetime.strptime(reminder_time, "%H:%M").time()
delay = (datetime.datetime.combine(datetime.date.today(), reminder_time) - 
         datetime.datetime.combine(datetime.date.today(), current_time)).total_seconds()

if delay < 0:
    delay += 86400

reminder(reminder_message, delay)
