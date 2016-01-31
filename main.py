#!/usr/bin/python
# RPHD parses the pihole logs and displays information on the 2x16 LCD display connected to the RPi.
# This version of this script is an exercise in using classes. The main objective was to create a script
# that only updates the display as necessary, because the updates take a lot of time.

import time, datetime
import Adafruit_CharLCD as LCD

# Variables
LOG_FILE = "/var/log/pihole.log"  # Location of the log file on the raspberry pi
NETWORK_IP = "192.168.178."
PIHOLE_IP = "192.168.178.3"
MATCHSTRING = "is " + PIHOLE_IP
Months = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct",
          11: "Nov", 12: "Dec"}
RED = (1.0, 0.0, 0.0)
GREEN = (1.0, 1.0, 0.0)
BLUE = (0.0, 0.0, 1.0)

alert = RED
remark = BLUE
ok = GREEN


class LCDDisplay(LCD.Adafruit_CharLCDPlate):
    # Subclassed the Adafruit class to create specific functions for writing to the two-line display
    def __init__(self):
        LCD.Adafruit_CharLCDPlate.__init__(self)
        self.currentlines = ("", "")
        self.newlines = ("", "")

    def write(self, lines, state=ok):
        self.setstate(state)
        self.newlines = lines
        if self.newlines != self.currentlines:
            self.update() # Updating the display is very slow, so only do that if necessary

    def update(self):
        self.clear()
        self.set_cursor(0, 0)
        self.message(self.newlines[0])
        self.set_cursor(0, 1)
        self.message(self.newlines[1])
        self.currentlines = self.newlines

    def setstate(self, state):
        self.set_color(state[0], state[1], state[2])


lcd = LCDDisplay()
lcd.autoscroll(False)
blocked = 0
processed = 0

f = open(LOG_FILE)
num_lines = sum(1 for line in f)

lcd.write(("Initializing", "Please stand by"), remark)

print("Initializing. Pattern to match is [%s]" % MATCHSTRING)
print("Searching through %s lines" % num_lines)

 # Go back to the start of the file
f.seek(0,0)

while processed < num_lines: # initial phase, where the log is parsed. Do not update display because it takes forever.
    logline = f.readline()
    processed += 1
    if MATCHSTRING in logline:
        blocked += 1

print("Initialization complete. Found %s lines, containing %s blocked IPs" % (processed, blocked))
lcd.write(("Blocked: %s" % blocked, "Init complete"))

while True: # continuous phase
    logline = f.readline()
    if MATCHSTRING in logline:
        blocked += 1
        print("Blocked %s" % logline[55:-len(MATCHSTRING)-2])
        lcd.write(("Blocked: %s" % blocked, logline[55:-len(MATCHSTRING)-2]))





