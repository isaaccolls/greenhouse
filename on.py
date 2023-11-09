import RPi.GPIO as GPIO
import time

# relay pinout
relay_grass = 15
relay_pine = 14
relay_light = 2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(relay_grass, GPIO.OUT)
GPIO.setup(relay_pine, GPIO.OUT)
GPIO.setup(relay_light, GPIO.OUT)


def on_everything():
    print("on_everything")
    GPIO.output(relay_grass, False)
    # GPIO.output(relay_pine, False)
    # GPIO.output(relay_light, False)


if __name__ == '__main__':
    on_everything()
