#!/usr/bin/python

# RPHD parses the pihole logs and displays information on the 2x16 LCD display connected to the RPi.

import time, datetime
import Adafruit_CharLCD as LCD

# Variables
LOG_FILE = "/var/log/pihole.log"   # Location of the log file on the raspberry pi
NETWORK_IP = "192.168.178."
PIHOLE_IP = "is 192.168.178.3" # This seems to be the matchstring for a redirect to self
#LOG_FILE = "pihole.log"
Months = {1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun", 7:"Jul", 8:"Aug", 9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"}

Blocked = 0
processedLines = 0
line = ""
lastLine = ""
rewrite = False

# Initialize LCD object
lcd = LCD.Adafruit_CharLCDPlate()
lcd.set_color(1.0, 0.0, 0.0)
lcd.clear()

print("Starting...")
lcd.message("Starting...")

f = open(LOG_FILE)
while True:
    today = datetime.date.today()
    d = Months[today.month] + " " + str(today.day)
    line = f.readline()
    if line != lastLine:
        processedLines += 1
        if (d in line) and (PIHOLE_IP in line):
            Blocked += 1
        rewrite = True
    elif rewrite == True:
        rewrite = False
        lcd.set_color(0.0, 0.0, 1.0)
        lcd.set_cursor(0,0)
        lcd.message("Requests %s" % d)
        lcd.set_cursor(0,1)
        lcd.message("Blocked %s" % Blocked)
    lastLine = line
