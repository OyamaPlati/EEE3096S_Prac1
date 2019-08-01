
#!/usr/bin/python3
"""
Read just this Docstring as follows:
Names: Oyama Plati
Student Number: PLTOYA001
Prac: 1
Date: 28/07/2019
"""

# Import Relevant Librares
import RPi.GPIO as GPIO
from time import sleep
# Prepare the raspberry Pi for code
# Define naming converntion
GPIO.setmode(GPIO.BOARD)
# Setup variables for pin numbers
UP_BUTTON=16
DOWN_BUTTON=12
LED_1=11
LED_2=7
LED_3=13

# Setup Pin 16 as input, activated pull up resistor
GPIO.setup(UP_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Setup Pin 12 as input, activated pull up resistor
GPIO.setup(DOWN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Disable WARNINGS from being printed to the screen
GPIO.setwarnings(False)

# Setup GPIO output pin 11, 7 AND 13
GPIO.setup(LED_1, GPIO.OUT)
GPIO.setup(LED_2, GPIO.OUT)
GPIO.setup(LED_3, GPIO.OUT)

# Set output to OFF
GPIO.output(LED_1, False)
GPIO.output(LED_2, False)
GPIO.output(LED_3, False)

# Global Variables
COUNTER=0

# Save Button Presses
def onClickButtonUp(channel):
    global COUNTER
    if (GPIO.event_detected(channel) and COUNTER != 7): # Ok! to increment
        COUNTER += 1
        print (bin(COUNTER)[2:].zfill(3))
        sleep(0.5)
    if (GPIO.event_detected(channel) and COUNTER == 7): # Stop increment and Restart
        COUNTER = 0 # At 0
        print (bin(COUNTER)[2:].zfill(3))
        sleep(0.5)
    return

def onClickButtonDown(channel):
    global COUNTER
    if (GPIO.event_detected(channel) and COUNTER != 0): # Ok! to decrement
        COUNTER -= 1
        print (bin(COUNTER)[2:].zfill(3))
        sleep(0.5)
    if (GPIO.event_detected(channel) and COUNTER == 0): # Stop decrement and Restart
        COUNTER = 7 # At 7
        print (bin(COUNTER)[2:].zfill(3))
        sleep(0.5)
    return

# Add rising edge detection on a channel, ignoring further edges for 200ms for switchbouncing
GPIO.add_event_detect(UP_BUTTON, GPIO.RISING, callback=onClickButtonUp, bouncetime=200)
GPIO.add_event_detect(DOWN_BUTTON, GPIO.RISING, callback=onClickButtonDown, bouncetime=200)

# Control on and off state of LEDs
def control(counter):
    binaryValue = bin(counter)[2:].zfill(3)
    for key, value in enumerate(binaryValue):
        if (value == '1'):
            onValue(key) # Set appropiate LEDs to HIGH
        else:
            offValue(key) # Set appropiate LEDs to LOW
    return
# Select LEDs to be set HIGH
def onValue(pin):
    if (pin == 0):
        GPIO.output(LED_1, True)
    if (pin == 1):
        GPIO.output(LED_2, True)
    if (pin == 2):
        GPIO.output(LED_3, True)
    return
# Select LEDs to be set LOW
def offValue(pin):
    if (pin == 0):
        GPIO.output(LED_1, False)
    if (pin == 1):
        GPIO.output(LED_2, False)
    if (pin == 2):
        GPIO.output(LED_3, False)
    return

# Logic tO write
def main():
    global UP_BUTTON
    global DOWN_BUTTON
    onClickButtonUp(UP_BUTTON)
    onClickButtonDown(DOWN_BUTTON)
    control(COUNTER)

# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
