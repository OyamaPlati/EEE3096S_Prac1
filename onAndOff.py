
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
# Disable WARNINGS from being printed to the screen
GPIO.setwarnings(False)
# Setup GPIO output pin
GPIO.setup(11, GPIO.OUT)
# Set output to OFF
GPIO.output(11, False)


# Logic tO write
def main():
    GPIO.output(11, True) # Turn LED on
    print("LED ON and Pin 11 (BOARD) : " +str(GPIO.input(11)))
    sleep(1)
    GPIO.output(11, False) # Turn LED off
    print("LED OFF and Pin 11 (BOARD): " + str(GPIO.input(11)))
    sleep(1)

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
