# RaspberryPi-Pihole-Display
This short Python scripts is used in the very specific case where a Raspberry Pi serves as a Pihole ad blocker and has a 2x16 LCD connected. The scripts parses the log and displays the number of domain requests blocked on the first line, and the last domain blocked on the last line.

It uses the class provided by Adafruit for their display and subclasses it for this specific purpose. My pihole is located near my server in a closet, and I wanted the display to do something.
