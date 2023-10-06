import RPi.GPIO as GPIO
import time

# relay pinout
relay_grass = 14
relay_pine = 15
relay_light = 2


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(relay_grass, GPIO.OUT)
GPIO.setup(relay_pine, GPIO.OUT)
GPIO.setup(relay_light, GPIO.OUT)


def off_everything():
    print("off_everything")
    GPIO.output(relay_grass, False)
    GPIO.output(relay_pine, False)
    GPIO.output(relay_light, False)


if __name__ == '__main__':
    off_everything()
