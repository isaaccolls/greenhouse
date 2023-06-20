import RPi.GPIO as GPIO
import time

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
    GPIO.output(led_panel, True)
    print("On fan_cooler")
    GPIO.output(fan_cooler, True)
    print("on status")
    GPIO.output(status, True)
    time.sleep(1)


if __name__ == '__main__':
    on_everything()
