
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
def onClickButton():
    global COUNTER
    if (GPIO.input(UP_BUTTON) == False and COUNTER != 7):
        COUNTER += 1
        print (bin(COUNTER)[2:].zfill(3))
        sleep(0.5)
    if (GPIO.input(UP_BUTTON) == False and COUNTER == 7):
        COUNTER = 0
        print (bin(COUNTER)[2:].zfill(3))
        sleep(0.5)
    if (GPIO.input(DOWN_BUTTON) == False and COUNTER != 0):
        COUNTER -= 1
        print (bin(COUNTER)[2:].zfill(3))
        sleep(0.5)
    if (GPIO.input(DOWN_BUTTON) == False and COUNTER == 0):
        COUNTER = 7
        print (bin(COUNTER)[2:].zfill(3))
        sleep(0.5)
    return

def control(counter):
    binaryValue = bin(counter)[2:].zfill(3)
    for key, value in enumerate(binaryValue):
        if (value == '1'):
            onValue(key)
        else:
            offValue(key)
    return

def onValue(pin):
    if (pin == 0):
        GPIO.output(LED_1, True)
    if (pin == 1):
        GPIO.output(LED_2, True)
    if (pin == 2):
        GPIO.output(LED_3, True)
    return

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
    onClickButton()
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