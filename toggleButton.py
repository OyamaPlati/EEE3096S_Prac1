
#!/usr/bin/python3
"""
Read just this Docstring as follows:
Names: Oyama Plati
Student Number: PLTOYA001
Prac: 1
Date: 27/07/2019
"""

# Import Relevant Librares
import RPi.GPIO as GPIO
from time import sleep
# Prepare the raspberry Pi for code
# Define naming converntion
GPIO.setmode(GPIO.BOARD)
# Setup variables for pin numbers
BUTTON=16
LED=11
# Setup Pin 16 as input, activated pull up resistor
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Disable WARNINGS from being printed to the screen
GPIO.setwarnings(False)
# Setup GPIO output pin
GPIO.setup(LED, GPIO.OUT)
# Set output to OFF
GPIO.output(LED, False)
BS=False # Keep track of LED states
# Logic tO write
def main():
    global BS # Accessing global 'BS'
    if GPIO.input(BUTTON)==False:
        # Button pressed
        print("Button pressed")
        if BS==False:
            GPIO.output(LED, True) # Turn LED on
            BS=True	# Change button state
            sleep(0.5) # Wait for system to run background programs
        else:
            GPIO.output(LED, False) # Turn LED off
            BS=False # Change button state
            sleep(0.5)

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
