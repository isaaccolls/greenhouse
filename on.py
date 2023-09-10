import RPi.GPIO as GPIO
import time

# relay_grass = 14
# relay_pine = 15
# relay_light = 2

led_panel = 14
fan_cooler = 15
status = 2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(led_panel, GPIO.OUT)
GPIO.setup(fan_cooler, GPIO.OUT)
GPIO.setup(status, GPIO.OUT)


def on_everything():
    print("on led_panel")
    GPIO.output(fan_cooler, True)


if __name__ == '__main__':
    on_everything()
