#!/usr/bin/python

# RPHD parses the pihole logs and displays information on the 2x16 LCD display connected to the RPi.

import time, datetime
import Adafruit_CharLCD as LCD

# Variables
LOG_FILE = "/var/log/pihole.log"   # Location of the log file on the raspberry pi

Months = {}
Months[1] = "Jan"
Months[2] = "Feb"
Months[3] = "Mar"
Months[4] = "Apr"
Months[5] = "May"
Months[6] = "Jun"
Months[7] = "Jul"
Months[8] = "Aug"
Months[9] = "Sep"
Months[10] = "Oct"
Months[11] = "Nov"
Months[12] = "Dec"



# LCD variables
#lcd_rs        = 27  # Note this might need to be changed to 21 for older revision Pi's.
#lcd_en        = 22
#lcd_d4        = 25
#lcd_d5        = 24
#lcd_d6        = 23
#lcd_d7        = 18
#lcd_backlight = 4
#lcd_columns   = 16
#lcd_rows      = 2

# Initialize LCD object
#lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
lcd = LCD.Adafruit_CharLCDPlate()
lcd.set_color(0.0, 0.0, 1.0)
lcd.clear()

print("Raspberry Pi - Pihole Display started...")

with open(LOG_FILE) as f:
    while True:
        today = datetime.date.today()
        d = Month(today.month) + " " + today.day
        line = f.readline()
        if line:
            #print(line)
            lcd.message(line)