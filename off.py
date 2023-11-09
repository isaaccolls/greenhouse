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
    GPIO.output(relay_grass, True)
    # GPIO.output(relay_pine, True)
    # GPIO.output(relay_light, True)


if __name__ == '__main__':
    off_everything()
