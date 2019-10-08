import RPi.GPIO as GPIO
import time

# Variable for the GPIO pin number
led_panel = 21
fan_cooler = 21
status = 16

# Tell the Pi we are using the breakout board pin numbering
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin for output
GPIO.setup(led_panel, GPIO.OUT)
GPIO.setup(fan_cooler, GPIO.OUT)
GPIO.setup(status, GPIO.OUT)

# Loop to blink our led
k = 0
while k < 3:
    GPIO.output(led_panel, True)
    GPIO.output(fan_cooler, True)
    GPIO.output(status, True)
    print("On")
    time.sleep(1)
    GPIO.output(led_panel, False)
    GPIO.output(fan_cooler, False)
    GPIO.output(status, False)
    print("Off")
    time.sleep(1)
    k = k + 1
GPIO.cleanup()
